# Bir görüntüyü döndürme işlemi gerçekleştireceğiz.

import cv2 as cv
import numpy as np

path = "Ekran Resmi 2024-08-06 12.14.58.png"
src = cv.imread(path)

# X Flip
dst1 = cv.flip(src, 0)
cv.imshow("x-flip", dst1)
cv.waitKey(1)

# Y Flip
dst2 = cv.flip(src, 1)
cv.imshow("y-flip", dst2)
cv.waitKey(1)

# XY Flip
dst3 = cv.flip(src, -1)
cv.imshow("xy-flip", dst3)
cv.waitKey(1)
