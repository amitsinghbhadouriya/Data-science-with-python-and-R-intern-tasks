# Dataset Registry & Data Provenance

| Dataset Name | Task Module | Source / Package | Format | Sample Count | Attributes | Primary Target |
|---|---|---|---|---|---|---|
| **Financial Fraud Demo** | `data_science_capstone_whitepaper` | Synthetic banking transaction stream | CSV | 120 | 13 | `is_fraud` (binary) |
| **Daily Demand Series** | `time_series_forecasting_deliverable` | Daily logistics demand records | CSV | 30 | 2 | `demand` (continuous) |
| **Iris Flower Dataset** | `dimensionality_reduction_clustering_task` | `sklearn.datasets.load_iris` | In-memory | 150 | 4 | Morphological cluster |
| **Diabetes Progression** | `analysis_preregistration_deliverable` | `sklearn.datasets.load_diabetes` | In-memory | 442 | 10 | 1-year progression |
| **Wine Recognition** | `advanced_statistical_analysis_task` | `sklearn.datasets.load_wine` | In-memory | 178 | 13 | Cultivar class (1, 2, 3) |

## Data Governance & Ethics
- Demonstrations use synthetic or open academic benchmarks.
- No personal identifying information (PII) or confidential client data is stored or tracked.
