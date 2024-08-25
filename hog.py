'''
Bir resimdeki yayaları saptama işlemi gerçekleştireceğiz.
HOG (Histogram of Oriented Gradients), görüntüden özellik çıkarmak için kullanılan özellik çıkarma yöntemidir.
HOGDescriptor, bir SVM - sınıflandırıcı yöntemidir.
'''

import cv2 as cv
import numpy as np

src = cv.imread("pedestrian.png")

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

rects, weights = hog.detectMultiScale(src,
                                      winStride=(4, 4),
                                      padding=(8, 8),
                                      scale=1.25)

for (x, y, w, h) in rects:
    cv.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("hog-detector", src)
cv.waitKey(1)
cv.destroyAllWindows()

