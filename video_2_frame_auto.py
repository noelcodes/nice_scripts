import numpy as np
import os
import glob
import cv2

face_cascade = cv2.CascadeClassifier('D:\\xrvision\\5_noelcodes\\data\\haarcascade_frontalface_default.xml')

i = 1

#vid_path = "D:/xrvision/5_noelcodes/xrv_indian_3/21Jan2018-entrance-extracted2.mp4"
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
       
#        color = (255, 0, 0)
#        stroke = 2
#        end_cord_x = x + w
#        end_cord_y = y + h
#        cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y), color, stroke)
	
        new = "noeface" + str(i) + ".jpg"
        cv2.imwrite(new, roi_color)
        i += 1
        
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()






   

            