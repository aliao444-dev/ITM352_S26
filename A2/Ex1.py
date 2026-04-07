# Read in a file from a URL and save a local CSV file with the first 10 rows of the data.

import pandas as pd
import numpy as np
import pyarrow
filename = "https://drive.google.com/file/d/1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA/view?usp=sharing"

pd.set_option('display.max_columns', None)

df = pd.read_csv(filename, engine="pyarrow")
out_file = "sales_data_test.csv"
df.head(10).to_csv(out_file, index=False)
