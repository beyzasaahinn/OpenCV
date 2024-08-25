# Geometrik dönüşüm, bir resimdekher bir pikselin mevcut x-y konumundan yeni bir x-y konumuna dönüşümüdür.

import cv2 as cv
import numpy as np

# shifting (kaydırma)

img = cv.imread('miuul.png')

rows = img.shape[0]
cols = img.shape[1]

M = np.float32([[1, 0, 300], [0, 1, 90]])   # çıktı matrisimiz

shifted = cv.warpAffine(img, M, (cols, rows))    # Yeni taşınacak olan konumun nerede olacağını belirlemek bir iştir. Bunu sağlayacak olan affine dönüşümüdür.

cv.imshow('original', img)
cv.waitKey(1)

cv.imshow('shifted', shifted)
cv.waitKey(1)



# rotation (döndürme)

M = cv.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)

dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow('rotation', dst)
cv.waitKey(1)


'''
scaling işlemi için eğer resmin boyutunu büyütmek istiyorsak fx için 0' dan büyük değerler,
eğer görüntünün boyutunu küçültmek istiyorsak 0'dan küçük değerler kullanmamız gerekmektedir. 
'''
res = cv.resize(img, None, fx=0.2, fy=0.2, interpolation=cv.INTER_CUBIC)
cv.imshow('img', res)
cv.waitKey(1)









