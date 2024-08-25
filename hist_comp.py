# Üç farklı resmin histogramlarını karşılaştırma işlemi yapacağız.

import cv2 as cv

src1 = cv.imread("miuul.png")
src2 = cv.imread("Ekran Resmi 2024-08-06 12.14.58.png")
src3 = cv.imread("lab.png")

# cvtColor
# rgb' den hsv' ye çevirmemizin sebebi hsv' nin daha kolay nesne takibi sağlaması, renkleri iyi ayırt edebilmesi
hsv1 = cv.cvtColor(src1, cv.COLOR_BGR2HSV)
hsv2 = cv.cvtColor(src2, cv.COLOR_BGR2HSV)
hsv3 = cv.cvtColor(src3, cv.COLOR_BGR2HSV)

# calcHist
hist1 = cv.calcHist([hsv1], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist2 = cv.calcHist([hsv2], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist3 = cv.calcHist([hsv3], [0, 1], None, [60, 64], [0, 180, 0, 256])

# normalize
cv.normalize(hist1, hist1, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist2, hist2, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist3, hist3, 0, 1.0, cv.NORM_MINMAX)

# compare_hist (q2 veya korelasyon gibi yöntemler kullanilabilmektedir.)
# HISTCMP_CORREL
cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
cv.compareHist(hist1, hist3, cv.HISTCMP_CORREL)
cv.compareHist(hist2, hist3, cv.HISTCMP_CORREL)

print(cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL))
print(cv.compareHist(hist1, hist3, cv.HISTCMP_CORREL))
print(cv.compareHist(hist2, hist3, cv.HISTCMP_CORREL))