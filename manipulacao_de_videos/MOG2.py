# Subtração de background com MOG2
import cv2

cap = cv2.VideoCapture(f"../midia/video.mp4")

sub = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

while True:
    _, frame = cap.read()

    # mascara para usar a subtração
    mask = sub.apply(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
