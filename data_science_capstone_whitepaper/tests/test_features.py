import pandas as pd
from src.features import clean_and_prepare_features, extract_temporal_features

def test_temporal_features():
    df = pd.DataFrame({
        "transaction_date": ["2026-08-01", "2026-08-01"],
        "transaction_time": ["03:30:00", "14:15:00"],
        "amount": [100.0, 50.0],
        "is_fraud": [1, 0]
    })
    res = clean_and_prepare_features(df)
    assert "hour" in res.columns
    assert "is_night" in res.columns
    assert list(res["hour"]) == [3, 14]
    assert list(res["is_night"]) == [1, 0]

def test_clean_null_records():
    df = pd.DataFrame({
        "transaction_date": ["2026-08-01", "invalid"],
        "transaction_time": ["03:30:00", "time"],
        "amount": [100.0, None],
        "is_fraud": [1, None]
    })
    res = clean_and_prepare_features(df)
    assert len(res) == 1
