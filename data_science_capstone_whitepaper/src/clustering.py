import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from .schema import FEATURE_COLUMNS

def standardize_behavioral_features(df):
    scaler = StandardScaler()
    Z = scaler.fit_transform(df[FEATURE_COLUMNS])
    return Z, scaler

def evaluate_kmeans_clustering(Z, n_clusters=3, random_state=42):
    km = KMeans(n_clusters=n_clusters, n_init=20, random_state=random_state)
    labels = km.fit_predict(Z)
    sil = silhouette_score(Z, labels)
    return km, labels, sil
