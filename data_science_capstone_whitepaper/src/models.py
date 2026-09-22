from sklearn.model_selection import train_test_split
from .schema import FEATURE_COLUMNS

def split_train_test(df, test_size=0.25, random_state=42):
    X = df[FEATURE_COLUMNS]
    y = df["is_fraud"].astype(int)
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=random_state)
