import pandas as pd
import numpy as np

def compute_summary_statistics(df):
    total = len(df)
    fraud_count = int(df["is_fraud"].sum())
    fraud_rate = df["is_fraud"].mean()
    return {
        "total_rows": total,
        "fraud_count": fraud_count,
        "fraud_rate": fraud_rate,
        "unique_customers": df["customer_id"].nunique()
    }
