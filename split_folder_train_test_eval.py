from scipy.misc import imread
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import scipy

path2 = "D:/xrvision/5_noelcodes/temp/split"
os.chdir(path2)

if not os.path.exists('train'):
    os.makedirs('train')
if not os.path.exists('test'):
    os.makedirs('test')
if not os.path.exists('dev'):
    os.makedirs('dev')        

path = "D:/xrvision/5_noelcodes/temp/dataset"
os.chdir(path)

count = 0
for subdirs, dirs, files in os.walk(path):
    n_path, n_dirs, n_files = next(os.walk(subdirs))
    file_count = len(n_files)
    train, test = round(file_count*0.7) , round(file_count*0.3)        
    print(file_count , train , test)
# Code for train and test folder only    
    for file in files:
        if test != 0:
            img_path = subdirs + "/" + file
            folder_name = subdirs[len(path)+1:]
            new = (path2 + '/test' + img_path[len(path):])
            print(img_path)
            print(new)
            os.renames(img_path, new)
            test = test -1

        
        
        try:
            if train != 0:
                img_path = subdirs + "/" + file
                folder_name = subdirs[len(path)+1:]
                new = (path2 + '/train' + img_path[len(path):])
                print(img_path)
                print(new)
                os.renames(img_path, new)
                train = train -1
        except:
            continue    
            
            
# Code for dev folder only    
#    try:
#        count +=1
#        img_path = subdirs + "/" + n_files[0]
#        new = (path2 + '/dev' )
#        print(img_path)
#
#        new = (subdirs[len(path)+ 1:].split('_')[1]) + '.jpg'
#        new = (path2 + '/dev/' + new)
#        print(new)        
#        os.renames(img_path, new)
#    except:
#        continue            