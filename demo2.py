# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 09:20:30 2017

@author: ashishHP

import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2GRAY)
    cv2.imshow('frame',gray)
    if cv2.Waitkey(1) & 0xFF == ord('q'):
        break
    cap.release()
    cv2.desroyAllWindows
"""
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
# Capture frame-by-frame
    ret, frame = cap.read()
# Our operations on the frame come here
   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()