import cv2 as cv
import numpy as np

path = "Ekran Resmi 2024-08-06 12.14.58.png"

src = cv.imread(path)
print("Orijinal görüntü boyutları:", src.shape)

# görüntüyü gri tonlamaya çevir
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

cv.imshow("gray", gray)
cv.waitKey(1)

print("Gri tonlamalı görüntü boyutları:", gray.shape)
print(gray)

#standartlaştırma işlemlerinde işin kolaylaşması için integerdan floata çeviriyoruz.
gray = np.float32(gray)
print(gray)


# min ve max değerleri hesaplama
min_value, max_value, min_loc, max_loc = cv.minMaxLoc(gray)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))

# ortalama ve standart sapmayı hesapla
means, stddev = cv.meanStdDev(gray)
print("mean: %.2f, stddev: %.2f" % (means, stddev))

# normalizasyon işlemi için boş bir matris oluştur
dst = np.zeros(gray.shape, dtype=np.float32)

# görüntüyü normalize et
cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)
print(dst)

'''
çeşitli işlemler için arrayi ondalık yapmıştık. daha sonra tekrar integera çevireceğiz.
integera çevirdiğimizde küsuratlı olan değerler 0'a yuvarlanacaktır ve görüntü siyah gözükecektir. 
bu sebeple önce float olan array değerlerini 255 ile çarptıktan sonra integera dönüştüreceğiz. 
'''
# normalize edilmiş görüntüyü uint8 formatına çevir ve yazdır
print(np.uint8(dst * 255))

means, stddev = cv.meanStdDev(np.uint8(dst * 255))
print("mean: %.2f, stddev: %.2f" % (means, stddev))

cv.imshow("NORM_MINMAX", dst)
cv.waitKey(1)

# çıktıda resimler aynı gözükecektir. farkı gösterim şekilleri !!!



# BAŞKA BİR STANDARTLAŞTIRMA YÖNTEMİ

# minimum ve maksimum değerleri hesapla
min_value, max_value, min_loc, max_loc = cv.minMaxLoc(dst)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))

# ortalama ve standart sapmayı hesapla
means, stddev = cv.meanStdDev(dst)
print("mean: %.2f, stddev: %.2f" % (means, stddev))

# normalizasyon için bir boş matris oluştur
dst = np.zeros(gray.shape, dtype=np.float32)

# görüntüyü NORM_INF norm türü ile normalize et
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_INF)

# normalizasyon sonucunu yazdır
print("Normalize edilmiş değerler:\n", dst)

# normalize edilmiş görüntüyü uint8 formatına çevirerek göster
cv.imshow("NORM_INF", np.uint8(dst * 255))
cv.waitKey(1)



# BAŞKA BİR STANDARTLAŞTIRMA YÖNTEMİ

# normalizasyon için bir boş matris oluşturma
dst = np.zeros(gray.shape, dtype=np.float32)

# görüntüyü NORM_L1 norm türü ile normalize et
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_L1)

# normalizasyon sonucunu yazdırma
print("Normalize edilmiş değerler:\n", dst)

# normalize edilmiş görüntüyü uint8 formatına çevirerek gösterme
cv.imshow("NORM_L1", np.uint8(dst * 10000000))
cv.waitKey(1)



# BAŞKA BİR STANDARTLAŞTIRMA YÖNTEMİ

# normalizasyon için bir boş matris oluştur
dst = np.zeros(gray.shape, dtype=np.float32)

# görüntüyü NORM_L2 norm türü ile normalize et
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_L2)

# normalizasyon sonucunu yazdır
print("Normalize edilmiş değerler:\n", dst)

# normalize edilmiş görüntüyü uint8 formatına çevirerek göster
cv.imshow("NORM_L2", np.uint8(dst * 10000))
cv.waitKey(1)  # Pencerenin açık kalması için bekler
