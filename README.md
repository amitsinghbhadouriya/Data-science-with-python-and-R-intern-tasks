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
