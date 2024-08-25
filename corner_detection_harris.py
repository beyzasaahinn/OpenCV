import cv2 as cv
import numpy as np

src = cv.imread("chessboard.png")


def harris(image):
    blockSize = 2
    apertureSize = 3
    k = 0.04

    # Görüntüyü gri tonlamaya çeviriyoruz.
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Harris köşe tespiti yapıyoruz.
    dst = cv.cornerHarris(gray, blockSize, apertureSize, k)

    # Sonuçları normalleştiriyoruz.
    dst_norm = np.empty(dst.shape, dtype=np.float32)
    cv.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
    dst_norm = cv.convertScaleAbs(dst_norm)

    # Köşe noktalarını işaretliyoruz.
    for i in range(dst_norm.shape[0]):
        for j in range(dst_norm.shape[1]):
            if dst_norm[i, j] > 120:
                cv.circle(image, (j, i), 2, (0, 255, 0), 2)

    return image


result = harris(src)
cv.imshow('result', result)
cv.waitKey(0)
cv.destroyAllWindows()

