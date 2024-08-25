import cv2 as cv
import numpy as np

#tıpkı iki numpy arrayini birleştiriyormuş gibi birleştirme işlemi gerçekleştireceğiz.
path1 = "left_images.png"
path2 = "right_images.png"

img1 = cv.imread(path1)
img2 = cv.imread(path2)

cv.imshow("spider_man1", img1)
cv.waitKey(1)

cv.imshow("spider_man2", img2)
cv.waitKey(1)

#görüntüyü birleştirmek için hstack metodu kullanıyoruz.
horizontal = np.hstack((img1, img2))

cv.imshow("spider_man", horizontal)
cv.waitKey(1)
cv.destroyAllWindows()