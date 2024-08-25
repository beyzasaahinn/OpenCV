# Resimde istediğimiz bölümü seçtikten sonra arkaplanını değiştirme işlemini gerçekleştireceğiz.

import cv2 as cv
import numpy as np

src = cv.imread("grabcut.png")
src = cv.resize(src, (0, 0), fx=0.5, fy=0.5)
r = cv.selectROI('input', src, False)

roi = src[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
img = src.copy()

cv.rectangle(img, (int(r[0]), int(r[1])), (int(r[0]) + int(r[2]), int(r[1]) + int(r[3])), (255, 0, 0), 2)

mask = np.zeros(src.shape[:2], dtype=np.uint8)
rect = (int(r[0]), int(r[1]), int(r[2]), int(r[3]))

bgdmodel = np.zeros((1, 65), np.float64)
fgdmodel = np.zeros((1, 65), np.float64)

cv.grabCut(src, mask, rect, bgdmodel, fgdmodel, 11, mode=cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype('uint8')

background = cv.imread("lab.png")

h, w, ch = src.shape
background = cv.resize(background, (w, h))
mask = np.zeros(src.shape[:2], dtype=np.uint8)
bgdmodel = np.zeros((1, 65), np.float64)
fgdmodel = np.zeros((1, 65), np.float64)

cv.grabCut(src, mask, rect, bgdmodel, fgdmodel, 5, mode=cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype('uint8')

se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
cv.dilate(mask2, se, mask2)

mask2 = cv.GaussianBlur(mask2, (5, 5), 0)

background = cv.GaussianBlur(background, (0, 0), 15)    # birleştirilen görüntünün organik gözükmesi için
mask2 = mask2 / 255.0
a = mask2[..., None]
result = a * (src.astype(np.float32)) + (1 - a) * (background.astype(np.float32))

cv.imshow("result", result.astype(np.uint8))
cv.waitKey(1)

cv.destroyAllWindows()