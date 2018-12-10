import numpy as np
import os
import glob
import cv2
from mtcnn.mtcnn import MTCNN

os.chdir("D:/xrvision/XRV_projects/age_gender_ethicity_dataset/UTKface_dataset/racenet_v13_abandon/dataset/train/Caucasian")
#face_cascade =  cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
#face_cascade = cv2.CascadeClassifier('D:\\xrvision\\5_noelcodes\\data\\haarcascade_frontalface_default.xml')
detector = MTCNN()


i = 1
for old_file in glob.glob("*.jpg"): 
    frame = cv2.imread(old_file)
    result = detector.detect_faces(frame)
    if result != []:
        for person in result:
            bounding_box = person['box']
            x,y,w,h = bounding_box
            roi_color = frame[y:y+h, x:x+w]

            if roi_color.shape[0] > 50 and roi_color.shape[1] > 50:
                print(old_file)
                print(roi_color.shape)
                new = "XRmtcnnC" + str(i) + ".jpg"
                cv2.imwrite(new, roi_color)
                i=i+1
            else:
                continue
    





   

            