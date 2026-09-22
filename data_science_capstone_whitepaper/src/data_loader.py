import pandas as pd
from pathlib import Path
from .schema import validate_schema

def load_transaction_data(file_path):
    p = Path(file_path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    df = pd.read_csv(p)
    validate_schema(df)
    return df
