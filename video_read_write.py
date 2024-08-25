# Bir videoyu okuyacağız ve yazma işlemini gerçekleştireceğiz.

import cv2 as cv
import numpy as np

capture = cv.VideoCapture("Ekran Kaydı 2024-08-06 16.54.05.mov")
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)  # video dosyasındaki toplam kare sayısını alır.
fps = capture.get(cv.CAP_PROP_FPS)            # videonun saniyedeki kare sayısını alır.
print(height, width, count, fps)

out = cv.VideoWriter("Ekran Kaydı 2024-08-06 16.54.05.mov/ds_path_save.avi",
                     cv.VideoWriter_fourcc('D', 'I', 'V', 'X'), 15,
                     (int(width), int(height)), True)

while True:
    # kameradan görüntü al
    ret, frame = capture.read()

    # görüntü başarıyla alındı mı kontrol et
    if ret is True:
        # okunan görüntüyü ekranda göster
        cv.imshow("video-input", frame)
        out.write(frame)
        # 50 ms sonra çık
        c = cv.waitKey(50)
        if c == 27:  # ESC tuşu
            break
    else:
        break

capture.release()
# Terminalde komutun durması için Ctrl + C'ye basılacak.
out.release()  # Geçici bellekte kapladığı alan serbest bırakılacak.

