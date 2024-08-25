'''
Resmin kenarlarını koruyarak görüntüyü yumuşatma (blurlama işlemi)
Görüntüyü yumuşatmak demek gürültüyü azaltmak demektir.
Gürültüyü azaltmak demek resimde gereksiz kabul edileblecek detayları kaldırmak demektir.
'''

import cv2 as cv
import numpy as np

src = cv.imread("test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(1)

h, w = src.shape[:2]

# Metodun üçüncü argümanı ne kadar büyük olursa o kadar birbirine uzak renkler birbirine karışır.
# Metodun dördüncü argümanı ne kadar büyük olursa o kadar fazla piksel birbirine karışır.
dst = cv.bilateralFilter(src, 0, 50, 20)

result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = dst

cv.imshow("result", result)
cv.waitKey(0)

cv.destroyAllWindows()