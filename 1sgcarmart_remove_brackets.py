# This script works only for sgcarmart web scrap dataset
# This Removes the folder's brackets
# Move all files to the shorter folder
# Then removes empty folders
# Just RUN again if it errors.

import os
import re
import regex
import errno, os, stat, shutil

path = "D:/xrvision/xrvision_dataset/sgcarmart_dataset"
os.chdir(path)


def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise

for subdirs, dirss, files in os.walk(path):
    for dirs in dirss:
        new_dirs = regex.subf(r"\((?:[^()]++|(?R))*+\)", "", dirs)

# Delete empty directories                    
        if not os.listdir(dirs) :
#            print(dirs)
#            print("Directory is empty")
            shutil.rmtree(dirs, ignore_errors=False, onerror=handleRemoveReadonly)
            continue

                    
                    
        try:
            os.rename(dirs,new_dirs)
        except:
            for subdirs, dirss, files in os.walk(dirs):
                for file in files:
                    file_short = new_dirs[:-1] + "/" + file
                    file_long = dirs + "/" + file
                    print("file_short" +  file_short)
                    print("file_long " + file_long)
                    # moves files to short dir
                    try:
                        os.rename(file_long,file_short)
                    except:
                        print("file_long XX " + file_long)
                        file_shortx = new_dirs[:-1] + "/x" + file
                        print(file_long)
                        print(file_shortx)
                        try:
                            os.rename(file_long,file_shortx)
                        except:
                            file_shortxs = new_dirs[:-2] + "/xs" + file
                            print(file_long)
                            print(file_shortxs)
                            os.rename(file_long,file_shortxs)
            
os.chdir(path)##  





