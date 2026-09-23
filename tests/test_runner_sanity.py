"""
Sanity tests validating root project dependencies and core libraries.
"""
import importlib

def test_core_dependencies():
    packages = ["numpy", "pandas", "scipy", "sklearn", "statsmodels", "matplotlib"]
    for pkg in packages:
        mod = importlib.import_module(pkg)
        assert mod is not None, f"Failed to import {pkg}"

def test_directory_structure():
    from pathlib import Path
    root = Path(__file__).resolve().parent.parent
    expected_folders = [
        "data_science_capstone_whitepaper",
        "time_series_forecasting_deliverable",
        "dimensionality_reduction_clustering_task",
        "analysis_preregistration_deliverable",
        "advanced_statistical_analysis_task",
    ]
    for folder in expected_folders:
        assert (root / folder).exists(), f"Missing required folder: {folder}"
