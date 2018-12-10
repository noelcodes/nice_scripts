# This script works too
# Only renaming the files based on the year
# There is another script to remove the year from folder and merges

import os

path = "D:/xrvision/xrvision_dataset/sgcarmart_dataset"
os.chdir(path)


for subdirs, dirss, files in os.walk(path):
    for dirs in dirss:
        print(dirs)
        year = (dirs.split('_')[0])        
        make = (dirs.split('_')[1])
        for subdirs, dirss, files in os.walk(dirs):
            for file in files:
                print(dirs + "/" + file)
                print(dirs + "/" + year + "_" + file)
                old_file = (dirs + "/" + file)
                new_file = (dirs + "/" + year + "_" + file)                
                os.rename(old_file,new_file)
                