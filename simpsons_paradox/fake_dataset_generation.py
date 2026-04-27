import numpy as np
import matplotlib.pyplot as plt


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

std_dev = 5
corr = -0.6


c, d = generate_inverse_correlation(
        mean_x=40, std_x=std_dev,
        mean_y=55, std_y=std_dev,
        size=100,
        correlation=corr
)

a, b = generate_inverse_correlation(
        mean_x=35, std_x=std_dev,
        mean_y=50, std_y=std_dev,
        size=100,
        correlation=corr
)

e, f = generate_inverse_correlation(
        mean_x=25, std_x=std_dev,
        mean_y=45, std_y=std_dev,
        size=100,
        correlation=corr
)

g, h = generate_inverse_correlation(
        mean_x=20, std_x=std_dev,
        mean_y=40, std_y=std_dev,
        size=100,
        correlation=corr

)


def third_col(col, data):
    df = []
    for i in range(len(col)):
        df.append(data)
    return df


print(np.column_stack([a, b, third_col(a, 1)]))

plt.scatter(a, b, alpha=0.5, color='steelblue')
plt.scatter(c, d, alpha=0.5, color='steelblue')
plt.scatter(e, f, alpha=0.5, color='steelblue')
plt.scatter(g, h, alpha=0.5, color='steelblue')
plt.legend()
plt.show()
