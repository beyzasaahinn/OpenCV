import cv2 as cv
import numpy as np
import numpy as pd
path = "Ekran Resmi 2024-08-06 12.14.58.png"

img = cv.imread(path)
cv.namedWindow("image_create", cv.WINDOW_AUTOSIZE)
cv.imshow("image_create", img)
cv.waitKey(1)

#üzerinde farklı işlemler yapacağız.
m1 = np.copy(img)   #kopyasını alıyoruz.
m2 = img

print(type(img))

#resmin belirli bir bölümüne gitmek için
img[100:200, 200:300, : ]
print(img[100:200, 200:300, : ])

#resmin seçtiğimiz kısmı beyaz olacak.
img[100:200, 200:300, : ] = 255
print(img[100:200, 200:300, : ])
cv.imshow("m2", m2)
cv.waitKey(1)

#resmin seçtiğimiz kısmı siyah olacak.
img[100:200, 200:300, : ] = 0
print(img[100:200, 200:300, : ])
cv.imshow("m2", m2)
cv.waitKey(1)

#resimle aynı boyutta 0'lar oluşturalım (resmin boyutunda siyah ekran oluşacak)
m3 = np.zeros(img.shape,img.dtype)
cv.imshow("m3", m3)
cv.waitKey(1)

#farklı boyutlarda siyah görsel oluşturmak istersek
m4 = np.zeros([512, 512], np.uint8)
cv.imshow("m4", m4)
cv.waitKey(1)

#gri bir görsel oluşturmak istersek
m5 = np.zeros([512, 512], np.uint8)
m5[:,:] = 127
cv.imshow("m5", m5)
cv.waitKey(1)

#daha özel şekiller de çizilebilir / şeklin üzerine yazı yazılabilir.
img = np.ones((550, 770, 3))

# Renk tanımlamaları
black = (0, 0, 0)  # Siyah renk (BGR formatında)
red = (0, 0, 255)  # Kırmızı renk (BGR formatında)
green = (0, 255, 0)  # Yeşil renk (BGR formatında)

# Dikdörtgen çizimleri
cv.rectangle(img, (480, 250), (100, 450), black, 8)
cv.rectangle(img, (580, 150), (200, 350), black, 8)

# Çizgi çizimleri
cv.line(img, (100, 450), (200, 350), black, 8)
cv.line(img, (480, 250), (580, 150), black, 8)
cv.line(img, (100, 250), (200, 150), black, 8)
cv.line(img, (480, 450), (580, 350), black, 8)

# Başlangıç noktası ve font ayarları
start_point = (150, 100)  # Metnin başlayacağı yer
font_thickness = 2        # Font kalınlığı
font_size = 1             # Font büyüklüğü
font = cv.FONT_HERSHEY_DUPLEX  # Kullanılacak font türü

# Metni görüntüye ekleme
cv.putText(img, 'www.harikaresimcizerim.com', start_point, font, font_size, (0, 0, 0), font_thickness)

# Görüntüyü gösterme
cv.imshow('dikdortgen', img)
cv.waitKey(1)
