# Opencv'de görüntülerdeki qr kodunu tespit edebilmek ve çözebilmek adına qrcodetector adında bir metot vardır.

import cv2 as cv
import numpy as np

path = "qrcode.png"
src = cv.imread(path)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

'''
codeinfo : çözülen metin
points : qr kodunun köşelerinin çıktı dizisi
straight_qrcode : düzeltilmiş ve ikili hale getirilmiş olan qr kod
'''
qrcoder = cv.QRCodeDetector()
codeinfo, points, straight_qrcode = qrcoder.detectAndDecode(gray)

print(points)

result = np.copy(src)

cv.drawContours(result, [np.int32(points)], 0, (0, 0, 255), 2)  # Okuttuğumuz qr kodun etrafına kontör çizmek istersek

print("qrcode information is :\n%s" % codeinfo)     # qr kod üzerinden çözülen metni verir


cv.imshow("result", result)
cv.waitKey(1)

