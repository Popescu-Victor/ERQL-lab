import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

num_cols = df.select_dtypes(include='number').columns
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(16, 5))
axes = axes.flatten()

for i, col in enumerate(num_cols):
    sns.kdeplot(df[col], fill=True, ax=axes[i])
    axes[i].set_title(col)

plt.tight_layout()
plt.show()
