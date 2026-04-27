import numpy as np

def generate_inverse_correlation(
    mean_x: float, std_x: float,
    mean_y: float, std_y: float,
    size: int = 100,
    correlation: float = -0.8,
    seed: int = 42
) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed=seed)
    
    cov = correlation * std_x * std_y
    cov_matrix = [
        [std_x**2, cov],
        [cov,      std_y**2]
    ]
    
    means = [mean_x, mean_y]
    data = rng.multivariate_normal(mean=means, cov=cov_matrix, size=size)
    
    x = np.round(data[:, 0]).astype(int)
    y = np.round(data[:, 1]).astype(int)
    
    return x, y

std_dev = 10

import matplotlib.pyplot as plt


c, d = generate_inverse_correlation(
        mean_x=40, std_x=std_dev,
        mean_y=40, std_y=std_dev,
        size=100,
        correlation=-0.8
)



a, b = generate_inverse_correlation(
        mean_x=30, std_x=std_dev,
        mean_y=30, std_y=std_dev,
        size=100,
        correlation=-0.7
)


e, f = generate_inverse_correlation(
        mean_x=20, std_x=std_dev,
        mean_y=20, std_y=std_dev,
        size=100,
        correlation=-0.7
)

g, h = generate_inverse_correlation(
        mean_x=10, std_x=std_dev,
        mean_y=10, std_y=std_dev,
        size=100,
        correlation=-0.7
)



plt.scatter(a, b, alpha=0.5, color='grey')
plt.scatter(c, d, alpha=0.5, color='steelblue')
plt.scatter(e, f, alpha=0.5, color='coral')
plt.scatter(g, h, alpha=0.5, color='lightgreen')
plt.legend()
plt.show()