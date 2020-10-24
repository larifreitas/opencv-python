# usando a mascara para detectar contornos
import cv2
import numpy as np


def f(f):
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow('tb')
cv2.createTrackbar('lh', 'tb', 0, 255, f)
cv2.createTrackbar('ls', 'tb', 0, 255, f)
cv2.createTrackbar('lv', 'tb', 0, 255, f)
cv2.createTrackbar('uh', 'tb', 255, 255, f)
cv2.createTrackbar('us', 'tb', 255, 255, f)
cv2.createTrackbar('uv', 'tb', 255, 255, f)

while True:
    lh = cv2.getTrackbarPos('lh', 'tb')
    ls = cv2.getTrackbarPos('ls', 'tb')
    lv = cv2.getTrackbarPos('lv', 'tb')
    uh = cv2.getTrackbarPos('uh', 'tb')
    us = cv2.getTrackbarPos('us', 'tb')
    uv = cv2.getTrackbarPos('uv', 'tb')

    lower = np.array([lh, ls, lv])
    upper = np.array([uh, us, uv])

    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    mask = cv2.inRange(hsv, lower, upper)

    # detectar contorno
    contourn, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # desenhar contornos
    cv2.drawContours(frame, contourn, -1, (255, 255, 2))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
