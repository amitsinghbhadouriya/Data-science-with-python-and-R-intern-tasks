# Implementation Note

Completed Task 05: **Time-Series Forecasting with SARIMA**.

- Loaded and cleaned the supplied daily demand series.
- Analyzed historical trend and weekly seasonality using time-series decomposition.
- Performed Augmented Dickey-Fuller tests on the original and differenced series.
- Used a chronological 7-day holdout for validation.
- Compared SARIMA hyperparameters using holdout RMSE and MAPE.
- Selected SARIMA `(1, 1, 2) x (1, 0, 1, 7)` from the tested candidates.
- Holdout RMSE: **0.50**
- Holdout MAPE: **0.25%**
- Refit the selected model on all 30 observations.
- Generated the required 30-day forecast and 95% forecast interval.

The notebook contains the full code, tables, plots, model selection results, evaluation, and forecast projection.
