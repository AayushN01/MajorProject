import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.VideoCapture(0)
ret,image=img.read()
im=cv2.imwrite('/home/apiiit-rkv/Desktop/currency-detector-opencv-master/train/old_50/test_old_50_6.jpg',image)
plt.imshow(image),plt.show()
