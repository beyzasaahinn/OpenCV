# Canny, kenar saptamada kullanılan en yaygın kullanılan yöntemlerdendir. Bu işlemi piksellerin renk farklılaşmasından yararlanarak yapıyordu.
# CANNY EDGE DETECTION

import cv2 as cv
import numpy as np

src = cv.imread("keanu.png")
cv.imshow("keanu", src)
cv.waitKey(1)

edge = cv.Canny(src, 100, 300)
cv.imshow("mask image", edge)
cv.waitKey(0)
# İki argümanı bulunmaktadır (threshold1 ve threshold2). Bu değerlerin daha büyük olması kuvvetli kenarların bulunmmasını sağlayacaktır.

cv.destroyAllWindows()