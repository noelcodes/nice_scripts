import numpy as np
import os
import glob
import cv2

os.chdir("D:/xrvision/0_google-images-download-master/google_images_download/downloads/malay")
#face_cascade =  cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
face_cascade = cv2.CascadeClassifier('D:\\xrvision\\5_noelcodes\\data\\haarcascade_frontalface_default.xml')

i = 9579
for old_file in glob.glob("*.jpg"): 
    frame = cv2.imread(old_file)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(old_file)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #img_item = "my-image.png"
        new = "mface" + str(i) + ".jpg"
        cv2.imwrite(new, roi_color)
        i=i+1
        








   

            