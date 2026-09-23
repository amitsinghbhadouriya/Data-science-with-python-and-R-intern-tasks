# Data Science & Machine Learning Internship Portfolio

A comprehensive collection of data science, statistical analysis, machine learning, and time-series forecasting projects developed during the Data Science Internship.

---

## 📌 Repository Overview

This repository documents end-to-end practical implementations spanning classical hypothesis testing, preregistered epidemiological modeling, unsupervised clustering & dimensionality reduction, seasonal time-series forecasting, and an applied machine learning capstone research paper.

Each project is self-contained with its own datasets, executable pipelines or notebooks, unit tests, generated visual figures, and documentation.

---

## 📂 Project Directory Structure

```text
.
├── data_science_capstone_whitepaper/       # Capstone: Financial Transaction Fraud Risk & Pattern Analysis
│   ├── data/                               # Demonstration / evaluation dataset (CSV)
│   ├── figures/                            # High-resolution charts & diagnostic plots
│   ├── notebooks/                          # Interactive analysis workflow notebook
│   ├── report/                             # Published formal whitepaper (PDF)
│   ├── results/                            # JSON & CSV model performance, clusters & statistical tests
│   ├── src/                                # Reproducible analysis pipeline source code
│   ├── tests/                              # Unit & integration tests for data processing & models
│   └── README.md                           # Capstone project documentation
│
├── time_series_forecasting_deliverable/    # Daily Demand Time-Series Forecasting with SARIMA
│   ├── 01_historical_demand.png            # Historical demand visualization
│   ├── 02_decomposition.png                # Additive decomposition (Trend, Seasonality, Residuals)
│   ├── 03_holdout_forecast.png             # Validation backtest vs actual holdout data
│   ├── 04_30_day_forecast.png              # 30-day out-of-sample forecast with 95% confidence bands
│   ├── 30_day_forecast.csv                 # Tabular projected demand values
│   ├── adf_stationarity_results.csv        # Augmented Dickey-Fuller test metrics
│   ├── daily-demand-series.csv             # Raw input daily demand dataset
│   ├── implementation_note.md              # Technical methodology note
│   ├── sarima_model_selection_results.csv  # Grid search AIC model selection log
│   ├── time_series_forecasting_SARIMA.ipynb# Complete executable Jupyter notebook
│   └── README.md                           # Time-series project documentation
│
├── dimensionality_reduction_clustering_task/ # Unsupervised Learning & PCA Dimensionality Reduction
│   ├── Dimensionality_Reduction_Unsupervised_Clustering.ipynb # Interactive notebook
│   ├── requirements.txt                    # Project dependencies
│   └── README.md                           # Task documentation
│
├── analysis_preregistration_deliverable/   # Preregistered Epidemiological Analysis Pipeline
│   ├── data/                               # Dataset documentation & instructions
│   ├── outputs/                            # Results (JSON, CSV, analysis log)
│   ├── tests/                              # Data-blind synthetic pipeline test suite
│   ├── analysis.py                         # Analysis execution script
│   ├── preregistration.md                  # Locked preregistration protocol & hypotheses
│   ├── deviations.md                       # Deviation log tracking protocol adherence
│   ├── environment.yml                     # Conda environment definition
│   └── README.md                           # Preregistration deliverable documentation
│
└── advanced_statistical_analysis_task/     # Hypothesis Testing & Variance Analysis
    └── advanced_statistical_analysis_task/
        ├── Advanced_Statistical_Analysis_Hypothesis_Testing.ipynb # Executable notebook
        ├── requirements.txt                # Required libraries
        └── README.md                       # Statistical task documentation
```

---

## 🔍 Detailed Folder & Module Breakdown

### 1. [data_science_capstone_whitepaper](./data_science_capstone_whitepaper/)
* **Project Title:** Financial Transaction Fraud Risk & Pattern Analysis  
* **Problem Type:** Supervised Binary Classification & Unsupervised Behavioral Profiling  
* **Core Research Question:** Can transaction amount, failed-attempt frequency, account age, and transaction timing reliably predict fraudulent transactions?  
* **Key Components & Deliverables:**
  * **Formal Whitepaper:** [Data_Science_Capstone_Whitepaper.pdf](./data_science_capstone_whitepaper/report/Data_Science_Capstone_Whitepaper.pdf) — publication-grade capstone research report.
  * **Pipeline Script:** [`src/capstone_analysis.py`](./data_science_capstone_whitepaper/src/capstone_analysis.py) — modular end-to-end data processing, statistical validation, model training, and reporting pipeline.
  * **Interactive Notebook:** [`notebooks/01_capstone_analysis.ipynb`](./data_science_capstone_whitepaper/notebooks/01_capstone_analysis.ipynb).
  * **Test Suite:** [`tests/test_models.py`](./data_science_capstone_whitepaper/tests/test_models.py) verifying data processing and model validity.
  * **Results & Metrics:** Benchmark logs in [`results/`](./data_science_capstone_whitepaper/results/) comparing Logistic Regression vs. Random Forest, alongside K-Means behavioral clustering summaries ($k=3$) and Mann–Whitney U test statistics.
