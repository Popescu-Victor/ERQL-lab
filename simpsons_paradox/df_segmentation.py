import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('simpsons_paradox/dataset.csv')

groups = {value: group for value, group in df.groupby(df.columns[-1])}

for value, group_df in groups.items():
    print(value, group_df.shape)

sns.regplot(x=df.iloc[:, 0], y=df.iloc[:, 1], scatter_kws={'alpha':0.5}, line_kws={'color':'red', 'linewidth':1.5})
plt.show()