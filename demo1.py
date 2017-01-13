# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 14:07:41 2016

@author: ashishHP
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('messi.jpg',0)

plt.imshow(img,cmap = 'gray',interpolation = 'bicubic')
plt.xticks([]),plt.yticks([]),
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
