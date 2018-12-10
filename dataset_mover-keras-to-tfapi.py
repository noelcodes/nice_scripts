# This script mainly designed for faster-RCNN tensoreflow API preparation
# Splits 80% train 20% val folder
# moves jpg + xml to train folder
# xml to xml folder
# Script put at 1x level down from "path"
# "path" is where txt and xml folder generated.
# dataset_path is where all FOLDERS of images located.
# set working directary same as path

import os
from sklearn.cross_validation import train_test_split

path = "D:/xrvision/5_noelcodes/try_folder/"
os.chdir(path)

dataset_path = "D:/xrvision/5_noelcodes/try_folder/dataset/"

train_path = "D:/xrvision/5_noelcodes/try_folder/train/"

    


#
#if not os.path.exists("train"):
#    os.makedirs("train")
#if not os.path.exists("val"):
#    os.makedirs("val")


    
i = 0
for subdir, dirs, files in os.walk(train_path):
#    print(subdir)
    
    X = y= os.listdir(str(subdir))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=13)
    
    print(X_train)

#
#    for file in files:
#        if 'jpg' in file:
#            whole_path = (str(subdir) + "/" + str(file))
#            sub_folder = (str(subdir[len(dataset_path):]))
#
#            if not os.path.exists(path + "train/" + sub_folder ):
#                os.makedirs(path + "train/" + sub_folder)
#
#            cur_loc = whole_path
#            new_loc = path + "train/" + "x3" + file
#            os.rename(cur_loc,new_loc)
#            
#        elif 'xml' in file:
#            whole_path = (str(subdir) + "/" + str(file))
#            sub_folder = (str(subdir[len(dataset_path):]))
#            
#            cur_loc = whole_path
#            new_loc = path + "train/" + "x3" + file
#            os.rename(cur_loc,new_loc)
#
## set back to working path, else it will jump back to default path for unknow reason
#os.chdir(path)
###    
    # done something

                   