import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Generate sample data
np.random.seed(42)
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(1.5, 1, 1000)

# Create a shared x-axis
x = np.linspace(-4, 6, 500)

# Compute KDE for each dataset
kde1 = gaussian_kde(data1)
kde2 = gaussian_kde(data2)

y1 = kde1(x)
y2 = kde2(x)

# Compute the overlap (intersection) at each point
overlap = np.minimum(y1, y2)

fig, ax = plt.subplots(figsize=(10, 6))

# Fill under each density curve
ax.fill_between(x, y1, alpha=0.3, color='white', label='Distribution 1')
ax.fill_between(x, y2, alpha=0.3, color='white', label='Distribution 2')

# Highlight the overlapping region
ax.fill_between(x, overlap, alpha=0.8, color='steelblue', label='Overlap')

# Draw the KDE lines on top
ax.plot(x, y1, color='lightblue', linewidth=2)
ax.plot(x, y2, color='blue', linestyle="--" , linewidth=2)

ax.set_xlabel('Value')
ax.set_ylabel('Density')
ax.set_title('Density Plots with Intersection Highlighted')
ax.legend()
plt.tight_layout()
plt.show()
