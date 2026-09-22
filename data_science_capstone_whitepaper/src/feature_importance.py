import numpy as np
import pandas as pd
from sklearn.inspection import permutation_importance
from .schema import FEATURE_COLUMNS

def compute_permutation_importance(model, X_test, y_test, random_state=42):
    r = permutation_importance(model, X_test, y_test, n_repeats=10, random_state=random_state)
    records = []
    for i, col in enumerate(FEATURE_COLUMNS):
        records.append({
            "feature": col,
            "importance_mean": float(r.importances_mean[i]),
            "importance_std": float(r.importances_std[i])
        })
    df_imp = pd.DataFrame(records).sort_values(by="importance_mean", ascending=False)
    return df_imp
