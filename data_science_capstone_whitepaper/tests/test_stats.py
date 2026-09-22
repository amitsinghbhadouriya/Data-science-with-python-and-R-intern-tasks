import pandas as pd
from src.stats_tests import run_statistical_tests

def test_statistical_tests():
    df = pd.DataFrame({
        "amount": [10000, 20000, 15000, 50, 100, 75],
        "failed_attempts": [4, 5, 6, 0, 1, 0],
        "is_fraud": [1, 1, 1, 0, 0, 0]
    })
    results = run_statistical_tests(df)
    assert len(results) == 2
    assert results[0]["p-value"] < 0.05
    assert results[1]["p-value"] < 0.05
