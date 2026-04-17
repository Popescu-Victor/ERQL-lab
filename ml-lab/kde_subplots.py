import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# KDE without line showing median of data.
num_cols = df.select_dtypes(include='number').columns
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(16, 5))
axes = axes.flatten()

for i, col in enumerate(num_cols):
    sns.kdeplot(df[col], fill=True, ax=axes[i])
    axes[i].set_title(col)

plt.tight_layout()
plt.show()


# With median:

import math

num_cols = df.select_dtypes(include='number').columns
n = len(num_cols)
ncols = 3
nrows = math.ceil(n / ncols)

fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(4*ncols, 2*nrows))
axes = axes.flatten()

for i, col in enumerate(num_cols):
    sns.kdeplot(df[col], fill=True, ax=axes[i])
    axes[i].axvline(df[col].median(), color='red', linestyle='--', linewidth=1.5, label=f'Median: {df[col].median():.2f}')
    axes[i].set_title(col)
    axes[i].legend()

# Hide any unused subplots
for j in range(i+1, len(axes)):
    axes[j].set_visible(False)

plt.tight_layout()
plt.show()


# And with mode:

num_cols = df.select_dtypes(include='number').columns
n = len(num_cols)
ncols = 3
nrows = math.ceil(n / ncols)

fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(4*ncols, 2*nrows))
axes = axes.flatten()

for i, col in enumerate(num_cols):
    sns.kdeplot(df[col], fill=True, ax=axes[i])
    axes[i].axvline(df[col].median(), color='red', linestyle='--', linewidth=1.5, label=f'Median: {df[col].median():.2f}')
    axes[i].axvline(df[col].mode()[0], color='green', linestyle='--', linewidth=1.5, label=f'Mode: {df[col].mode()[0]:.2f}')
    axes[i].set_title(col)
    axes[i].legend()

# Hide any unused subplots
for j in range(i+1, len(axes)):
    axes[j].set_visible(False)

plt.tight_layout()
plt.show()


# Subplots with correlation to a single central column

import math

target_col = 'Success'
other_cols = [col for col in df.select_dtypes(include='number').columns if col != target_col]

n = len(other_cols)
ncols = 3
nrows = math.ceil(n / ncols)

fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(5*ncols, 4*nrows))
axes = axes.flatten()

for i, col in enumerate(other_cols):
    sns.regplot(x=col, y=target_col, data=df, ax=axes[i])
    axes[i].set_title(f'{col} vs {target_col}')

# Hide any unused subplots
for j in range(i+1, len(axes)):
    axes[j].set_visible(False)

plt.tight_layout()
plt.show()
