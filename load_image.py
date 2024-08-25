import cv2 as cv

path = "miuul.png"
img = cv.imread(path)
print(type(img))

#namedWindow metodu, resimleri tutmak için pencere oluşturur.
cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)   #window_autosize resmin orijinal kendi boyutlarıyla tutulmasını sağlar.

#resimleri göstermek için imshow
cv.imshow("opencv_test", img)
cv.waitKey(1)   #0 yazıldığında işlem sonsuza kadar aktif tutulur. Geçici bellekte sürekli yer tutar. Konsol çıktı vermez.
cv.destroyAllWindows()  #tüm pencerelerin kapanmasını sağlar. Birden fazla resimle çalışıldığında konsolun meşgul olmamasını sağlar.

