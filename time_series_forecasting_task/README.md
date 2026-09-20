# Task 05 — Time-Series Forecasting with ARIMA / Prophet

## Deliverables
- `Time_Series_Forecasting_ARIMA_Prophet.ipynb`: Fully executed Jupyter Notebook with decomposition plots, diagnostics, model comparison, and 30-day forecast projections.
- `data/daily_demand.csv`: 365-day historical daily demand series with trend, weekly seasonality, marketing events, holidays, and holdout period.
- `data/daily_demand_30days.csv`: 30-day holdout dataset (June 2026).
- `requirements.txt`: Python package dependencies.

## What is Implemented
1. **Time-Series Decomposition**:
   - Classical and STL additive decomposition ($Y_t = T_t + S_t + R_t$).
   - Extraction of underlying trend, weekly cyclicality ($m = 7$), and noise diagnostics.
   - 4-panel decomposition visualization.

2. **Stationarity Diagnostics & Differencing**:
   - Augmented Dickey-Fuller (ADF) test evaluating unit-root presence.
   - First-order differencing ($\Delta y_t = y_t - y_{t-1}$) establishing stationarity ($p < 0.001$).
   - Autocorrelation (ACF) and Partial Autocorrelation (PACF) correlograms up to 28 lags.

3. **Model Training & Hyperparameter Tuning**:
   - AIC-driven grid search across SARIMA parameter space: $(p, d, q) \times (P, D, Q)_7$.
   - SARIMAX with exogenous regressors (`marketing_event`, `holiday`).
   - Facebook Prophet model configured with weekly seasonality, changepoint priors, and marketing/holiday regressors.
   - 4-panel residual diagnostics (standardized residuals, KDE vs. normal, Q-Q plot, correlogram).

4. **Holdout Evaluation**:
   - Chronological train-test split (335 training days vs. 30 holdout days).
   - Accuracy benchmarked across Baseline (Seasonal Naive), SARIMAX, and Facebook Prophet.
   - Metrics calculated: **RMSE**, **MAE**, and **MAPE (%)**.

5. **30-Day Future Forecast Projections**:
   - Full model retraining on complete 365-day history.
   - 30-day demand projection for July 2026 with 95% confidence intervals.
   - High-resolution projection chart with uncertainty bands.

## Run Instructions
```bash
pip install -r requirements.txt
jupyter notebook Time_Series_Forecasting_ARIMA_Prophet.ipynb
```
