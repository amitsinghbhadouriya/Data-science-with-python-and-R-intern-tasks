import pandas as pd
from src.clustering import run_clustering_pipeline, compute_cluster_summary

def test_clustering():
    df = pd.DataFrame({
        "transaction_id": [f"TXN{i}" for i in range(10)],
        "amount": [100, 200, 150, 8000, 9000, 8500, 100, 200, 150, 9000],
        "previous_transactions": [10]*10,
        "account_age_days": [100]*10,
        "failed_attempts": [0]*10,
        "hour": [12]*10,
        "is_fraud": [0, 0, 0, 1, 1, 1, 0, 0, 0, 1]
    })
    df_clustered, sil = run_clustering_pipeline(df, n_clusters=2)
    summary = compute_cluster_summary(df_clustered)
    assert "cluster" in df_clustered.columns
    assert len(summary) == 2
