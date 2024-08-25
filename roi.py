'''
ROİ (region of interest) - ilgilenilen alan
Özetle resim üzerinde bölgesel çalışmalar yaparken kullancak olduğumuz yapıdır.
Örneğin bir yüz resmi ile ilgilendiğimizde odağımız göz olacaksa o alana odaklanırız.
Bu bize zaman ve performans kazandırır.
'''

import cv2 as cv

src = cv.imread("miuul.png")
h, w = src.shape[:2]
img = src.copy()     #resim üzerinde işlem yaptığımızda orijinal haline ihtiyaç duyarsak diye kopyasını alıyoruz.
roi = img[300:750, 950:1300, :]  # resmin bir bölümünü seçiyoruz.

roi.shape[:2]
cv.imshow("roi", roi)
cv.waitKey(1)


img[0:450, 0:350, :] = roi

cv.imshow("img", img)
cv.waitKey(1)

# görütünün boyutları büyük gelirse küçültme işlemi uygulayabiliriz.
res = cv.resize(roi, None, fx=0.3, fy=0.3, interpolation=cv.INTER_CUBIC)
cv.imshow('res', res)
cv.waitKey(1)

# ilgilenilen görüntüyü resmin üzerine koymak istersek
img[0:135, 0:105, :] = res
cv.imshow("img", img)
cv.waitKey(1)

cv.destroyAllWindows()