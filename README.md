# Databricks Repository

This repository contains a small Python package for Databricks-related utilities together with example notebook content and tests.

## Repository Layout

- `databricks_project/`: Python package project managed with `pyproject.toml`
- `databricks_project/databricks_sample_package/`: importable package source code
- `databricks_project/databricks_sample_package/udfs/functions.py`: reusable Spark UDFs, including `is_valid_email`
- `databricks_project/notebooks/`: notebook examples, including `pandas_udf.ipynb`
- `databricks_project/tests/`: test suite for the package

## Package Import

After installing the package, import UDF helpers with:

```python
from databricks_sample_package.udfs.functions import is_valid_email
```

## Development Notes

- Package metadata lives in `databricks_project/pyproject.toml`
- The package README used during builds is `databricks_project/README.md`