# Architecture & Methodological Flow

This document outlines the methodological and structural framework governing the data pipelines, hypothesis tests, and modeling workflows in this repository.

```mermaid
graph TD
    A[Raw Datasets] --> B[Data Ingestion & Integrity Validation]
    B --> C1[Parametric & Non-Parametric Hypothesis Testing]
    B --> C2[Time-Series Decomposition & SARIMA Grid Search]
    B --> C3[Feature Scaling & Dimensionality Reduction - PCA]
    B --> C4[Supervised Classification - RF / Logistic Regression]
    
    C1 --> D1[Effect Sizes & Confirmatory Results]
    C2 --> D2[Out-of-Sample Holdout & 30-Day Projections]
    C3 --> D3[Unsupervised Cluster Profiling - KMeans / DBSCAN]
    C4 --> D4[Model Benchmark Evaluation & Whitepaper PDF]
```

## Modular Design Guidelines
1. **Determinism:** All random operations use seeded generators (`random_state=42`).
2. **Confirmatory Separation:** Preregistered analysis plans are strictly separated from exploratory data transformations.
3. **Pipeline Encapsulation:** Scaling and transformations are packaged inside scikit-learn `Pipeline` objects to prevent data leakage.
