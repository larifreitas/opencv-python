import cv2

cap = cv2.VideoCapture('../download/video.mp4')

_, first_frame = cap.read()
first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_frame = cv2.GaussianBlur(first_frame, (3, 3), 0)

while True:
    _, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.GaussianBlur(frame_gray, (3, 3), 0)

    diff = cv2.absdiff(first_frame, frame_gray)
    cv2.imshow('diff', diff)

    _, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    cv2.imshow('diff', diff)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
