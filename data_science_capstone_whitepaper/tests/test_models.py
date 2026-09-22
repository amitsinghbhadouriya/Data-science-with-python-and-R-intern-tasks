import pandas as pd
from src.models import get_model_suite, split_train_test, evaluate_models

def test_model_training_and_evaluation():
    df = pd.DataFrame({
        "amount": [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600],
        "previous_transactions": [10, 20] * 8,
        "account_age_days": [100, 200] * 8,
        "failed_attempts": [0, 1] * 8,
        "hour": [10, 12, 14, 16, 18, 20, 22, 23] * 2,
        "is_fraud": [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
    })
    X_train, X_test, y_train, y_test = split_train_test(df, test_size=0.25, random_state=42)
    models = get_model_suite()
    results, fitted = evaluate_models(models, X_train, X_test, y_train, y_test)
    assert len(results) == 2
    assert "ROC-AUC" in results[0]
