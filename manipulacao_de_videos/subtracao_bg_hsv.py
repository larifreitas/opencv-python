# hsv: uado para saturar uma cor específica usando o opencv
# SUBTRAÇÃO DE BACKGROUND COM HSV
import cv2
import numpy as np


def func(func):
    pass


# CAPTURE IMAGE
cap = cv2.VideoCapture(0)
# CREATE WINDOW
cv2.namedWindow('trackbars')
# baixas e altas do hsv pra saturar uma cor
cv2.createTrackbar('l-h', 'trackbars', 0, 255, func)  # lower
cv2.createTrackbar('l-s', 'trackbars', 0, 255, func)  # lower
cv2.createTrackbar('l-v', 'trackbars', 0, 255, func)  # lower
cv2.createTrackbar('u-h', 'trackbars', 255, 255, func)  # upper
cv2.createTrackbar('u-s', 'trackbars', 255, 255, func)  # upper
cv2.createTrackbar('u-v', 'trackbars', 255, 255, func)  # upper

# LOOP
while True:
    # GET TRACKBARS VALUE
    lh = cv2.getTrackbarPos('l-h', 'trackbars')
    ls = cv2.getTrackbarPos('l-s', 'trackbars')
    lv = cv2.getTrackbarPos('l-v', 'trackbars')
    uh = cv2.getTrackbarPos('u-h', 'trackbars')
    us = cv2.getTrackbarPos('u-s', 'trackbars')
    uv = cv2.getTrackbarPos('u-v', 'trackbars')

    # arrays do lower e upper para o hsv
    lower = np.array([lh, ls, lv])
    upper = np.array([uh, us, uv])

    # READ FRAME
    ret, frame = cap.read()

    # converter RGB(frame original) para HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    # criar máscara
    mask = cv2.inRange(hsv, lower, upper)

    # unir máscara c/ frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('result', result)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
