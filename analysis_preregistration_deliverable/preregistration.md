# Analysis Preregistration

**Status:** Locked plan  
**Version:** 1.0  
**Preregistration timestamp:** 2026-09-12  
**Analysis lock rule:** The statistical decisions below must not be changed after inspecting the real outcome relationships. Any later change must be recorded in `deviations.md` with a timestamp and reason.

## Research question

Among observations in the scikit-learn diabetes regression dataset, is baseline body-mass index (BMI) associated with one-year quantitative disease progression after adjustment for age and sex?

This is falsifiable because the primary coefficient for standardized BMI will be tested against zero.

## Hypotheses

### Null hypothesis
H0: After adjustment for age and sex, the population association between baseline BMI and one-year quantitative disease progression is zero.

### Alternative hypothesis
H1: After adjustment for age and sex, the population association between baseline BMI and one-year quantitative disease progression is non-zero.

A two-sided alternative is specified because no directional assumption is imposed by this preregistration.

## Population, sample, and exclusions

### Target population
The target population is represented by the observations available in the scikit-learn diabetes regression dataset.

### Unit of analysis
One observation corresponding to one study participant.

### Inclusion rules
1. Include observations present in the official scikit-learn diabetes regression dataset.
2. Require non-missing values for disease progression, BMI, age, and sex.
3. Retain the dataset's supplied numerical coding without outcome-based filtering.

### Exclusion rules
1. Exclude observations with missing values in the primary outcome, BMI, age, or sex.
2. Do not exclude observations because of unusually high/low predictor or outcome values.
3. Do not remove observations based on residuals, leverage, Cook's distance, or statistical significance in the primary analysis.

### Stopping rule
No sequential data collection or optional stopping is planned. The analysis uses the complete eligible dataset supplied by scikit-learn.

## Variables and measures

### Primary outcome
`disease_progression`: the quantitative disease-progression target supplied by the dataset.

### Primary predictor
`BMI`: baseline body-mass-index measure.

### Controls
- `age`
- `sex`

Age and sex are included a priori as adjustment variables.

### Transformations
1. Standardize BMI, age, and sex using z-scores calculated within the analysis sample.
2. Do not transform the outcome.
3. Do not test alternative transformations and select the one with the strongest association.
4. Keep the same preprocessing rule for the primary model and all prespecified sensitivity analyses.

### Missing-data handling
Complete-case analysis will be used for the primary model. The number of excluded observations due to missingness will be reported. No outcome imputation is planned.

## Analysis plan

### Primary model
Fit an ordinary least-squares linear regression:

`standardized disease_progression ~ standardized BMI + standardized age + standardized sex`

The primary estimand is the regression coefficient for standardized BMI.

### Statistical test
Use a two-sided t-test for the BMI coefficient.

### Alpha
Set alpha = 0.05.

### Effect size
Report:
- standardized BMI regression coefficient (beta)
- 95% confidence interval
- p-value
- model R-squared
- sample size

### Uncertainty intervals
Use conventional model-based 95% confidence intervals for regression coefficients.

### Assumption checks
Report:
1. Residual-vs-fitted pattern.
2. Q-Q plot of residuals.
3. Heteroskedasticity test using Breusch-Pagan.
4. Maximum absolute standardized residual.
5. Variance inflation factors for predictors.

These checks are descriptive/diagnostic and do not authorize changing the primary model after seeing results.

### Robustness checks
The following are prespecified:
1. Heteroskedasticity-robust (HC3) standard errors for the same linear model.
2. A secondary model adding baseline blood-pressure (`bp`) as an additional covariate, if the variable is available in the dataset.
3. A sensitivity analysis using Spearman correlation between BMI and disease progression, reported as a secondary nonparametric association.

The primary conclusion remains based on the preregistered OLS model.

### Multiple testing
Only the BMI coefficient in the primary model is the confirmatory hypothesis test. Secondary robustness analyses are not treated as additional confirmatory hypotheses and will be clearly labeled exploratory/robustness results.

### Reporting
Report all prespecified analyses, including null results and diagnostics. Do not selectively report only statistically significant results.

## Deviations

Any deviation from this plan after lock-in must be recorded with:
- timestamp
- exact change
- reason
- whether the deviation occurred before or after viewing real outcome relationships
- likely impact on interpretation

No deviations are currently recorded.
