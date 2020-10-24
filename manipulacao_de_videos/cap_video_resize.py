#  Alterando tamanho do frame
from cv2 import VideoCapture, waitKey, imshow, destroyAllWindows, resize

cap = VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        imshow('original', frame)

        #  redimensiona(frame, largura, altura)
        resize_frame = resize(frame, (100, 100))
        #  mostra redimensionamento
        imshow('RESIZE', resize_frame)

    # 27 == ESC
    wait_key = waitKey(1)
    if wait_key == 27:
        break

cap.release()
destroyAllWindows()
