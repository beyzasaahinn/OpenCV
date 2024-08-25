import cv2 as cv
import numpy as np

path = "Ekran Resmi 2024-08-06 12.14.58.png"
img = cv.imread(path)

# Eğer görüntü yüklenemediyse, hata mesajı yazdırma
if img is None:
    print("Görüntü dosyası yüklenemedi. Lütfen dosya yolunu kontrol edin.")
else:
    # Görüntünün negatifini al
    img_negatif = 255 - img

    # Sonucu gösterme
    cv.imshow("Orijinal Görüntü", img)
    cv.imshow("Negatif Görüntü", img_negatif)
    cv.waitKey(1)
    cv.destroyAllWindows()
