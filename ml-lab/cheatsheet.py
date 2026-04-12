import numpy as np
import pandas as pd
import scipy
from sklearn.model_selection import train_test_split
import modin
import tensorflow as tf

scipy.stats.binom.pmf(x, n, p) # x = value of interest, n = number of trials, p = possibility of success

scipy.stats.norm.cdf(x, loc, scale) # loc = mean of the probability distribution, scale = standard dev

scipy.stats.poisson.pmf (expected_value, probability)