# UYGULAMA: DNN (DEEP NEURAL NETWORK) ile Görüntü Sınıflandırma
# GOOGLENET MODELİNE AİT KATMANINLARIN BİLGİLERİNİ OKUMA
# Daha önceden eğitilmiş bir modelin özellikleri kullanılarak
# Kullanılacak sınıf etketleri txt dosyasının içinde

import cv2 as cv
import numpy as np

path = "06_UYGULAMALAR/02_DNN_ILE_GORUNTU_SINIFLANDIRMA_I/"

bin_model = "06_UYGULAMALAR/02_DNN_ILE_GORUNTU_SINIFLANDIRMA_I/model/google/bvlc_googlenet.caffemodel"
protxt = "06_UYGULAMALAR/02_DNN_ILE_GORUNTU_SINIFLANDIRMA_I/model/google/bvlc_googlenet.prototxt"

net = cv.dnn.readNet(bin_model, protxt)

layer_names = net.getLayerNames()

for name in layer_names:
    id = net.getLayerId(name)
    layer = net.getLayer(id)
    print("layer id : %d, type : %s, name: %s" % (id, layer.type, layer.name))

# GOOGLENET MODELİ İLE GÖRÜNTÜ SINIFLANDIRMA
with open("06_UYGULAMALAR/02_DNN_ILE_GORUNTU_SINIFLANDIRMA_I/model/google/classification_classes_ILSVRC2012.txt",'rt') as f:
        classes = f.read().split('\n')

net = cv.dnn.readNetFromCaffe(protxt, bin_model)

image1 = cv.imread(path + "guinea_pig.jpg")
image2 = cv.imread(path + "dog.jpg")

'''
İkinci parametre ölçeklendirme faktörüdür, default değeri None'dır, 1 yapılırsa ölçeklendirme uygulanmaz. 
GoogleNet modeli, 224 x 224 boyutlarında girdi görüntüsü almaktadır
Dördüncü argüman görüntülerin piksellerin elde edilen ortalama değerlerdir
Beşinci argümanı true yaparsak sıralama RGB şeklinde olur, yoksa bgr
'''
blob = cv.dnn.blobFromImage(image1, 1.0, (224, 224), (104, 117, 123), False, crop=False)  # Burada kullanılacak fonksiyon önceden öğretilmiş modelin girdileri ile bizim verdiğimiz girdilerin aynı dili konuşmasını sağlamaktadır

result = np.copy(image1)

net.setInput(blob)
out = net.forward()     # Ağı ileri doğru besle

out = out.flatten()

classId = np.argmax(out)   # Olasılık değeri en yüksek olanı almamız gerekiyor
confidence = out[classId]

# Modelin performansıyla ilgili bir raporlama
t, _ = net.getPerfProfile()
label = 'cost time: %.2f ms' % (t * 1000.0 / cv.getTickFrequency())
cv.putText(result, label, (0, 20), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

# Label'ın ne olduğuyla ilgli bilgi
label = '%s: %.4f' % (classes[classId] if classes else 'Class #%d' % classId, confidence)
cv.putText(result, label, (0, 60), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

show_img = np.hstack((image1, result))
cv.namedWindow('demo', cv.WINDOW_NORMAL)
cv.imshow("demo", show_img)
cv.waitKey(1)




