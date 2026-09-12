# BMI and 1-Year Disease Progression — Preregistered Analysis

This repository contains a preregistered, reproducible analysis plan and a data-blind pipeline test.

## Research question
Among the observations in the scikit-learn diabetes regression dataset, is baseline body-mass index (BMI) associated with one-year quantitative disease progression after adjustment for age and sex?

The analysis is specified **before examining outcome relationships**.

## Deliverables
- `preregistration.md` — locked analysis plan
- `analysis.py` — analysis pipeline for the real dataset
- `tests/test_pipeline.py` — synthetic, data-blind pipeline check
- `environment.yml` — reproducible environment specification
- `requirements.txt` — pinned Python dependencies
- `data/README.md` — instructions for supplying the real dataset

## Data source
The intended dataset is the `diabetes` regression dataset distributed by scikit-learn. The analysis script loads it directly through scikit-learn, so the raw dataset is not copied into this repository.

## Data-blind rule
Do not run the real-data analysis or inspect outcome/predictor relationships until the preregistration is timestamped/archived. The included test uses synthetic data only.

## Run the synthetic pipeline test
```bash
pytest -q
```

## Run the preregistered analysis after lock-in
```bash
python analysis.py
```

The script writes:
- `outputs/results.json`
- `outputs/results.csv`
- `outputs/analysis_log.txt`

No exploratory model selection is performed.
