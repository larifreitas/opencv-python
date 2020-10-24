import numpy as np
import cv2 as cv

# Define limites maiores e menores das cores no espaço de cores HSV
lower = {'red': (166, 84, 141),
         'blue': (97, 100, 117),
         'yellow': (23, 59, 119),
         'green': (132, 176, 132)}
upper = {'red': (186, 255, 255),
         'blue': (117, 255, 255),
         'yellow': (54, 255, 255),
         'green': (174, 255, 174)}

# Cores padrão para circular o objeto
colors = {'red': (0, 0, 255),
          'blue': (255, 0, 0),
          'yellow': (0, 255, 117),
          'green': (0, 255, 0)}

# Transformando as imagens capturadas de RGB para HSV
cap = cv.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame_color = cv.resize(frame, (600, 600))

    # Converte BGR pra HSV
    hsv = cv.cvtColor(frame_color, cv.COLOR_BGR2HSV)

    # Percorrer o dicionario de cores lower até upper
    # criando uma mask para objetos que possuam esses ranges de cores
    # Definindo contorno
    for key, value in upper.items():
        kernel = np.ones((9, 9), np.uint8)
        mask = cv.inRange(hsv, lower[key], upper[key])
        mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
        mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

        # Encontra contorno na máscara
        contourn = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]

        # Se o objeto com as cores definidas for maior que o threshold definido
        if len(contourn) > 0:
            threshold = 0.5
            c = max(contourn, key=cv.contourArea)
            ((x, y), radius) = cv.minEnclosingCircle(c)
            M = cv.moments(c)
            center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

            if radius > 0.5:
                cv.circle(frame, (int(x), int(y)),
                           int(radius), colors[key], 2)
                cv.putText(frame, key + " object", (int(x - radius), int(y - radius)),
                            cv.FONT_HERSHEY_SIMPLEX, 0.6, colors[key], 2)

        cv.imshow('frame', frame)
        cv.imshow('mask', mask)

    k = cv.waitKey(1) & 0xFF
    if k == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
