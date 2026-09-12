from pathlib import Path
import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import spearmanr
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.datasets import load_diabetes

OUT = Path("outputs")
OUT.mkdir(exist_ok=True)

def zscore(s):
    return (s - s.mean()) / s.std(ddof=1)

def run_analysis(df):
    # Expected scikit-learn frame columns include age, sex, bmi, bp and target.
    d = df[["age", "sex", "bmi", "bp", "target"]].dropna().copy()
    d = d.rename(columns={"target": "disease_progression"})

    for col in ["age", "sex", "bmi", "bp", "disease_progression"]:
        d[col + "_z"] = zscore(d[col])

    X = sm.add_constant(d[["bmi_z", "age_z", "sex_z"]])
    y = d["disease_progression_z"]

    model = sm.OLS(y, X).fit()
    robust = model.get_robustcov_results(cov_type="HC3")

    bp_test = het_breuschpagan(model.resid, model.model.exog)

    vif = {
        name: float(variance_inflation_factor(X.values, i))
        for i, name in enumerate(X.columns)
        if name != "const"
    }

    secondary = sm.OLS(
        y, sm.add_constant(d[["bmi_z", "age_z", "sex_z", "bp_z"]])
    ).fit()

    rho, rho_p = spearmanr(d["bmi"], d["disease_progression"])

    result = {
        "n": int(len(d)),
        "primary_bmi_beta": float(model.params["bmi_z"]),
        "primary_bmi_p": float(model.pvalues["bmi_z"]),
        "primary_bmi_ci95": [float(x) for x in model.conf_int().loc["bmi_z"]],
        "robust_hc3_bmi_beta": float(robust.params[1]),
        "robust_hc3_bmi_p": float(robust.pvalues[1]),
        "r_squared": float(model.rsquared),
        "breusch_pagan_p": float(bp_test[1]),
        "max_abs_standardized_residual": float(np.max(np.abs(model.get_influence().resid_studentized_internal))),
        "vif": vif,
        "secondary_bp_adjusted_bmi_beta": float(secondary.params["bmi_z"]),
        "secondary_bp_adjusted_bmi_p": float(secondary.pvalues["bmi_z"]),
        "spearman_rho": float(rho),
        "spearman_p": float(rho_p),
    }

    return result, model

def main():
    data = load_diabetes(as_frame=True)
    df = data.frame
    result, model = run_analysis(df)

    with open(OUT / "results.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    pd.DataFrame([result]).to_csv(OUT / "results.csv", index=False)

    with open(OUT / "analysis_log.txt", "w", encoding="utf-8") as f:
        f.write("Preregistered analysis executed.\n")
        f.write("Primary model: standardized disease progression ~ standardized BMI + standardized age + standardized sex\n")
        f.write(f"N={result['n']}\n")
        f.write(f"Primary BMI beta={result['primary_bmi_beta']:.6f}\n")
        f.write(f"Primary BMI p={result['primary_bmi_p']:.6g}\n")

if __name__ == "__main__":
    main()
