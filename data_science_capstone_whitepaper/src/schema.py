REQUIRED_COLUMNS = [
    "transaction_id", "customer_id", "transaction_date", "transaction_time",
    "amount", "merchant_category", "payment_method", "location", "device_type",
    "is_fraud", "previous_transactions", "account_age_days", "failed_attempts"
]

FEATURE_COLUMNS = [
    "amount", "previous_transactions", "account_age_days", "failed_attempts", "hour"
]

def validate_schema(df):
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns in dataset: {missing}")
    return True
