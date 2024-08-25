# Kenarları koruyarak filtreleme işlemi gerçekleştireceğiz.

# FAST IMAGE EDGE FILTERING
# edgePreservingFilter

import cv2 as cv
import numpy as np

src = cv.imread("test.png")
cv.imshow("input", src)
cv.waitKey(1)

h, w = src.shape[:2]

# 'flags' parametresi, filtreleme metodunu belirtir (RECURS_FILTER burada kullanılır)
# sigma_s parametresi 0 ile 200 arasında değer alır, sigma_r ise 0 ile 1 arasında değer alır.
# sigma_s blurluğun şiddetini, sigma_r ise kenarların ne kadar dikkate alınıp alınmayacağını belirtiyor.
dst = cv.edgePreservingFilter(src, sigma_s=200, sigma_r=0.5, flags=cv.RECURS_FILTER)

result = np.zeros([h, w * 2, 3], dtype=src.dtype)
# iki kat genişlikte sıfırlarla dolu bir dizi oluşturulur (sol kaynak, sağ sonuç görüntü için)

result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = dst

cv.imshow("result", result)

cv.waitKey(0)
cv.destroyAllWindows()