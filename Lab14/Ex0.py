# Check if SciPy, statsmodels, and matplotlib are installed

import importlib

packages = ['scipy', 'statsmodels', 'matplotlib']

for pkg in packages:
    try:
        mod = importlib.import_module(pkg)
        print(f"{pkg}: installed (version {mod.__version__})")
    except ImportError:
        print(f"{pkg}: NOT installed")
