import pandas as pd
from scipy.stats import mannwhitneyu

def compute_rank_biserial(stat, n1, n2):
    # Rank-biserial correlation effect size r = 1 - 2*U / (n1*n2)
    return abs(1.0 - (2.0 * stat) / (n1 * n2))

def run_statistical_tests(df):
    fraud = df.loc[df["is_fraud"] == 1]
    normal = df.loc[df["is_fraud"] == 0]
    n1, n2 = len(fraud), len(normal)

    # Amount test
    stat_amt, p_amt = mannwhitneyu(fraud["amount"], normal["amount"], alternative="two-sided")
    effect_amt = compute_rank_biserial(stat_amt, n1, n2)

    # Failed attempts test
    stat_fail, p_fail = mannwhitneyu(fraud["failed_attempts"], normal["failed_attempts"], alternative="two-sided")
    effect_fail = compute_rank_biserial(stat_fail, n1, n2)

    return [
        {
            "Variable": "Amount",
            "Fraud median": float(fraud["amount"].median()),
            "Non-fraud median": float(normal["amount"].median()),
            "Mann-Whitney U": float(stat_amt),
            "p-value": float(p_amt),
            "Effect size": float(effect_amt)
        },
        {
            "Variable": "Failed attempts",
            "Fraud median": float(fraud["failed_attempts"].median()),
            "Non-fraud median": float(normal["failed_attempts"].median()),
            "Mann-Whitney U": float(stat_fail),
            "p-value": float(p_fail),
            "Effect size": float(effect_fail)
        }
    ]
