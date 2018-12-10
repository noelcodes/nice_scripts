# This script mainly designed for yolo preparation
# moves jpg to txt folder
# xml to xml folder
# Only works in 1x level folder, meaning path = is the main_path, and subsequent are last level of folders
# Also make sure working folder is SAME as path
import os
import pandas as pd
#path = "D:/xrvision/5_noelcodes/try_folder/"
#os.chdir(path)
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


path = "D:/xrvision/0_google-images-download-master/google_images_download/downloads"
os.chdir(path)
df_raw = pd.read_csv('./ijbb_subject_names.csv', keep_default_na=False)
df_raw.SUBJECT_NAME[0]

i = 1
score = 0
for subdirs, dirs, files in os.walk(path):
    for dirss in dirs:
        for row in range(0, len(df_raw)):
            pd_name = (df_raw.loc[row,'SUBJECT_NAME'])
            dir_index = (df_raw.loc[row,'SUBJECT_ID'])
            score = similar(dirss,pd_name)
            
            if score > 0.82:
                print(pd_name)
                print(dirss)
                print(dir_index)
                print(score)
                os.rename(dirss,str(dir_index))

#            if str(dirss) == str(df_raw.loc[row,'SUBJECT_NAME']):
#                print('True')
#                pd_name = (df_raw.loc[row,'SUBJECT_NAME'])
#                dir_name = (dirss)
#                dir_index = (df_raw.loc[row,'SUBJECT_ID'])
#                print(pd_name)
#                print(dir_name)
#                print(dir_index)
#                os.rename(dirss,str(dir_index))
                
            else:
                continue
            
    
#for subdirs, dirs, files in os.walk(path):
#    for dirss in dirs:
#        for row in range(0, len(df_raw)):
#
#            if str(dirss) == str(df_raw.loc[row,'SUBJECT_NAME']):
#                print('True')
#                pd_name = (df_raw.loc[row,'SUBJECT_NAME'])
#                dir_name = (dirss)
#                dir_index = (df_raw.loc[row,'SUBJECT_ID'])
#                print(pd_name)
#                print(dir_name)
#                print(dir_index)
#                os.rename(dirss,str(dir_index))
#                
#            else:
#                continue

    
# set back to working path, else it will jump back to default path for unknow reason
os.chdir(path)##    
    # done something

#item {
#  id: 1
#  name: 'dress'
#}

