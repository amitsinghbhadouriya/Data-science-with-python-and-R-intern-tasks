import pytest
import pandas as pd
from src.data_loader import load_transaction_data
from src.schema import validate_schema, REQUIRED_COLUMNS

def test_validate_schema_valid():
    df = pd.DataFrame(columns=REQUIRED_COLUMNS)
    assert validate_schema(df) is True

def test_validate_schema_missing():
    df = pd.DataFrame(columns=["transaction_id", "amount"])
    with pytest.raises(ValueError) as exc:
        validate_schema(df)
    assert "Missing required columns" in str(exc.value)
