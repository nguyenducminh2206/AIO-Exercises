import numpy as np
import math
import cv2

# Calculate vector length
def compute_vector_length(vector):
    return math.sqrt(sum(x**2 for x in vector))

# Calculate dot product
def dot_product(vector1, vector2):
    return np.dot(vector1, vector2)

# Calculate multiplication with matrix and vector
def matrix_multi_vector(vector, matrix):
    vector = np.array(vector)
    matrix = np.array(matrix)

    return np.dot(matrix, vector)

# Calculate multiplication with matrix and matrix
def matrix_multi_matrix(matrix1, matrix2):
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    if matrix1.shape[1] != matrix2.shape[0]:
        raise ValueError
    return np.dot(matrix1, matrix2)

# Calculate invese matrix
def inverse_matrix(matrix):
    matrix = np.array(matrix)

    if matrix.shape != (2, 2):
        raise ValueError
    
    det = matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

    if det == 0:
        raise ValueError
    
    inverse = (1 / det) * np.array([[matrix[1, 1], -matrix[0, 1]],
                                   [-matrix[1, 0], matrix[0, 0]]])

    return inverse

# Calculate eigenvector and eigenvalue
def compute_eigenvalue_eigenvector(matrix):
    matrix = np.array(matrix)

    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    eigenvectors = eigenvectors / np.linalg.norm(eigenvectors, axis=0)

    return eigenvalues, eigenvectors

# Calculate Cosine similarity
def compute_cosine(vector1, vector2):
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)

    product = np.dot(vector1, vector2)

    magnitude_v1 = np.linalg.norm(vector1)
    magnitude_v2 = np.linalg.norm(vector2)

    cosine_sim = product / (magnitude_v1 * magnitude_v2)

    return cosine_sim

# Question 1
print("Question 1")

vector = np.array([-2, 4, 9, 21])
result = compute_vector_length(vector)
print(result)
print()

# Question 2
print("Question 2")

v1 = np.array([0, 1, -1, 2])
v2 = np.array([2, 5, 1, 0])
result = dot_product(v1, v2)
print(result)
print()

# Question 3
print("Question 3")

x = np. array ([[1, 2] ,
                [3, 4]])
k = np. array ([1, 2])
print(x.dot(k))
print()

# Question 4
print("Question 4")

x = np.array([[-1 , 2],
              [3 , -4]])
k = np.array([1 , 2])
print(x@k)
print()

# Question 5
print("Question 5")

m = np.array([[-1, 1, 1], 
              [0, -4, 9]])
v = np.array([0, 2, 1])
result = matrix_multi_vector(v, m)
print(result)
print()

# Question 6
print("Question 6")

m1 = np.array([[0, 1 , 2], [2, -3 , 1]])
m2 = np.array([[1, -3], [6 , 1], [0, -1]])
result = matrix_multi_matrix(m1 ,m2)
print(result)
print()

# Question 7
print("Question 7")

m1 = np.eye(3)
m2 = np.array ([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
result = m1@m2
print(result)
print()

# Question 8
print("Question 8")

m1 = np.eye(2)
m1 = np.reshape(m1,(-1, 4))[0]
m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1@m2
print(result)
print()

# Question 9
print("Question 9")

m1 = np.array([[1, 2], [3, 4]])
m1 = np.reshape(m1, (-1, 4), "F")[0]
m2 = np.array([[1, 1, 1, 1],
               [2, 2, 2, 2],
               [3, 3, 3, 3],
               [4, 4, 4, 4]])
result = m1@m2
print(result)
print()

# Question 10
print("Question 10")

m1 = np.array([[-2, 6], [8, -4]])
result = inverse_matrix(m1)
print(result)
print()

# Question 11
print("Question 11")

matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = compute_eigenvalue_eigenvector(matrix)
print(eigenvectors)
print()

# Question 12
print("Question 12")

x = np.array([1, 2, 3, 4])
y = np.array([1, 0, 3, 0])
result = compute_cosine(x, y)
print(round(result, 3))
print()