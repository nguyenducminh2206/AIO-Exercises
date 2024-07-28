from math import sqrt, pi, exp
import numpy as np

data = [
    (1.4, 0), (1.0, 0), (1.3, 0), (1.9, 0), (2.0, 0), (1.8, 0),
    (3.0, 1), (3.8, 1), (4.1, 1), (3.9, 1), (4.2, 1), (3.4, 1)
]

data_class_0 = [length for length, cls in data if cls == 0]
data_class_1 = [length for length, cls in data if cls == 1]


def calculate_mean(data):
    return np.mean(data)


def calculate_variance(data):
    return np.var(data)


mean_0 = calculate_mean(data_class_0)
variance_0 = calculate_variance(data_class_0)
mean_1 = calculate_mean(data_class_1)
variance_1 = calculate_variance(data_class_1)

print(f"Class 0 - Mean: {mean_0:.3f}, Variance: {variance_0:.3f}")
print(f"Class 1 - Mean: {mean_1:.3f}, Variance: {variance_1:.3f}")

# Question 13
x = 3.4
prior_0 = len(data_class_0) / len(data)
prior_1 = len(data_class_1) / len(data)


def gaussian_probability(x, mean, variance):
    return (1 / sqrt(2 * pi * variance)) * exp(-((x - mean) ** 2) / (2 * variance))


likelihood_0 = gaussian_probability(x, mean_0, variance_0)
likelihood_1 = gaussian_probability(x, mean_1, variance_1)

posterior_0 = likelihood_0 * prior_0
posterior_1 = likelihood_1 * prior_1

print(f"P(0|X) = {posterior_0}")
print(f"P(1|X) = {posterior_1}")
