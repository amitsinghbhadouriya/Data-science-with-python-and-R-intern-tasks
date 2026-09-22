"""
Data Science Research Capstone
Financial Transaction Fraud Risk & Pattern Analysis

Run:
    python src/capstone_analysis.py data/capstone_demo_dataset.csv

The script also works with the original fraud_test_dataset.csv if the
same column names are present.
"""
import os
# Prevent KMeans memory leak UserWarning on Windows with MKL
os.environ["OMP_NUM_THREADS"] = "1"

import sys
import warnings
from pathlib import Path
import pandas as pd
from scipy.stats import mannwhitneyu
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, silhouette_score

warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

REQUIRED = [
    "transaction_id","customer_id","transaction_date","transaction_time",
    "amount","merchant_category","payment_method","location","device_type",
    "is_fraud","previous_transactions","account_age_days","failed_attempts"
]

def load_data(path):
    df = pd.read_csv(path)
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    df["timestamp"] = pd.to_datetime(df["transaction_date"] + " " + df["transaction_time"], errors="coerce")
    df = df.dropna(subset=["timestamp","amount","is_fraud"]).copy()
    df["hour"] = df["timestamp"].dt.hour
    return df

def main(path):
    df = load_data(path)
    features = ["amount","previous_transactions","account_age_days","failed_attempts","hour"]
    X, y = df[features], df["is_fraud"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=42
    )

    models = {
        "Logistic Regression": Pipeline([
            ("scale", StandardScaler()),
            ("model", LogisticRegression(max_iter=2000, class_weight="balanced", random_state=42))
        ]),
        "Random Forest": RandomForestClassifier(
            n_estimators=300, max_depth=6, class_weight="balanced",
            random_state=42
        )
    }

    print(f"Dataset path: {path}")
    print(f"Rows: {len(df)}")
    print(f"Fraud rate: {y.mean():.2%}")

    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        proba = model.predict_proba(X_test)[:,1]
        print(f"\n--- {name} ---")
        print("Accuracy :", round(accuracy_score(y_test,pred),4))
        print("Precision:", round(precision_score(y_test,pred,zero_division=0),4))
        print("Recall   :", round(recall_score(y_test,pred,zero_division=0),4))
        print("F1       :", round(f1_score(y_test,pred,zero_division=0),4))
        print("ROC-AUC  :", round(roc_auc_score(y_test,proba),4))

    # Statistical tests
    fraud_amount = df.loc[y==1, "amount"]
    normal_amount = df.loc[y==0, "amount"]
    u_amt, p_amt = mannwhitneyu(fraud_amount, normal_amount, alternative="two-sided")
    print(f"\nAmount Mann-Whitney U: {u_amt} (p-value: {p_amt:.4e})")

    fraud_failed = df.loc[y==1, "failed_attempts"]
    normal_failed = df.loc[y==0, "failed_attempts"]
    u_fail, p_fail = mannwhitneyu(fraud_failed, normal_failed, alternative="two-sided")
    print(f"Failed Attempts Mann-Whitney U: {u_fail} (p-value: {p_fail:.4e})")

    # K-Means clustering
    Z = StandardScaler().fit_transform(df[features])
    km = KMeans(n_clusters=3, n_init=20, random_state=42)
    labels = km.fit_predict(Z)
    sil = silhouette_score(Z, labels)
    print(f"\nKMeans silhouette (k=3): {round(sil, 4)}")

    df["cluster"] = labels
    summary = df.groupby("cluster").agg(
        transactions=("transaction_id", "count"),
        fraud_rate=("is_fraud", "mean"),
        avg_amount=("amount", "mean"),
        avg_failed=("failed_attempts", "mean")
    )
    print("\nCluster Summary:")
    print(summary)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
    else:
        # Default fallback paths for convenient execution
        candidates = [
            Path("data/capstone_demo_dataset.csv"),
            Path(__file__).resolve().parent.parent / "data" / "capstone_demo_dataset.csv",
            Path("data_science_capstone_whitepaper/data/capstone_demo_dataset.csv"),
            Path("../data/capstone_demo_dataset.csv")
        ]
        csv_path = None
        for p in candidates:
            if p.exists():
                csv_path = str(p)
                break
        if csv_path is None:
            raise SystemExit("Usage: python src/capstone_analysis.py <csv_path>")

    main(csv_path)
