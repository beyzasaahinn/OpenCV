# Bir bilgisayarın resimdeki nesnelerin kenarlarını algılaması demek renk geçişlerini algılaması demektir.
'''Sobel' in yapmış olduğu şey bir görüntüden türevler hesaplamak.
 x eksenine ve y eksenine göre türevler hesaplam yoluyla kenar algılama için bir yöntem yaratıyor.
'''

import cv2 as cv  # cv2 kütüphanesini 'cv' adıyla ithal eder
import numpy as np  # numpy kütüphanesini 'np' adıyla ithal eder

src = cv.imread("Ekran Resmi 2024-08-06 12.14.58.png")
h, w = src.shape[:2]

x_grad = cv.Sobel(src, cv.CV_32F, 1, 0)
# Görüntünün x eksenindeki kenarlarını tespit eder, 32-bit kayan nokta formatında çıktı verir
y_grad = cv.Sobel(src, cv.CV_32F, 0, 1)
# Görüntünün y eksenindeki kenarlarını tespit eder, 32-bit kayan nokta formatında çıktı verir
x_grad = cv.convertScaleAbs(x_grad)
# X ekseni gradyanını mutlak değerlere çevirir ve 8-bit formatında yeniden ölçekler
y_grad = cv.convertScaleAbs(y_grad)
# Y ekseni gradyanını mutlak değerlere çevirir ve 8-bit formatında yeniden ölçekler

cv.imshow("x_grad", x_grad)
cv.waitKey(1)
cv.imshow("y_grad", y_grad)
cv.waitKey(1)

dst = cv.add(x_grad, y_grad, dtype=cv.CV_16S)
dst = cv.convertScaleAbs(dst)
cv.imshow("gradient", dst)
cv.waitKey(0)

cv.destroyAllWindows()




