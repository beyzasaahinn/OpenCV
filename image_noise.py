import cv2 as cv
import numpy as np

# Görüntüyü okuma
src = cv.imread("Ekran Resmi 2024-08-06 12.14.58.png")

def add_salt_pepper_noise(image):
    h, w = image.shape[:2]
    nums = 10000
    rows = np.random.randint(0, h, nums, dtype=int)
    cols = np.random.randint(0, w, nums, dtype=int)
    for i in range(nums):
        if i % 2 == 1:
            image[rows[i], cols[i]] = (255, 255, 255)
        else:
            image[rows[i], cols[i]] = (0, 0, 0)
    return image

h, w = src.shape[:2]

# farkı daha iyi görebilmek adına iki görseli yan yana birleştirerek görüntüleyelim.
copy = np.copy(src)
copy = add_salt_pepper_noise(copy)

result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = copy

cv.imshow('Original and Noisy Image', result)

cv.imwrite('output.png', result)

cv.waitKey(0)
cv.destroyAllWindows()
