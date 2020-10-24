import cv2
import numpy as np

cap = cv2.VideoCapture(f"../midia/video.mp4")

sub = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

while True:
    _, frame = cap.read()

    mask = sub.apply(frame)
    kernel = np.ones((5, 5), np.uint8)

    # open
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # detectar contorno
    contourn, h = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    dilate = cv2.dilate(opening, kernel)

    # desenhar contornos
    cv2.drawContours(frame, contourn, -1, (0, 255, 0), 5)

    # cv2.imshow('mask', mask)
    cv2.imshow('dilate', dilate)  # menos ruídos pretos: opening na mascara e contourn no opening
    cv2.imshow('frame', frame)  # frame com contorno

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
