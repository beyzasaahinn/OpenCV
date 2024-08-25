'''
Şablon eşleştirme demektir.
Daha çok bir kaynak görüntü üzerinde bir şablonu aramak için kullanılan bir yöntemdir.
Yani kısacası büyük bir görüntü üzerinde bir şablon görüntüsünün konumunu arıyor olacağız ve bu konumu belirlemeye çalışacağız.
Aradığımız şablonu sliding window (kayan pencere) yöntemiyle bulmaya çalışacağız.
'''

import cv2 as cv
import numpy as np

def template_demo():
    src = cv.imread("Ekran Resmi 2024-08-06 12.14.58.png")
    tpl = cv.imread("sablon.png")

    cv.imshow("input", src)
    cv.imshow("tpl", tpl)

    th, tw = tpl.shape[:2]

    result = cv.matchTemplate(src, tpl, method=cv.TM_CCORR_NORMED)
    cv.imshow("result", result)

    t = 0.98    # kendimiz belirlediğimiz threshold similarity oranı
    loc = np.where(result > t)

    for pt in zip(*loc[::-1]):
        cv.rectangle(src, pt, (pt[0] + tw, pt[1] + th), (255, 0, 0), 1, 8, 0)

    cv.imshow("ilk_demo", src)

template_demo()
cv.waitKey(0)