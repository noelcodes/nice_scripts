import os
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
        print(dirs)
        year = (dirs.split('_')[0])        
        make = (dirs.split('_')[1])
        if not os.path.exists(make):
            os.makedirs(make)
                    
        try:
            os.rename(dirs,make)
            print("GOOD")
            
        except:
            print("BAD :" + dirs )
            for subdirs, dirss, files in os.walk(dirs):
                for file in files:
                    long_dir = (dirs + "/" +  file)
                    short_dir = (make + "/" + file)
                    os.rename(long_dir,short_dir)
            
# Delete empty directories                    
        if not os.listdir(dirs) :
            print(dirs)
            print("Directory is empty")
            shutil.rmtree(dirs, ignore_errors=False, onerror=handleRemoveReadonly)

            
os.chdir(path)