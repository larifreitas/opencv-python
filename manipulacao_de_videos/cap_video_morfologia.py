import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def func(run):
    pass


cv2.namedWindow('track')
th = cv2.createTrackbar('th', 'track', 200, 255, func)  # threshold
er = cv2.createTrackbar('er', 'track', 1, 255, func)
di = cv2.createTrackbar('di', 'track', 1, 255, func)
op = cv2.createTrackbar('op', 'track', 1, 255, func)
cl = cv2.createTrackbar('cl', 'track', 1, 255, func)

while True:
    ret, frame = cap.read(0)

    # controles
    th = cv2.getTrackbarPos('th', 'track')  # threshold
    er = cv2.getTrackbarPos('er', 'track')
    di = cv2.getTrackbarPos('di', 'track')
    op = cv2.getTrackbarPos('op', 'track')
    cl = cv2.getTrackbarPos('cl', 'track')

    # RISIZE
    img_resize = cv2.resize(frame, (250, 200))
    cv2.imshow('img_resize', img_resize)

    # CINZA(p/b)
    gray = cv2.cvtColor(img_resize, cv2.COLOR_RGB2GRAY)
    cv2.imshow('gray', gray)

    # THRESHOULD, 255: luminosidade | binary:preto e branco
    ret, thres = cv2.threshold(gray, th, 255, cv2.THRESH_BINARY)
    cv2.imshow('thres', thres)

    #  BLUR (suaviza thres)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imshow('blur', blur)

    # KERNEL  de 5x5
    kernel = np.ones((5, 5), np.uint8)

    # EROSION(thres em erosion)
    erosion = cv2.erode(thres, kernel, iterations=er)
    # cv2.imshow('erosion', erosion)

    # dilatação
    dilat = cv2.dilate(thres, kernel, iterations=di)
    # cv2.imshow('dilate', dilat)

    #open
    opening = cv2.morphologyEx(thres, cv2.MORPH_OPEN, kernel, iterations=op)
    cv2.imshow('op', opening)

    #close
    closing = cv2.morphologyEx(thres, cv2.MORPH_CLOSE, kernel, iterations=cl)
    cv2.imshow('cl', closing)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
