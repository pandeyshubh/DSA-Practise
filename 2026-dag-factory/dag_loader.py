"""
dag_loader.py
─────────────────────────────────────────────────────────────
Place this file in your $AIRFLOW_HOME/dags/ folder.

dagfactory automatically handles:
  - Dataset outlets on tasks
  - Dataset-based schedules on consumer DAGs
  - Cross-DAG wiring via matching URI strings

NO special dataset handling needed here.
The YAML drives everything.
"""

import os
from dagfactory import load_yaml_dags

load_yaml_dags(
    globals_dict=globals(),
    dags_folder=os.path.dirname(__file__),  # scans this folder recursively for .yml files
)
