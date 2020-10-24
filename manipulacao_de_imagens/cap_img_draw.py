import cv2

dir = '../midia/'
img = cv2.imread(f'{dir}cat.jpg')
cv2.imshow('imagem:', img)

#  LINHA, parâmetros:
#  -10x10 px de distancia da horizontal e da vertical, onde a linha começa
#  -200x200 px de distancia da horizontal e vertical, onde a linha termina
# - (b, g, r)-> rgb
# -Grossura da linha
line = cv2.line(img, (10, 10), (200, 200), (0, 200, 0), 5)
# cv2.imshow('Line:', line)

#  RETANGULO/QUADRADO, parâmetros:
rectangle = cv2.rectangle(img, (10, 10), (200, 200), (0, 0, 200), 2)
# cv2.imshow('Rectangle', rectangle)

#  CIRCULO, parâmetros
#  posição do meio do circulo | raio do circulo | cor | espessura *p/ circulo preenchido: -1
circle = cv2.circle(img, (200, 200), 40, (50, 0, 0), 8)
# cv2.imshow('circle', circle)

circle_1 = cv2.circle(img, (200, 200), 40, (0, 5, 50), -1)
# cv2.imshow('circle_1', circle_1)

#TEXTO, parâmetros:
#  imagem | texto para exibição | posição do texto, como no circulo(30x30, para horizontal x vertical | fonte \
#  CÓD ou nome da fonte | cor | espessura | deixa imagem menos pixalizada

text = cv2.putText(img, 'opencv', (10, 220), cv2.FONT_HERSHEY_SIMPLEX, 1, (25, 50, 46), 2, cv2.LINE_AA)
cv2.imshow('texto', text)

# pausa
cv2.waitKey(0)
