import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np

df = pd.read_csv("table.csv")

df = df.drop(columns=["Name"])

scaler = StandardScaler()
scaled_df = scaler.fit_transform(df)

pca = PCA()
pca_result = pca.fit_transform(scaled_df)

pca_df = pd.DataFrame(
    pca_result,
    columns=[f"PC{i+1}" for i in range(pca_result.shape[1])]
)

loadings = pd.DataFrame(
    pca.components_.T,
    columns=[f"PC{i+1}" for i in range(pca.components_.shape[0])],
    index=df.columns
)

print(loadings)

pca = PCA(n_components=2)
pca_2d = pca.fit_transform(scaled_df)


k = 2
kmeans = KMeans(n_clusters=k, random_state=42)
labels = kmeans.fit_predict(pca_2d)


plt.scatter(pca_2d[:, 0], pca_2d[:, 1], c=labels, cmap='Set1', s=40, alpha=0.7)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            c='red', marker='X', s=200, label='Centroids')
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title(f"PCA + K-Means (k={k})")
plt.legend()
plt.show()

