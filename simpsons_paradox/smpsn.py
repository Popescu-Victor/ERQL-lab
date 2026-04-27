import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('simpsons_paradox/dataset.csv')
print(df.head())

x = df.iloc[:, 0].values
y = df.iloc[:, 1].values

m, b = np.polyfit(x, y, 1)
trendline = np.poly1d([m, b])

x_sorted = np.sort(x)
plt.scatter(x, y, alpha=0.3)
plt.plot(x_sorted, trendline(x_sorted), color='red', linewidth=2, linestyle='--')
plt.show()