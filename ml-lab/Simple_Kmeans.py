from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('kmeanstest.csv')
df = df.iloc[:, 1:3]
print(df.head())

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(df)

df['cluster'] = kmeans.labels_

plt.scatter(df["Var1"], df["Var1"], c=df['cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            s=200, c='red', marker='*')

plt.show()
