import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu, sigma = 0, 1  # mean and standard deviation

x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot the full bell curve
ax.plot(x, y, 'b-', linewidth=2)

# --- Highlight a section (e.g., between x = -1 and x = 1) ---
x_fill_low, x_fill_high = -1, 1

x_fill = np.linspace(x_fill_low, x_fill_high, 500)
y_fill = norm.pdf(x_fill, mu, sigma)

ax.fill_between(x_fill, y_fill, alpha=0.4, color='red', label=f'Highlighted: [{x_fill_low}, {x_fill_high}]')

ax.set_title('Normal Distribution with Highlighted Section')
ax.set_xlabel('Value')
ax.set_ylabel('Probability Density')
ax.legend()
plt.tight_layout()
plt.show()
