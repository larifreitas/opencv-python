# importando opencv
import cv2
from cv2 import imread, imshow, waitKey, resize, imwrite

# criando variável para receber o valor da imagem, (passar caminho da imagem)
# caminho para as imagens
dir = '../imagens/'
img = imread(f'{dir}/person.jpg')

# mostrando img
imshow('imagem: ', img)

#  salvar nova imagem -> ler e salvar
print('nova')
imwrite(f'{dir}/new_person.jpg', img)

# CRIANDO ROI -> Roi é o corte principal para a detecção de determinada parte da imagem
roi_person = img[160:350, 400:580]
# roi_dog = img[370:560, 390:590]
# roi_horse = img[50:230, 650:800]

# mostrando o roi
imshow('Roi: ', roi_person)
# imshow('Roi: ', roi_dog)
# imshow('Roi: ', roi_horse)

#  resize -> redimencionar(objeto_para_redimensionar, (alt, larg))
resize_person = resize(img, (500, 500))

#  mostrando imagem redimensionada
imshow('Imagem redimensionada: ', resize_person)

# pausa -> para que a execução da imagem não feche
waitKey(0)
