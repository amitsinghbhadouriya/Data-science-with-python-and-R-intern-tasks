#!/usr/bin/env python3
"""
Deliverable Export Validator
Verifies the presence and non-zero size of all critical project deliverables.
"""
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent

CRITICAL_DELIVERABLES = [
    WORKSPACE / "data_science_capstone_whitepaper" / "report" / "Data_Science_Capstone_Whitepaper.pdf",
    WORKSPACE / "data_science_capstone_whitepaper" / "src" / "capstone_analysis.py",
    WORKSPACE / "data_science_capstone_whitepaper" / "notebooks" / "01_capstone_analysis.ipynb",
    WORKSPACE / "time_series_forecasting_deliverable" / "time_series_forecasting_SARIMA.ipynb",
    WORKSPACE / "time_series_forecasting_deliverable" / "30_day_forecast.csv",
    WORKSPACE / "time_series_forecasting_deliverable" / "adf_stationarity_results.csv",
    WORKSPACE / "dimensionality_reduction_clustering_task" / "Dimensionality_Reduction_Unsupervised_Clustering.ipynb",
    WORKSPACE / "analysis_preregistration_deliverable" / "preregistration.md",
    WORKSPACE / "analysis_preregistration_deliverable" / "analysis.py",
    WORKSPACE / "advanced_statistical_analysis_task" / "advanced_statistical_analysis_task" / "Advanced_Statistical_Analysis_Hypothesis_Testing.ipynb",
]

def main():
    print("=" * 60)
    print("Validating Critical Deliverable Artifacts")
    print("=" * 60)
    
    missing = []
    for item in CRITICAL_DELIVERABLES:
        if not item.exists():
            print(f"  [MISSING] {item.relative_to(WORKSPACE)}")
            missing.append(item)
        elif item.stat().st_size == 0:
            print(f"  [EMPTY]   {item.relative_to(WORKSPACE)}")
            missing.append(item)
        else:
            size_kb = item.stat().st_size / 1024
            print(f"  [EXISTS]  {item.relative_to(WORKSPACE)} ({size_kb:.1f} KB)")

    print("-" * 60)
    if not missing:
        print("All critical deliverables are present and valid.")
        sys.exit(0)
    else:
        print(f"ERROR: {len(missing)} deliverable(s) missing or empty.")
        sys.exit(1)

if __name__ == "__main__":
    main()
