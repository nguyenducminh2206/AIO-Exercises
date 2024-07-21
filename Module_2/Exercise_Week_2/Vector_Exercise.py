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

# Background subtraction
old_bg = 'Module_2/Exercise_Week_2/GreenBackground.png'
old_bg = cv2.imread(old_bg)
old_bg = cv2.resize(old_bg, (700, 400))

object_img = cv2.imread('Module_2/Exercise_Week_2/Object_Greenscreen.png', 1)
object_img = cv2.resize(object_img, (700, 400))

new_bg = cv2.imread('Module_2/Exercise_Week_2/NewBackground.jpg', 1)
new_bg = cv2.resize(new_bg, (700, 400))

method = 'Image Window'


def compute_difference(bg_img, input_img):
    diff = cv2.absdiff(bg_img, input_img)
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    return gray_diff

# Usage for compute_difference function
mask_obj = compute_difference(old_bg, object_img)
cv2.imshow(method, mask_obj)
cv2.waitKey(0)


def compute_binary_mask(diff_single_channel):
    _, binary_mask = cv2.threshold(diff_single_channel, 50, 255, cv2.THRESH_BINARY)

    return binary_mask

# Usage for cimpute_binary_mask function
binary_mask = compute_binary_mask(mask_obj)
cv2.imshow(method, binary_mask)
cv2.waitKey(0)


def replace_background(old_bg, obj_img, new_bg):
     # Compute the difference between the original background and the object image
    difference_channel = compute_difference(old_bg, obj_img)

    # Compute the binary mask from the difference
    binary_img = compute_binary_mask(difference_channel)
    
    # Ensure binary mask is 3-channel for combining with color images
    binary_img_3channels = cv2.cvtColor(binary_img, cv2.COLOR_GRAY2BGR)

    # Replace the background
    # Where the binary mask is 255 (white), take pixels from ob_image
    # Where the binary mask is 0 (black), take pixels from bg2_image
    new_img = np.where(binary_img_3channels==255, obj_img, new_bg)

    return new_img

img_new_bg = replace_background(old_bg, object_img, new_bg)
cv2.imshow(method, img_new_bg)
cv2.waitKey(0)