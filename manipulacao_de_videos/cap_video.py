# CAPTURANDO WEBCAM
from cv2 import VideoCapture, imshow, waitKey, destroyAllWindows

# 0->primeiro dispositivo de video encontrado pelo notebook
cap = VideoCapture(0)
# CAPTURANDO VIDEO local: cap = cv2.VideoCapture('detect_person.avi')

# criar um loop para percorrer todas as imagens do vídeo
while True:
    # recuperar cada imagem do video
    ret, frame = cap.read()

    if ret:
        # mostrar frame
        imshow('frame:', frame)

        # criar ROI -> corte de imagem
        roi_frame = frame[100:300, 200:400]

        # mostrar ROI
        imshow("ROI", roi_frame)

    # para não parar de rodar o vídeo, enquanto não dar o comando do if
    k = waitKey(1)
    if k == ord('q'):
        # para o loop se a tecla q parar
        break
# libera o cache de cap
cap.release()
# para não continuar aberto depois de break, destruir todas as janelas
destroyAllWindows()
