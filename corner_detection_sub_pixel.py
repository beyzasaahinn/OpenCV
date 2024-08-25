'''
Subpixel yöntemi, köşe konumlarını iyileştirir.
Farklı bir köşe saptama yöntemi kullanılıp sonrasında bu yöntem kullanıldığında daha hassas bir şekilde köşeler saptanabiliyor olacaktır.
Örneğin shi thomas yönteminin yaklayamadığı köşeleri yakalamaya çalışacağız.
goodFeaturesToTrack metodunu kullanarak yeni yöntemimiz olan cornerSubPix'i kullanarak daha detaylı bir yakalama işlemi gerçekleştirmeye çalışacağız.
cornerSubPix'in birinci parametresi üzerinde iş yapacağımız resim,
winSize parametresi arama penceresinin yan uzunluğunun yarısı anlamına geliyor,
zeroZone ifadesi, arama bölgesinin ortasındaki ölü bölgenin yarısı anlamına geliyor.
'''

import cv2 as cv
import numpy as np

src = cv.imread("blox.png")
def process(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    corners = cv.goodFeaturesToTrack(gray, 100, 0.05, 10)
    print(len(corners))
    for pt in corners:
        print(pt)
        b = np.random.random_integers(0, 256)
        g = np.random.random_integers(0, 256)
        r = np.random.random_integers(0, 256)
        x = np.int32(pt[0][0])
        y = np.int32(pt[0][1])
        cv.circle(image, (x, y), 5, (int(b), int(g), int(r)), 2)

    winSize = (3, 3)
    zeroZone = (-1, -1)
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_COUNT, 40, 0.001)
    corners = cv.cornerSubPix(gray, corners, winSize, zeroZone, criteria)

    for i in range(corners.shape[0]):
        print(" -- Refined Corner [", i, "] (", corners[i, 0, 0], ",", corners[i, 0, 1], ")")
    return image

result = process(src)
cv.imshow('result', result)
cv.waitKey(0)
cv.destroyAllWindows()