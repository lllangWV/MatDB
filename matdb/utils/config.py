import os
import pandas as pd
from pathlib import Path
from variconfig import LoggingConfig

FILE = Path(__file__).resolve()
PKG_DIR = str(FILE.parents[1])
UTILS_DIR = str(FILE.parents[0])


config = LoggingConfig.from_yaml(os.path.join(UTILS_DIR, 'config.yml'))


pd.set_option('display.max_columns', config.pandas_config.display.max_columns)
pd.set_option('display.max_rows', config.pandas_config.display.max_rows)
pd.set_option('display.max_colwidth', config.pandas_config.display.max_colwidth)