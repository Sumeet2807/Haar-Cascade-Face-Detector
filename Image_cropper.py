
# coding: utf-8

# In[13]:


import cv2
import os
import sys
import numpy as np


img_path = sys.argv[1]
out_path = sys.argv[2]
if len(out_path) <= 0:
    exit()
if out_path[-1] != "/":
    out_path += "/"

image = cv2.imread(img_path)

steps = [24,32,64,120,240]
num = 0
for step in steps:
    
    h_range = np.arange(1,image.shape[0],step,dtype=int)
    w_range = np.arange(1,image.shape[1],step,dtype=int)
    
    for height in h_range:
        for width in w_range:
            if (width+(step-1) <= image.shape[1]) and (height+(step-1) <= image.shape[0]):
                num += 1
                path = out_path + "image" + str(num) + ".jpg"
                cropped = image[height : height + step, width : width + step]
                cv2.imwrite(path, cropped)
                
                
                
            
           
            

