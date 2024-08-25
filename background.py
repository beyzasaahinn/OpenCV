# Bir videonun arka planını çıkarma işlemini gerçekleştireceğiz.

'''
varthreshold, odaklanılacak görüntüde ne kadar hassas olunacağını ifade eder.
history ise gecikmelere ne kadar odaklanmamız gerektiğini ifade eder.
Gecikmelerden kasıt, video akarkenki her bir pencere.
'''

import cv2 as cv

cap = cv.VideoCapture('lab3.mp4')

fgbg = cv.createBackgroundSubtractorMOG2(history=250, varThreshold=250)

while True:
    ret, frame = cap.read()                     # yüklemiş olduğumuz videoyla alakalı bilgileri tutar.
    fgmask = fgbg.apply(frame)                  # uygulanan siyah arka plana ait yapıyı tutar.
    background = fgbg.getBackgroundImage()      # arkaplan görüntüsünün hesaplandığı bölüm
    cv.imshow('input', frame)
    cv.imshow('mask', fgmask)
    cv.imshow('background', background)
    k = cv.waitKey(10) & 0xff
    if k == 27:
        break

        cap.release()
        cv.destroyAllWindows()
