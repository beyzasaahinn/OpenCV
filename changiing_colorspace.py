# Renk uzayları belirli renkler çerçevesinde oluşturulan renk paletleridir. (rgb ve gri renk uzayları)
'''
HSV de kullanılan diğer renk uzaylarındandır (öz, doygunluk, değer)
Her bir renk bu üç elemanlı dizinin kombinasyonu şeklinde oluşturulur.
Bu renk uzayı sayesinde renklerin özü ve doygunluğu olduğundan dolayı nesnelerin takibi kolaylaşır.
'''

import cv2 as cv

img = cv.imread("Ekran Resmi 2024-08-06 12.14.58.png")
cv.namedWindow("rgb", cv.WINDOW_AUTOSIZE)
cv.imshow("rgb", img)
cv.waitKey(1)

# RGB to GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)
cv.waitKey(1)

cv.destroyAllWindows()
