import pandas as pd
import sqlite3

df = pd.read_csv('simpsons_paradox/dataset.csv')

groups = {value: group for value, group in df.groupby(df.columns[-1])}

for value, group_df in groups.items():
    print(value, group_df.shape)