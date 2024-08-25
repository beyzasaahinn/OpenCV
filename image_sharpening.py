'''
Görüntü keskinleştirme işlemi, daha keskin hatlara sahip görüntü elde etmeyi sağlar.
'''


import cv2 as cv
import numpy as np

src = cv.imread("Ekran Resmi 2024-08-06 12.14.58.png")

sharpen_op = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)   # görüntünün bir araya gelmesini istediğimiz iki boyutlu matris


sharpen_image = cv.filter2D(src, cv.CV_32F, sharpen_op)

sharpen_image = cv.convertScaleAbs(sharpen_image)   # ölçekleme, mutlak değer alma ve işaretsiz 8 bitlik bir türe dönüştürme işlemi gerçekleştiriyor.

cv.imshow("sharpen_image", sharpen_image)
cv.waitKey(1)
# daha keskin hatlara sahip bir görüntü elde edildi.

cv.destroyAllWindows()



