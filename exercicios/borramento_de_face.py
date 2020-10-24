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
        # roi de face
        roi = frame[y:y + h, x:x + w]

        # aumentar uma imagem diminuida causa má qualidade
        roi = cv2.resize(roi, (10, 10))
        roi = cv2.resize(roi, (w, h))

        frame[y:y + h, x:x + w] = roi

        # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

        cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# harrcascades, fonte: https://github.com/opencv/opencv/tree/master/data/haarcascades
