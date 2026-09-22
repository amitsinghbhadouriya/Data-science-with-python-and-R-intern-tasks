import pandas as pd

def clean_and_prepare_features(df):
    df = extract_temporal_features(df)
    cleaned_df = df.dropna(subset=["timestamp", "amount", "is_fraud"]).copy()
    cleaned_df["is_fraud"] = cleaned_df["is_fraud"].astype(int)
    return cleaned_df

def extract_temporal_features(df):
    df = df.copy()
    df["timestamp"] = pd.to_datetime(
        df["transaction_date"] + " " + df["transaction_time"], errors="coerce"
    )
    df["hour"] = df["timestamp"].dt.hour
    df["is_night"] = ((df["hour"] < 6) | (df["hour"] >= 23)).astype(int)
    return df
