import pandas as pd
from scipy.stats import mannwhitneyu

def run_amount_mann_whitney(df):
    fraud = df.loc[df["is_fraud"] == 1, "amount"]
    normal = df.loc[df["is_fraud"] == 0, "amount"]
    stat, pval = mannwhitneyu(fraud, normal, alternative="two-sided")
    return {
        "variable": "Amount",
        "fraud_median": float(fraud.median()),
        "normal_median": float(normal.median()),
        "statistic": float(stat),
        "p_value": float(pval)
    }
