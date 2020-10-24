import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('../download/haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()

    # gray
    image_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detecção
    faces = face_cascade.detectMultiScale(image_gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.imshow('image_gray', image_gray)
        cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# harcascades, fonte: https://github.com/opencv/opencv/tree/master/data/haarcascades
