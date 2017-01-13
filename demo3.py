# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 09:43:53 2017

@author: ashishHP
"""

import numpy as np
import cv2
img = np.zeros((119,119,3),np.uint8)
img =cv2.line(img,(0,0),(118,118),(255,0,0),5)
cv2.imshow('image',img)