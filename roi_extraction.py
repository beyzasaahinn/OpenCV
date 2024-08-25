# Hareket halindeki nesneleri takip edip arka plandan ayırma işlemi gerçekleştireceğiz.

import numpy as np
import cv2 as cv

cap = cv.VideoCapture('videonunyolu/yoldayürüyeninsanvideosu')

fgbg = cv.createBackgroundSubtractorMOG2(history=500, varThreshold=100)

def process(image):
    mask = fgbg.apply(image)
    line = cv.getStructuringElement(cv.MORPH_RECT, (1, 5), (-1, -1))
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, line)
    cv.imshow("mask", mask)
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in range(len(contours)):
        area = cv.contourArea(contours[c])
        if area < 150:
            continue
        rect = cv.minAreaRect(contours[c])
        cv.ellipse(image, rect, (0, 255, 0), 2, 8)
        cv.circle(image, (np.int32(rect[0][0]), np.int32(rect[0][1])), 2, (255, 0, 0), 2, 8)
    return image

# işlemin sürekliliğini sağlamak için while kuruyoruz.
while True:
    ret, frame = cap.read()
    cv.imshow('input', frame)
    result = process(frame)
    cv.imshow('result', result)
    k = cv.waitKey(50) & 0xff
    if k == 27:
        break
        
