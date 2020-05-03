import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.VideoCapture(0)
ret,image=img.read()
im=cv2.imwrite('/home/apiiit-rkv/Desktop/curreency_denomination/train_light/frnt_new_10_6.jpg',image)
plt.imshow(image),plt.show()
