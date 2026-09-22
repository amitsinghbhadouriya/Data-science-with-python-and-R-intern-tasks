import pandas as pd

def extract_temporal_features(df):
    df = df.copy()
    df["timestamp"] = pd.to_datetime(
        df["transaction_date"] + " " + df["transaction_time"], errors="coerce"
    )
    df["hour"] = df["timestamp"].dt.hour
    df["is_night"] = ((df["hour"] < 6) | (df["hour"] >= 23)).astype(int)
    return df
