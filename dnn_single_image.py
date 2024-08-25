# DNN (DEEP NEURAL NETWORK) VE SSD (SINGLE SHOT MULTİBOX DETECTOR) İLE TEK SINIFLI GÖRÜNTÜ SINIFLANDIRMA

import cv2 as cv

model_bin = "06_UYGULAMALAR/02_DNN_ILE_GORUNTU_SINIFLANDIRMA_I/model/ssd/MobileNetSSD_deploy.caffemodel"  # modelin ağırlıklarını barındıran dosya
config_text = "06_UYGULAMALAR/02_DNN_ILE_GORUNTU_SINIFLANDIRMA_I/model/ssd/MobileNetSSD_deploy.prototxt"  # modelin katmanlarını barındıran dosya

objName = ["background", "aeroplane", "bicycle",
           "bird", "boat", "bottle", "bus", "car",
           "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person",
           "pottedplant", "sheep", "sofa", "train",
           "tvmonitor"]

net = cv.dnn.readNetFromCaffe(config_text, model_bin)

image = cv.imread("06_UYGULAMALAR/04_DNN_SSD_SINGLE_IMAGE_DETECTION/ ...")
h = image.shape[0]
w = image.shape[1]

layerNames = net.getLayerNames()
lastLayerId = net.getLayerId(layerNames[-1])
lastLayer = net.getLayer(lastLayerId)

blobImage = cv.dnn.blobFromImage(image, 0.007843, (300, 300), (127.5, 127.5, 127.5), True, False)
net.setInput(blobImage)
cvOut = net.forward()

for detection in cvOut[0, 0, :, :]:
    score = float(detection[2])
    objIndex = int(detection[1])
    if score > 0.5:
        left = detection[3] * w
        top = detection[4] * h
        right = detection[5] * w
        bottom = detection[6] * h
        cv.rectangle(image, (int(left), int(top)), (int(right), int(bottom)), (255, 0, 0), thickness=2)
        cv.putText(image, "score:%.2f, %s" % (score, objName[objIndex]),
                   (int(left) - 10, int(top) - 5), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

cv.imshow("mobilenet-ssd-demo", image)
cv.imwrite("result.png", image)
cv.waitKey(1)
