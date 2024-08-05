import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Module_2/Exercise_Week_1/advertising.csv")

def correlation(x, y):
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

# Question 5
print("Question 5")

x = data['TV']
y = data['Radio']
print(f"Correlation between TV and Sales: {correlation(x, y)}")
print()

# Question 6
print("Question 6")

features = ['TV', 'Radio', 'Newspaper']

for feature_1 in features:
    for feature_2 in features:
        correlation_value = correlation(data[feature_1], data[feature_2])
        print(f"Correlation between {feature_1} and {feature_2} : {correlation_value:.2f}")

# Question 7
print("Question 7")

x = data['Radio']
y = data['Newspaper']

result = np.corrcoef(x, y)
print(result)
print()

# Question 8
print("Question 8")

print(data.corr())
print()

# Question 9
print("Question 9")

plt.figure(figsize=(10,8))
data_corr = data.corr()
sns.heatmap(data_corr, annot=True, fmt='.2f', linewidths=.5)
plt.show()
