import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mp


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])# multiplication using R,G,B value



img = mp.imread('VPICTURE_ASIF HASSAN.jpg')     
gray = rgb2gray(img)
cmap=plt.get_cmap('gray')
plt.imshow(gray,cmap)
plt.show()
