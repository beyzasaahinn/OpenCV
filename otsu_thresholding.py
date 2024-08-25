'''
Otsu thresholding, otomatik görüntü eşikleme yapmak için kullanılan bir yöntemdir.
Giriş olarak verilen görüntüyü ikili görüntüye çevirmek için kullanılır.
İkili görüntü, görüntünün siyah veya beyaz olarak sınıflandırılmasıdır.
Burdaki amaç da genel olarak görüntüdeki gürültüleri azaltmak ve nesne tespiti gibi işlemlerdir.
Giriş olarak verilen görüntü üzerinde bu işlemler uygulandığında pikselleri verilen eşik değerine göre siyah veya beyaz olarak günceller.
Gri skalaya çevrilmiş görseller üzerinde uygulanır (önce görsel griye çevrilecek).
Çevrilen görselde gri tonlamalar ortadan kalkmıştır, görüntü yalnızca siyah ve beyaz renklerinden oluşmaktadır.
'''

import cv2 as cv
import numpy as np

src = cv.imread("lena.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(1)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

h, w = src.shape[:2]

cv.imshow("binary", binary)
cv.waitKey(1)

cv.destroyAllWindows()