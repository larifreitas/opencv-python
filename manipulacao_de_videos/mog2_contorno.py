import cv2

cap = cv2.VideoCapture(f"../midia/video.mp4")

sub = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

while True:
    _, frame = cap.read()

    mask = sub.apply(frame)

    # detectar contorno
    contourn, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # desenhar contornos
    cv2.drawContours(frame, contourn, -1, (255, 255, 2))

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
