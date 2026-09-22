import pandas as pd
from sklearn.preprocessing import StandardScaler
from .schema import FEATURE_COLUMNS

def standardize_behavioral_features(df):
    scaler = StandardScaler()
    Z = scaler.fit_transform(df[FEATURE_COLUMNS])
    return Z, scaler
