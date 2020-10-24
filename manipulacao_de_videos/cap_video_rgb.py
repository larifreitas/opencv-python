import cv2

cap = cv2.VideoCapture(0)

while (1):
    ret, frame = cap.read()

    (b, g, r) = frame[200, 200]
    frame[198:202, 198:202] = (0, 0, 255)
    frame[10:90, 10:90] = (b, g, r)

    cv2.imshow("Video", frame)

    # 27 == ESC
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
