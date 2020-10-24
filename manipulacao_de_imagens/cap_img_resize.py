from cv2 import resize, waitKey, imread, imshow

dir = '../midia/'
img = imread(f'{dir}cat.jpg')

imshow('imagem', img)

resize_img = resize(img, (200, 200))

imshow('RESIZE', resize_img)

waitKey(0)
