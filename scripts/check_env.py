#!/usr/bin/env python3
"""
Environment Verification Utility
Validates that required libraries and runtime versions are properly configured.
"""
import sys
import platform

REQUIRED_LIBRARIES = {
    "numpy": "1.20.0",
    "pandas": "1.3.0",
    "scipy": "1.7.0",
    "sklearn": "1.0.0",
    "statsmodels": "0.13.0",
    "matplotlib": "3.4.0",
    "pytest": "7.0.0",
}

def main():
    print("=" * 60)
    print("Environment Diagnostic Check")
    print("=" * 60)
    print(f"Python Platform : {platform.platform()}")
    print(f"Python Version  : {platform.python_version()}")
    print(f"Executable      : {sys.executable}")
    print("-" * 60)

    all_ok = True
    for lib, min_ver in REQUIRED_LIBRARIES.items():
        try:
            mod = __import__(lib)
            installed_ver = getattr(mod, "__version__", "unknown")
            print(f"  [OK] {lib:<15} : installed {installed_ver}")
        except ImportError:
            print(f"  [MISSING] {lib:<11} : required >= {min_ver}")
            all_ok = False

    print("=" * 60)
    if all_ok:
        print("All dependencies satisfied.")
    else:
        print("Some dependencies are missing. Run: pip install -r requirements.txt")
    print("=" * 60)
    sys.exit(0 if all_ok else 1)

if __name__ == "__main__":
    main()
