import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler #statsmodels api module
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.cross_validation import cross_val_score, cross_val_predict
import os
import cv2

sns.set_style('darkgrid')
%config InlineBackend.figure_format = 'retina'
%matplotlib inline

path = "D:/xrvision/xrvision_dataset/IJB dataset"
os.chdir(path)

df_raw = pd.read_csv('./ijbb_subject_names.csv', keep_default_na=False)
len(df_raw.index)


#df_raw.SUBJECT_NAME[0]
##
#for i in range(len(df_raw.index)):
#    print(df_raw.SUBJECT_NAME[i] + ' face, ', end='')
    
#    old_file = df_raw.FILENAME[i]    
#    x = df_raw.FACE_X[i]
#    y = df_raw.FACE_Y[i]
#    w = df_raw.FACE_WIDTH[i]
#    h = df_raw.FACE_HEIGHT[i]
#    
#    frame = cv2.imread(old_file)
#    roi = frame[y:y+h, x:x+w]
#    
#    folder = str(df_raw.SUBJECT_ID[i])
#    if not os.path.exists(path + "/extracted2/"  + folder):
#        os.makedirs(path + "/extracted2/"  + folder)    
#    
#    if 'img' in old_file :
#        new = path + "/extracted2/"  + folder + "/face_" + old_file[4:]
#        cv2.imwrite(new, roi)
#    
#    elif 'frames' in old_file:
#        new = path + "/extracted2/"  + folder + "/face_" + old_file[7:]
#        cv2.imwrite(new, roi)
        
