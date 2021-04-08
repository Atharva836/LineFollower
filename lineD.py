# A program using OpenCV to detect yellow and white lines on the image of a road.

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('line_detection.jpg') # To read the image given
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # To convert original image to a gray-scaled image

ret, mask = cv2.threshold(img_gray,160,255,cv2.THRESH_BINARY)
 # Converts all points in gray-scaled image having pixel value >160 to 255 and rest all points to 0

location = np.where(mask == 255) 
# To filter out all the locations in the image having pixel value of 255(as converted by the cv2.threshold function)

for point in zip(*location[::-1]): 
    cv2.circle(img, point, 1, (0,0,255)) # To create a red coloured circle at points given by the 'location' parameter

cv2.imshow('image',img) # To show the image
cv2.waitKey(0)
cv2.destroyAllWindows()
