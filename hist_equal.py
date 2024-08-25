''''Histogram eşitleme, histogram dağılımının daha eşit olmasını sağlar.
Histogram eşitlemenin amacı kontrast (zıtlık) yaratmaktır.
Kötü çekilen resimlerde kotrast yaratırsak resmi zenginleştirmiş oluruz.'''


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

src = cv.imread("lab.png")
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("input", gray)
cv.waitKey(1)


def custom_hist(gray):
    h, w = gray.shape
    hist = np.zeros([256], dtype=np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1

    y_pos = np.arange(0, 256, 1, dtype=np.int32)
    plt.bar(y_pos, hist, align='center', color='r', alpha=0.5)
    plt.xticks(y_pos, y_pos)
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

# custom_hist(gray)

dst = cv.equalizeHist(gray)
cv.imshow("eh", dst)
cv.waitKey(0)

custom_hist(dst)

# resimler kıyaslandığında eşitlenmiş histograma sahip resmin daha anlaşılır olduğunu görürüz.


