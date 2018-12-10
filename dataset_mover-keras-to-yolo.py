# This script mainly designed for yolo preparation
# moves jpg to txt folder
# xml to xml folder
# Script put at 1x level down from "path"
# "path" is where txt and xml folder generated.
# dataset_path is where all FOLDERS of images located.
# set working directary same as path

import os

path = "D:/xrvision/5_noelcodes/try_folder/"
os.chdir(path)

dataset_path = "D:/xrvision/5_noelcodes/try_folder/dataset/"

if not os.path.exists("txt"):
    os.makedirs("txt")
if not os.path.exists("xml"):
    os.makedirs("xml")
    
i = 0
for subdir, dirs, files in os.walk(dataset_path):
    for file in files:
        if 'jpg' in file:
            whole_path = (str(subdir) + "/" + str(file))
            sub_folder = (str(subdir[len(dataset_path):]))

            if not os.path.exists(path + "txt/" + sub_folder ):
                os.makedirs(path + "txt/" + sub_folder)

            cur_loc = whole_path
            new_loc = path + "txt/" + sub_folder + "/" + file
            os.rename(cur_loc,new_loc)
            
        elif 'xml' in file:
            whole_path = (str(subdir) + "/" + str(file))
            sub_folder = (str(subdir[len(dataset_path):]))

            if not os.path.exists(path + "xml/" + sub_folder ):
                os.makedirs(path + "xml/" + sub_folder)

            cur_loc = whole_path
            new_loc = path + "xml/" + sub_folder + "/" + file
            os.rename(cur_loc,new_loc)

# set back to working path, else it will jump back to default path for unknow reason
os.chdir(path)
##    
    # done something

                   