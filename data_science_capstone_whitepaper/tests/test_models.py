import pandas as pd
from src.models import get_model_suite, split_train_test, evaluate_models

def test_model_training_and_evaluation():
    df = pd.DataFrame({
        "amount": [100, 200, 300, 400, 500, 600, 700, 800],
        "previous_transactions": [10, 20, 10, 20, 10, 20, 10, 20],
        "account_age_days": [100, 200, 100, 200, 100, 200, 100, 200],
        "failed_attempts": [0, 1, 0, 1, 0, 1, 0, 1],
        "hour": [10, 12, 14, 16, 18, 20, 22, 23],
        "is_fraud": [0, 0, 0, 0, 1, 1, 0, 0]
    })
    X_train, X_test, y_train, y_test = split_train_test(df, test_size=0.25, random_state=42)
    models = get_model_suite()
    results, fitted = evaluate_models(models, X_train, X_test, y_train, y_test)
    assert len(results) == 2
    assert "ROC-AUC" in results[0]
