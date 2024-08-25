# Hoffman kullanarak daire tespiti gerçekleştireceğiz.

import cv2 as cv
import numpy as np

src = cv.imread("coins.png")

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (9, 9), 2, 2)

circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, dp=1, minDist=10, param1=100, param2=50, minRadius=20, maxRadius=100)
'''
Metodun argümanlarına bakacak olursak :
dp : resmin çözünürlüğü (1 olursa girdi çözünürlüğüyle aynı çözünürlükte bir çıktı verecek)
minDist : saptanmış olan dairenin merkeziyle minimum uzaklığını ifade etmektedir. 
'''
if circles is not None:
    circles = np.uint16(np.around(circles))
    for c in circles[0, :]:
        print(c)
        cx, cy, r = c
        cv.circle(src, (cx, cy), 2, (0, 255, 0), 2, 8, 0)
        cv.circle(src, (cx, cy), r, (0, 0, 255), 2, 8, 0)

cv.imshow("hough line demo", src)
cv.waitKey(1)

cv.destroyAllWindows()
