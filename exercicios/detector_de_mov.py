import cv2
import numpy as np

cap = cv2.VideoCapture(0)

sub = cv2.createBackgroundSubtractorMOG2(varThreshold=200, detectShadows=True)


while True:
    _, frame = cap.read()
    mask = sub.apply(frame)
    kernel = np.ones((5, 5), np.uint8)

    open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    ret, mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
    dilate = cv2.dilate(mask, kernel)
    close = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
    contourn, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)

    for c in contourn:
        area = cv2.contourArea(c)
        if area > 600:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow('open', open)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
