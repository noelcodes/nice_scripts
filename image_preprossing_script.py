from __future__ import print_function
import numpy as np
import glob
import cv2
import os

def adjust_gamma(image, gamma):
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	return cv2.LUT(image, table)

########################################
os.chdir("D:/xrvision/XRV_projects/age_gender_ethicity_dataset/UTKface_dataset/\
/gender_v15/dataset/train/female/")

i = 1
g = 1
for old_file in glob.glob("*.jpg"):
    original = cv2.imread(old_file)
    for gamma in np.arange(0.5, 2.0, 0.5):  
        if gamma == 1.0 or gamma == 1.5:
            continue
        else:
            adjusted = adjust_gamma(original, gamma=gamma)
            new = "gamma_" + str(g) + ".jpg"
            cv2.imwrite(new, adjusted)
            g=g+1
        
    gray_name = "gray_" + str(i) + ".jpg"
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(gray_name, gray)
    
    blur_name = "blur_" + str(i) + ".jpg"
    blur = cv2.blur(original,(7,7))
    cv2.imwrite(blur_name, blur)
    
    guas_name = "guas_" + str(i) + ".jpg"
    gausBlur = cv2.GaussianBlur(original,(7,7),0)
    cv2.imwrite(guas_name, gausBlur)
    
    bilf_name = "bilFilter_" + str(i) + ".jpg"
    bilFilter = cv2.bilateralFilter(original,9,75,75)
    cv2.imwrite(bilf_name, bilFilter)
    
    i=i+1
#
#########################################################    
    

