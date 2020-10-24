from cv2 import imshow, imread, waitKey

dir = '../midia/'

img = imread(f'{dir}dog.jpg')
imshow('imagem', img)

roi_dog = img[200:550, 8:482]
imshow('ROI', roi_dog)

waitKey(0)
