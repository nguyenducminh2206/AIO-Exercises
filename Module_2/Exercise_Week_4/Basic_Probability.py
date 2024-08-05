import numpy as np

# Question 1
print("Question 1")

def compute_mean(x):
    return np.mean(x)

x = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
print(compute_mean(x))
print()

# Question 2
print("Question 2")

def compute_median(x):
    return np.median(x)

x = [1, 5, 4, 4, 9, 13]
print(compute_median(x))
print()

# Question 3
print("Question 3")

def compute_std(x):
    mean = compute_mean(x)
    total = 0

    for i in range(len(x)):
        total += (x[i] - mean) ** 2
    variance = total / len(x)

    return round(np.sqrt(variance), 2)

x = [171, 176, 155, 167, 169, 182]
print(compute_std(x))
print()

# Question 4
print("Question 4")

def compute_correlation_cofficient(x, y):
    n = len(x)
    sum_xy = 0
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_sqr = np.sum(x ** 2)
    sum_y_sqr = np.sum(y ** 2)

    for x, y in zip(x, y):
        sum_xy += x * y
    
    numerator = n * sum_xy - sum_x * sum_y
    denominator = np.sqrt(n * sum_x_sqr - (sum_x ** 2)) * np.sqrt(n * sum_y_sqr - (sum_y ** 2))

    correlation_cofficient = numerator / denominator

    return round(correlation_cofficient, 2)

x = np.asarray([-2, -5, -11, 6, 4, 15, 9])
y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print(compute_correlation_cofficient(x, y))
print()

