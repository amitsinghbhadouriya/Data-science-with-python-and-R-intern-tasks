import pandas as pd
from pathlib import Path
from .schema import validate_schema

CANDIDATE_PATHS = [
    Path("data/capstone_demo_dataset.csv"),
    Path("../data/capstone_demo_dataset.csv"),
    Path(__file__).resolve().parent.parent / "data" / "capstone_demo_dataset.csv",
    Path("data_science_capstone_whitepaper/data/capstone_demo_dataset.csv")
]

def resolve_dataset_path(provided_path=None):
    if provided_path:
        p = Path(provided_path)
        if p.exists():
            return str(p)
    for c in CANDIDATE_PATHS:
        if c.exists():
            return str(c)
    raise FileNotFoundError("Could not find capstone_demo_dataset.csv in candidate locations.")

def load_transaction_data(file_path=None):
    resolved = resolve_dataset_path(file_path)
    df = pd.read_csv(resolved)
    validate_schema(df)
    return df, resolved
