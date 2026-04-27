import faker
import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=42)

print(rng.integers(0, 10, size=5))