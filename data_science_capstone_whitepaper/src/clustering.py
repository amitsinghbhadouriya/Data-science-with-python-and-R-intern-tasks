import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from .schema import FEATURE_COLUMNS

def standardize_behavioral_features(df):
    scaler = StandardScaler()
    Z = scaler.fit_transform(df[FEATURE_COLUMNS])
    return Z, scaler

def run_clustering_pipeline(df, n_clusters=3, random_state=42):
    Z, scaler = standardize_behavioral_features(df)
    km = KMeans(n_clusters=n_clusters, n_init=20, random_state=random_state)
    labels = km.fit_predict(Z)
    sil = silhouette_score(Z, labels)
    df_clustered = df.copy()
    df_clustered["cluster"] = labels
    return df_clustered, sil

def compute_cluster_summary(df_clustered):
    summary = df_clustered.groupby("cluster").agg(
        transactions=("transaction_id", "count"),
        avg_amount=("amount", "mean"),
        fraud_rate=("is_fraud", "mean"),
        avg_failed_attempts=("failed_attempts", "mean"),
        avg_hour=("hour", "mean")
    ).reset_index()
    return summary
