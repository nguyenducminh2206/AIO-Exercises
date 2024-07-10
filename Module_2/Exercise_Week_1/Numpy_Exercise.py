import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Question 1
print("Question 1")

# Create 1D array from 0 to 9
arr = np.arange(0, 10, 1)
print(arr)
print()

# Question 2
print("Question 2")

# Create 3x3 matrix with all values as True
arr1 = np.full((3, 3), fill_value=True, dtype=bool)
print(arr1)
print()

arr2 = np.ones((3, 3)) > 0
print(arr2)
print()

arr3 = np.ones((3, 3), dtype=bool)
print(arr3)
print()

# Question 3
print("Question 3")

arr = np.arange(0, 10)
print(arr[arr % 2 == 1])
print()

# Question 4
print("Question 4")

arr = np.arange(0, 10)
arr[arr % 2 == 1] = -1
print(arr)
print()

# Question 5
print("Question 5")

arr = np.arange(10)
arr_2d = arr.reshape(2, -1)
print(arr_2d)
print()

# Question 6
print("Question 6")

arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=0)
print(c)
print()

# Question 7
print("Question 7")

arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=1)
print(c)
print()

# Question 8
print("Question 8")

arr = np.array([1, 2, 3])
print(np.repeat(arr, 3))
print(np.tile(arr, 3))
print()

# Question 9
print("Question 9")

print("[ 6  9 10]")
print()

# Question 10
print("Question 10")


def maxx(x, y):
    if x >= y:
        return x
    else:
        return y


a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(a, b))
print()

# Question 11
print("Question 11")

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

print(np.where(a < b, b, a))
print()


img = mpimg.imread('Module_2\Exercise_Week_1\dog.jpg')

img = img.astype(np.float32)

gray_img = np.zeros((img.shape[0], img.shape[1]))

# Question 12
print("Question 12")

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r, g, b = img[i, j][:3]
        gray_img[i, j] = (max(r, g, b) + min(r, g, b)) / 2

plt.imshow(gray_img, cmap='gray')
plt.show()

print(gray_img[0, 0])
print()

# Question 13
print("Question 13")

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r, g, b = img[i, j][:3]
        gray_img[i, j] = (r + g + b) / 3

plt.imshow(gray_img, cmap='gray')
plt.show()

print(f"{gray_img[0, 0]:.2f}")
print()

# Question 14
print("Question 14")

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r, g, b = img[i, j][:3]
        gray_img[i, j] = 0.21*r + 0.72*g + 0.07*b

plt.imshow(gray_img, cmap='gray')
plt.show()

print(f"{gray_img[0, 0]:.2f}")
print()


df = pd.read_csv('Module_2/Exercise_Week_1/advertising.csv')
data = df.to_numpy()

# Question 15
print("Question 15")

max_value = df['Sales'].max()
max_index = df['Sales'].idxmax()

print(f"Max: {max_value} - Index: {max_index}")
print()

# Question 16
print("Question 16")

average_tv = round(df['TV'].mean(), 2)

print(average_tv)
print()

# Question 17
print("Question 17")

count_sales = round((df['Sales'] >= 20).sum(), 2)

print(count_sales)
print()

# Question 18
print("Question 18")

filtered_df = df[df['Sales'] >= 15]

average_radio = round(filtered_df['Radio'].mean(), 2)

print(average_radio)
print()

# Question 19
print("Question 19")

average_news = df['Newspaper'].mean()
filter_news_df = df[df['Newspaper'] > average_news]
sum_news = filter_news_df['Sales'].sum()

print(sum_news)
print()

# Question 20
print("Question 20")

average_sales = df['Sales'].mean()
scores = ['Good' if sale > average_sales else 'Bad' if sale <
          average_sales else 'Average' for sale in df["Sales"]]

print(scores[7:10])
print()

# Question 21
print("Question 21")

closest_to_avg = df['Sales'].iloc[(
    df["Sales"] - average_sales).abs().argsort()[:1]].values[0]
scores = ["Good" if sale > closest_to_avg else "Bad" if sale <
          closest_to_avg else "Average" for sale in df["Sales"]]

print(scores[7:10])
