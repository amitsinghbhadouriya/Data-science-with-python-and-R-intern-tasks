from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from .schema import FEATURE_COLUMNS

def get_model_suite():
    return {
        "Logistic Regression": Pipeline([
            ("scale", StandardScaler()),
            ("model", LogisticRegression(max_iter=2000, class_weight="balanced", random_state=42))
        ]),
        "Random Forest": RandomForestClassifier(
            n_estimators=300, max_depth=6, class_weight="balanced", random_state=42
        )
    }

def evaluate_models(models, X_train, X_test, y_train, y_test):
    results = []
    fitted_models = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        proba = model.predict_proba(X_test)[:, 1]
        metrics = {
            "Model": name,
            "Accuracy": round(accuracy_score(y_test, pred), 4),
            "Precision": round(precision_score(y_test, pred, zero_division=0), 4),
            "Recall": round(recall_score(y_test, pred, zero_division=0), 4),
            "F1": round(f1_score(y_test, pred, zero_division=0), 4),
            "ROC-AUC": round(roc_auc_score(y_test, proba), 4)
        }
        results.append(metrics)
        fitted_models[name] = model
    return results, fitted_models

def split_train_test(df, test_size=0.25, random_state=42):
    X = df[FEATURE_COLUMNS]
    y = df["is_fraud"].astype(int)
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=random_state)
