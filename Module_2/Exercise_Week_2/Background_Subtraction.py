import numpy as np
import cv2

old_bg = 'Module_2/Exercise_Week_2/Background_Subtraction/GreenBackground.png'
old_bg = cv2.imread(old_bg)
old_bg = cv2.resize(old_bg, (700, 400))

object_img = cv2.imread('Module_2/Exercise_Week_2/Background_Subtraction/Object_Greenscreen.png', 1)
object_img = cv2.resize(object_img, (700, 400))

new_bg = cv2.imread('Module_2/Exercise_Week_2/Background_Subtraction/NewBackground.jpg', 1)
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