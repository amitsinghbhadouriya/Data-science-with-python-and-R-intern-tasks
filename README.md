# Data Science & Machine Learning Internship Portfolio

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Style: PEP 8](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://peps.python.org/pep-0008/)
[![Test Suite](https://img.shields.io/badge/tests-pytest%20passing-brightgreen.svg)](#-verification--testing)

A comprehensive collection of data science, statistical analysis, machine learning, and time-series forecasting projects developed during the Data Science Internship.

---

## 📌 Repository Overview

This repository documents end-to-end practical implementations spanning classical hypothesis testing, preregistered epidemiological modeling, unsupervised clustering & dimensionality reduction, seasonal time-series forecasting, and an applied machine learning capstone research paper.

Each project is self-contained with its own datasets, executable pipelines or notebooks, unit tests, generated visual figures, and documentation.

### Quick Links
- [📂 Project Directory Structure](#-project-directory-structure)
- [🔍 Detailed Folder & Module Breakdown](#-detailed-folder--module-breakdown)
- [📊 Summary Comparison Matrix](#-summary-comparison-of-modules)
- [⚙️ Environment Setup & Installation](#️-environment-setup--installation)
- [🧪 Verification & Testing](#-verification--testing)
- [📖 Replication Guide](docs/REPLICATION.md)
- [📐 Architecture & Methodology](docs/ARCHITECTURE.md)
- [🗃️ Dataset Registry](docs/DATA_REGISTRY.md)

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


---

### 5. [advanced_statistical_analysis_task](./advanced_statistical_analysis_task/)
* **Project Title:** Advanced Statistical Analysis & Hypothesis Testing  
* **Problem Type:** Inferential Statistics, Distribution Testing & Factorial ANOVA  
* **Core Focus:** Rigorous statistical evaluation across multi-group continuous datasets.  
* **Key Components & Deliverables:**
  * **Executable Notebook:** [`Advanced_Statistical_Analysis_Hypothesis_Testing.ipynb`](./advanced_statistical_analysis_task/advanced_statistical_analysis_task/Advanced_Statistical_Analysis_Hypothesis_Testing.ipynb).
  * **Implemented Statistical Methods:**
    * **Normality Assessment:** Shapiro–Wilk test, Kolmogorov–Smirnov test, histograms, and Q-Q plots.
    * **Two-Sample Testing:** Welch's Two-Sample t-test (heteroscedasticity-robust), Mann–Whitney U non-parametric test, 95% Confidence Intervals, and Cohen's $d$ effect size.
    * **One-Way ANOVA:** Analysis of variance across class groupings, Levene's test for variance homogeneity, and Tukey's HSD post-hoc pairwise analysis.
    * **Two-Way Factorial ANOVA:** Main effects, interaction term analysis, and Partial Eta-Squared ($\eta_p^2$) effect size computations.
* **How to Run:**
  ```bash
  cd advanced_statistical_analysis_task/advanced_statistical_analysis_task
  pip install -r requirements.txt
  jupyter notebook Advanced_Statistical_Analysis_Hypothesis_Testing.ipynb
  ```


---

## 📊 Summary Comparison of Modules

| Folder / Deliverable | Domain / Focus | Key Dataset | Primary Methods & Algorithms | Deliverable Format |
|---|---|---|---|---|
| **`data_science_capstone_whitepaper`** | Fraud Risk & Predictive Modeling | Financial transactions dataset | Random Forest, Logistic Regression, K-Means ($k=3$), Mann–Whitney U | Whitepaper PDF, Python CLI Pipeline, Notebook, Tests |
| **`time_series_forecasting_deliverable`** | Demand Forecasting | Daily demand series | SARIMA $(p,d,q)	imes(P,D,Q)_7$, ADF Test, Additive Decomposition | Jupyter Notebook, Forecast CSVs, Plots |
| **`dimensionality_reduction_clustering_task`** | Unsupervised Learning | Scikit-learn Iris dataset | PCA (2D/3D), K-Means (Elbow + Silhouette), DBSCAN, Agglomerative | Jupyter Notebook |
| **`analysis_preregistration_deliverable`** | Confirmatory Statistics | Scikit-learn Diabetes dataset | Multiple Linear Regression (OLS), Data-blind pipeline testing | Preregistration Markdown, Python Script, Pytest |
| **`advanced_statistical_analysis_task`** | Inferential Statistics | Scikit-learn Wine dataset | Welch's t-test, Mann–Whitney U, One-Way/Two-Way ANOVA, Tukey HSD, Levene | Jupyter Notebook |


---

## ⚙️ Environment Setup & Installation

To run any or all of the projects in this repository:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/amitsinghbhadouriya/Data-science-with-python-and-R-intern-tasks.git
   cd Data-science-with-python-and-R-intern-tasks
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows PowerShell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   # Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies for a specific module** by navigating to that project folder and using its respective `requirements.txt` (or install standard data science packages: `numpy`, `pandas`, `scipy`, `statsmodels`, `scikit-learn`, `matplotlib`, `seaborn`, `pytest`, `jupyter`).

---

## 👤 Author

* **Amit Singh Bhadouriya**

## 🧪 Verification & Testing

To run the unified test suite across all projects:
```bash
python scripts/run_all_tests.py
```

To validate all deliverables and output files:
```bash
python scripts/validate_deliverables.py
```
