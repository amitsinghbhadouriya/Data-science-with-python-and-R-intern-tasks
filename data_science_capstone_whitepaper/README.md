# Data Science Research Capstone & Whitepaper

## Financial Transaction Fraud Risk & Pattern Analysis

**Author:** Amit Singh Bhadouriya  
**Date:** September 2026  
**Project type:** Data Science Research Capstone

### Research question
Can transaction amount, failed-attempt behavior, historical activity, account age, and transaction time provide useful predictive signals for identifying potentially fraudulent transactions?

### Deliverables
- `report/Data_Science_Capstone_Whitepaper.pdf` — formal research report
- `src/capstone_analysis.py` — reproducible analysis pipeline
- `notebooks/01_capstone_analysis.ipynb` — notebook workflow
- `data/capstone_demo_dataset.csv` — reproducible demonstration dataset
- `results/` — model, statistical and clustering outputs
- `figures/` — research figures

### Important dataset note
The original `fraud_test_dataset.csv` was available in the project File Library, but its full binary/CSV contents were not mounted into the execution sandbox used to generate this package. Therefore, the included CSV is a **reproducible demonstration dataset mirroring the uploaded dataset's schema and fraud-pattern structure**; it is not presented as the original source data.

For final submission, place your original `fraud_test_dataset.csv` in `data/` and run:

```bash
python src/capstone_analysis.py data/fraud_test_dataset.csv
```

Then regenerate/update the report if your mentor requires metrics from the exact original file.

### Methods
1. Data validation and timestamp feature extraction
2. Exploratory/descriptive analysis
3. Mann–Whitney U statistical testing
4. Logistic Regression baseline
5. Random Forest predictive model
6. K-Means behavioral clustering
7. Permutation-based feature importance
8. Limitations and business implications

### Reproducibility
Random seed: `42`  
Test split: 25%, stratified  
Primary metrics: precision, recall, F1 and ROC-AUC  
Clustering: K-Means, k=3, silhouette score

### Suggested GitHub commit
`feat: add data science capstone research report and predictive modeling pipeline`
