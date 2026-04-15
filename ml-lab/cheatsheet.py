import numpy as np
import pandas as pd
import scipy
from sklearn.model_selection import train_test_split
import modin
import tensorflow as tf

scipy.stats.binom.pmf(x, n, p) # x = value of interest, n = number of trials, p = possibility of success

scipy.stats.norm.cdf(x, loc, scale) # loc = mean of the probability distribution, scale = standard dev

scipy.stats.poisson.pmf (expected_value, probability)

sns.regplot(x=x, y=y, line_kws={"color":"red","linewidth":1, "linestyle":"--"}) # Scatterplot + trendline

sns.scatterplot(x, y, hue = , palette = ) # Scatterplot. 'Hue' can be a variable.

pd.merge(df1,df2, on="Name", how="SQL_join_type") # For example inner, outer, left, right

pd.concat(df1,df2)

pd.groupby()

# Adding jitter to scatterplot
jitter = 0.05
df["x_j"] = df["x"] + np.random.randn(len(df)) * jitter
df["y_j"] = df["y"] + np.random.randn(len(df)) * jitter
plt.scatter(df["x_j"], df["y_j"])
