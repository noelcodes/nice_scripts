import numpy as np
import argparse
import imutils
import pickle
import cv2
from mtcnn.mtcnn import MTCNN

detector = MTCNN()
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
   
    result = detector.detect_faces(frame)
    if result != []:
        for person in result:
            bounding_box = person['box']
            x,y,w,h = bounding_box
            roi_color = frame[y:y+h, x:x+w]
            		   
            color = (255, 0, 0)
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y), color, stroke)

            cv2.imshow('frame',frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()















