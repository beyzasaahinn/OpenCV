# burada amacımız eşik değerini kullanarak çeşitli görseller oluşturmak.
'''
Daha açık bir şekilde anlatacak olursak, elimizdeki görsele bir threshold belirleyeceğiz ve
bu thresholdun altında veya üstünde kalma durumuna göre elimizdeki resmin farklı formatlarını çıkaracağız.
Aslında bir nevi filtreleme işlemi yapacağız.
'''

import cv2 as cv

path = "work.png"
src = cv.imread(path)

T = 127  # 0 ile 255 arasındaki değerlerden 127'yi threshold olarak belirliyoruz.

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

'''
Basitçe bir döngü yazacağız. Bu döngünün amacı girdi görüntüsüne göre 
optimum eşk değerini otomatik olarak hesaplayarak bize farklı farklı görseller elde etme imkanı sunacak
 '''

for i in range(5):
    ret, binary = cv.threshold(gray, T, 255, i)
    cv.imshow("binary_" + str(i), binary)

cv.waitKey(0)