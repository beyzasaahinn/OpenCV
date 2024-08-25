# PERFORMANS ÖLÇME VE DEĞERLENDİRME TEKNİKLERİ

import cv2 as cv
import numpy as np

path = "Ekran Resmi 2024-08-06 12.14.58.png"
src = cv.imread(path, cv.IMREAD_GRAYSCALE)

# resmin min,max ve location erişimi
min_value, max_value, min_loc, max_loc = cv.minMaxLoc(src)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))
print("min loc:", min_loc, ",", "max loc:", max_loc)

# ortalama ve standart sapmayı hesapla
means, stddev = cv.meanStdDev(src)
print("mean: %.2f, stddev: %.2f" % (means, stddev))


# ortalamadan düşük olanlara 0 (siyah), ortalamadan yüksek olanlara 255 (beyaz) desek :
src[np.where(src < means)] = 0
src[np.where(src > means)] = 255

cv.imshow("binary", src)
cv.waitKey(0)
