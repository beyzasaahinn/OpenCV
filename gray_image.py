import cv2 as cv

# Görüntü yolunu kontrol edin
path = "Ekran Resmi 2024-08-06 12.14.58.png"

# Görüntüyü yükle
img = cv.imread(path)

# Görüntünün yüklenip yüklenmediğini kontrol et
if img is not None:
    print(f"Görüntü başarıyla yüklendi. Boyutlar: {img.shape}")

    # Görüntüyü gri tonlamaya çevir
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow("Original Image", img)
    cv.imshow("Grayscale Image", gray)
    cv.waitKey(1)
    cv.destroyAllWindows()

