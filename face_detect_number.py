import cv2
import sys
import os
# Get user supplied values

factor = sys.argv[2]
img_src = sys.argv[1]
cascPath = sys.argv[3]
folder = "Out/"
pathf = folder + str(factor) 
#os.mkdir(pathf)
pathf = pathf + "/"
dir = os.listdir(img_src)
for n in [12,14,16,18,20]:


    index = 0
    for file in dir:
        
        if file.endswith(".jpg"):                

            
            imagePath = img_src + "/" + file
    # Create the haar cascade
            faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
            image = cv2.imread(imagePath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
            faces = faceCascade.detectMultiScale(
            
                gray,
                scaleFactor=float(factor),
                minNeighbors=n,
                minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
            )
        

            

            for (x, y, w, h) in faces:
                index = index + 1

    print(str(index) + "\n")            






        