* **How to Run:**
  ```bash
  cd data_science_capstone_whitepaper
  pip install -r requirements.txt
  python -m pytest tests/
  python src/capstone_analysis.py data/capstone_demo_dataset.csv
  ```

---

### 2. [time_series_forecasting_deliverable](./time_series_forecasting_deliverable/)
* **Project Title:** Daily Demand Time-Series Forecasting with SARIMA  
* **Problem Type:** Univariate Time-Series Decomposition, Stationarity Testing & Forecasting  
* **Core Focus:** Modeling historical demand patterns, weekly seasonality ($m=7$), and delivering a robust 30-day out-of-sample demand forecast.  
* **Key Components & Deliverables:**
  * **Interactive Notebook:** [`time_series_forecasting_SARIMA.ipynb`](./time_series_forecasting_deliverable/time_series_forecasting_SARIMA.ipynb) with full outputs, diagnostic plots, and markdown evaluations.
  * **Statistical Artifacts:** [`adf_stationarity_results.csv`](./time_series_forecasting_deliverable/adf_stationarity_results.csv) verifying series stationarity and [`sarima_model_selection_results.csv`](./time_series_forecasting_deliverable/sarima_model_selection_results.csv) detailing AIC-ranked SARIMA configurations.
  * **Forecast Deliverable:** [`30_day_forecast.csv`](./time_series_forecasting_deliverable/30_day_forecast.csv) containing projected demand and 95% confidence intervals.
  * **Generated Visualizations:** Diagnostic figures covering historical trends, seasonal decomposition, holdout test set validation, and future projections.
* **How to Run:**
  ```bash
  cd time_series_forecasting_deliverable
  pip install -r requirements.txt
  jupyter notebook time_series_forecasting_SARIMA.ipynb
  ```

---

### 3. [dimensionality_reduction_clustering_task](./dimensionality_reduction_clustering_task/)
* **Project Title:** Dimensionality Reduction & Unsupervised Clustering  
* **Problem Type:** Feature Extraction, Dimensionality Reduction & Cluster Analysis  
* **Core Focus:** Evaluating cluster separation and structural discovery on multivariate feature spaces.  
* **Key Components & Deliverables:**
  * **Interactive Notebook:** [`Dimensionality_Reduction_Unsupervised_Clustering.ipynb`](./dimensionality_reduction_clustering_task/Dimensionality_Reduction_Unsupervised_Clustering.ipynb).
  * **Implemented Techniques:**
    * **Feature Standardization:** `StandardScaler` data normalization.
    * **PCA (Principal Component Analysis):** Scree plot analysis, cumulative explained variance ratio, 2D and 3D visual projections.
    * **K-Means Clustering:** Inertia Elbow Method and Silhouette Coefficient optimization across $k \in [2, 10]$.
    * **DBSCAN (Density-Based Clustering):** Epsilon ($\epsilon$) and `min_samples` parameter tuning with automated noise detection.
    * **Hierarchical / Agglomerative Clustering:** Ward linkage computation and cluster boundary comparisons.
* **How to Run:**
  ```bash
  cd dimensionality_reduction_clustering_task
  pip install -r requirements.txt
  jupyter notebook Dimensionality_Reduction_Unsupervised_Clustering.ipynb
  ```

---

### 4. [analysis_preregistration_deliverable](./analysis_preregistration_deliverable/)
* **Project Title:** BMI and 1-Year Disease Progression — Preregistered Analysis  
* **Problem Type:** Confirmatory Hypothesis Testing & Open Science Methodology  
* **Core Research Question:** Is baseline Body Mass Index (BMI) independently associated with one-year quantitative disease progression after adjusting for age and biological sex?  
* **Key Components & Deliverables:**
  * **Preregistration Document:** [`preregistration.md`](./analysis_preregistration_deliverable/preregistration.md) — locked, timestamped analysis specification defined prior to examining outcome relationships to prevent p-hacking and HARKing.
  * **Deviation Record:** [`deviations.md`](./analysis_preregistration_deliverable/deviations.md) logging protocol fidelity.
  * **Synthetic Pipeline Test:** [`tests/test_pipeline.py`](./analysis_preregistration_deliverable/tests/test_pipeline.py) enabling data-blind pipeline verification.
  * **Analysis Script:** [`analysis.py`](./analysis_preregistration_deliverable/analysis.py) computing regression coefficients, confidence intervals, model $R^2$, and logging all metrics to `outputs/`.
* **How to Run:**
  ```bash
  cd analysis_preregistration_deliverable
  pytest -q
  python analysis.py
  ```
