import numpy as np
import math

# Calculate vector length
def compute_vector_length(vector):
    return math.sqrt(sum(x**2 for x in vector))

# Calculate dot product
def dot_product(vector1, vector2):
    return np.dot(vector1, vector2)

# Calculate multiplication with matrix and vector
def matrix_multi_vector(vector, matrix):
    if len(vector) != len(matrix[0]):
        raise ValueError
    return np.dot(vector, matrix)

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