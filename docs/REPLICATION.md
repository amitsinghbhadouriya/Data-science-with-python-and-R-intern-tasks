# Replication & Reproducibility Guide

This guide provides explicit, end-to-end instructions for reproducing all results, tables, and visualization artifacts included in this repository.

## 1. Prerequisites
Ensure you have Python 3.9+ installed.

```bash
git clone https://github.com/amitsinghbhadouriya/Data-science-with-python-and-R-intern-tasks.git
cd Data-science-with-python-and-R-intern-tasks
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 2. Replicating Deliverables

### Task 1: Financial Fraud Risk Capstone
- **Dataset:** `data_science_capstone_whitepaper/data/capstone_demo_dataset.csv`
- **Command:**
  ```bash
  python data_science_capstone_whitepaper/src/capstone_analysis.py data_science_capstone_whitepaper/data/capstone_demo_dataset.csv
  ```
- **Outputs Produced:** Model metrics in `results/`, clustering tables, Mann-Whitney U test outputs.

### Task 2: SARIMA Demand Forecasting
- **Dataset:** `time_series_forecasting_deliverable/daily-demand-series.csv`
- **Command:** Launch and run all cells in `time_series_forecasting_deliverable/time_series_forecasting_SARIMA.ipynb`.
- **Outputs Produced:** Stationarity test CSV, model selection CSV, 30-day forecast CSV, and decomposition plots.

### Task 3: Dimensionality Reduction & Clustering
- **Dataset:** Scikit-learn Iris dataset (in-memory)
- **Command:** Run `dimensionality_reduction_clustering_task/Dimensionality_Reduction_Unsupervised_Clustering.ipynb`.
- **Outputs Produced:** PCA variance tables, 2D/3D projections, K-Means elbow plot, DBSCAN clusters.

### Task 4: Preregistered BMI Analysis
- **Command:**
  ```bash
  cd analysis_preregistration_deliverable
  pytest -q
  python analysis.py
  ```
- **Outputs Produced:** `outputs/results.json`, `outputs/results.csv`, `outputs/analysis_log.txt`.

### Task 5: Advanced Statistical Analysis
- **Command:** Run `advanced_statistical_analysis_task/advanced_statistical_analysis_task/Advanced_Statistical_Analysis_Hypothesis_Testing.ipynb`.
- **Outputs Produced:** Normality tests, Welch's t-test, Mann-Whitney U, One-Way and Two-Way ANOVA.
