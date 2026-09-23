#!/usr/bin/env python3
"""
Unified Test Runner
Discovers and executes all unit tests across all internship task deliverables.
"""
import sys
import subprocess
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent

TEST_SUITES = [
    ("Capstone Tests", WORKSPACE / "data_science_capstone_whitepaper" / "tests"),
    ("Preregistration Tests", WORKSPACE / "analysis_preregistration_deliverable" / "tests"),
    ("Repository Sanity Tests", WORKSPACE / "tests"),
]

def main():
    print("=" * 60)
    print("Executing All Internship Task Test Suites")
    print("=" * 60)
    
    total_passed = 0
    total_suites = 0
    all_succeeded = True

    for name, test_dir in TEST_SUITES:
        if not test_dir.exists():
            continue
        total_suites += 1
        print(f"\n[RUNNING] {name} in {test_dir.relative_to(WORKSPACE)}...")
        res = subprocess.run([sys.executable, "-m", "pytest", str(test_dir), "-q"], cwd=str(WORKSPACE))
        if res.returncode == 0:
            print(f"[PASS] {name} completed successfully.")
            total_passed += 1
        else:
            print(f"[FAIL] {name} encountered failures (exit code: {res.returncode}).")
            all_succeeded = False

    print("\n" + "=" * 60)
    print(f"Summary: {total_passed}/{total_suites} test suites passed.")
    print("=" * 60)
    sys.exit(0 if all_succeeded else 1)

if __name__ == "__main__":
    main()
