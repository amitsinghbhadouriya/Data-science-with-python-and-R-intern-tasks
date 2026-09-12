# Data

The real dataset is intentionally not stored here.

The analysis uses the scikit-learn `load_diabetes(as_frame=True)` dataset. The repository's analysis script obtains the dataset through the installed scikit-learn package.

For a strict preregistration workflow:
1. Timestamp/archive `preregistration.md`.
2. Do not inspect the real variables or outcome relationships before lock-in.
3. Run `pytest -q` first; this uses only synthetic data.
4. After lock-in, run `python analysis.py`.
