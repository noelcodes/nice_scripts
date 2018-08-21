import os
import glob
os.chdir("D:/xrvision/google-images-download-master/downloads/saree")
i = 1
for old_file in glob.glob("*.jpg"): 
    new = "saree_" + str(i) + ".jpg"
    os.renames(old_file, new)
    i=i+1