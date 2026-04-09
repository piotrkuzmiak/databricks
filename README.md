# Databricks Repository

This repository contains a small Python package for Databricks-related utilities together with example notebook content and tests.

## Repository Layout

- `databricks_utils/`: Python package project managed with `pyproject.toml`
- `databricks_utils/src/utilities/`: importable package source code
- `databricks_utils/src/utilities/udfs/functions.py`: reusable Spark UDFs, including `is_valid_email`
- `databricks_utils/notebooks/`: notebook examples, including `pandas_udf.ipynb`
- `databricks_utils/tests/`: test suite for the package

## Package Import

After installing the package, import UDF helpers with:

```python
from utilities.udfs.functions import is_valid_email
```

## Development Notes

- Package metadata lives in `databricks_utils/pyproject.toml`
- The package README used during builds is `databricks_utils/README.md`
- Source code follows the `src/` layout for packaging
