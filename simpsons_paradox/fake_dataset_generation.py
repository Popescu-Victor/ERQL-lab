import numpy as np

def generate_inverse_correlation(
    mean_x: float, std_x: float,
    mean_y: float, std_y: float,
    size: int = 100,
    correlation: float = -0.8,
    seed: int = 42
) -> tuple[np.ndarray, np.ndarray]:
    """
    correlation should be between -1 and 0 for inverse correlation.
    -0.8 is a strong inverse, -0.3 is a weak one.
    """
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



import matplotlib.pyplot as plt


x, y = generate_inverse_correlation(
        mean_x=50, std_x=10,
        mean_y=50, std_y=10,
        size=100,
        correlation=-0.8
)



a, b = generate_inverse_correlation(
        mean_x=35, std_x=12,
        mean_y=35, std_y=12,
        size=100,
        correlation=-0.7
)

plt.scatter(x, y, alpha=0.5, color='steelblue', label='XY')
plt.scatter(a, b, alpha=0.5, color='coral', label='AB')
plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Correlation: {np.corrcoef(x, y)[0, 1]:.2f}")
plt.show()