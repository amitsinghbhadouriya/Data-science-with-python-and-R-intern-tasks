# Time-Series Forecasting with SARIMA

This deliverable implements the supplied Task 05 daily-demand forecasting problem.

## Contents
- `time_series_forecasting_SARIMA.ipynb` — complete notebook with outputs
- `daily-demand-series.csv` — supplied dataset
- `adf_stationarity_results.csv` — ADF results
- `sarima_model_selection_results.csv` — candidate model comparison
- `30_day_forecast.csv` — 30-day forecast
- `01_historical_demand.png` — historical series
- `02_decomposition.png` — trend/seasonal/residual decomposition
- `03_holdout_forecast.png` — validation forecast
- `04_30_day_forecast.png` — 30-day forecast projection
- `requirements.txt` — dependencies
- `implementation_note.md` — submission note

## Run
```bash
pip install -r requirements.txt
jupyter notebook time_series_forecasting_SARIMA.ipynb
```

The notebook uses a 7-day seasonal period because the input is daily demand with a weekly pattern.
