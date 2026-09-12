import numpy as np
import pandas as pd
from analysis import run_analysis

def synthetic_fixture(n=120, seed=20260912):
    rng = np.random.default_rng(seed)
    age = rng.normal(0, 1, n)
    sex = rng.normal(0, 1, n)
    bmi = rng.normal(0, 1, n)
    bp = rng.normal(0, 1, n)
    target = 0.45 * bmi + 0.20 * age - 0.10 * sex + rng.normal(0, 1, n)
    return pd.DataFrame({
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "bp": bp,
        "target": target,
    })

def test_pipeline_contract():
    result, model = run_analysis(synthetic_fixture())
    assert result["n"] == 120
    assert np.isfinite(result["primary_bmi_beta"])
    assert 0 <= result["primary_bmi_p"] <= 1
    assert len(result["primary_bmi_ci95"]) == 2
    assert "bmi_z" in result["vif"]
    assert np.isfinite(result["spearman_rho"])

def test_output_contract():
    result, model = run_analysis(synthetic_fixture(80, 7))
    required = {
        "n", "primary_bmi_beta", "primary_bmi_p",
        "primary_bmi_ci95", "robust_hc3_bmi_beta",
        "robust_hc3_bmi_p", "r_squared",
        "breusch_pagan_p", "max_abs_standardized_residual",
        "vif", "secondary_bp_adjusted_bmi_beta",
        "secondary_bp_adjusted_bmi_p", "spearman_rho", "spearman_p"
    }
    assert required.issubset(result)
