
import os
import re
import regex
import errno, os, stat, shutil

path = "D:/xrvision/xrvision_dataset/sgcarmart_gen"
new_path = "D:/xrvision/xrvision_dataset/sgcarmart_gen"
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
        print(subdirs + "/" + dirs)
        print(subdirs)
        print(dirs + "_" + subdirs[len(path)+1:])   
        new_gen = (dirs + "_" + subdirs[len(path)+1:])
        new_gen_path = (new_path + "/" + new_gen)        

        
        
        
#        try:
#            data = int(input("Enter a number: "))
#        except:
#            
#            data = 10
#        
#        dir_split = (dirs.split())
#        print(dir_split)
#        new_dir = (" ".join(dir_split[:data]))
#        print(new_dir)
#        if not os.path.exists(new_dir):
#            os.makedirs(new_dir)
#                
#        
#        for subdirs, dirss, files in os.walk(dirs):
#            for file in files:
#                file_short = new_dir + "/" + file
#                file_long = dirs + "/" + file
#                print("file_short" +  file_short)
#                print("file_long " + file_long)
#                # moves files to short dir
#                os.rename(file_long,file_short)
#          
#        # Delete empty directories                    
#        if not os.listdir(dirs) :
#            print(dirs)
#            print("Directory is empty")
#            shutil.rmtree(dirs, ignore_errors=False, onerror=handleRemoveReadonly)
        
            
os.chdir(path)##          
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        







