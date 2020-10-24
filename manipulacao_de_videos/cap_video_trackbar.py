# criação de trackbars para controle do vídeo
from cv2 import VideoCapture, imshow, waitKey, destroyAllWindows, namedWindow, createTrackbar, getTrackbarPos

cap = VideoCapture(0)


# função necessária para criar a trackbar
def nothing(x):
    pass


# criar janela de trackbars
namedWindow('trackbars')
#  1º trackbar | janela que vai aparecer | valor que começa, entre 0 e 800 | nothing
x = createTrackbar('x', 'trackbars', 0, 500, nothing)  # 1º ponto
y = createTrackbar('y', 'trackbars', 0, 500, nothing)  # 2 º ponto
h = createTrackbar('w', 'trackbars', 200, 500, nothing)  # weight - largura
w = createTrackbar('h', 'trackbars', 200, 500, nothing)  # height - altura

while True:
    # recuperar trackbar
    x = getTrackbarPos('x', 'trackbars')
    y = getTrackbarPos('y', 'trackbars')
    w = getTrackbarPos('w', 'trackbars')
    h = getTrackbarPos('h', 'trackbars')

    # recuperar frame do vídeo
    ret, frame = cap.read()

    # y: ponto inicial da altura, h:altura, x:ponto inicial da largura, w:largura
    roi = frame[y:h, x:w]

    imshow("ROI", roi)
    imshow("frame", frame)

    if waitKey(1) == ord('q'):
        break

cap.release()
destroyAllWindows()
