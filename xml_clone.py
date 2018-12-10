# This script works
# You use this bcos many images had the same annotation bbox position
# Put this script outside txt and xml folder.
# First labellmg a good xml, pull out paste at filepath
# Run script
# It will run thru txt folder, take the filename, clone xml , 
# then replace filename in new xml with the respective filename.

import os
from PIL import Image
import sys
import glob
import string

list_path = []
path =     "D:/xrvision/0_new_images/PSA3/txt/low"
xml_path = "D:/xrvision/0_new_images/PSA3/xml/low/"
filepath = "D:/xrvision/0_new_images/PSA3/frame12099.xml" 

os.chdir(path) #the directory containing your .jpg
for file in glob.glob("*.jpg"): #iterates over all files in the directory ending in .jpg        
        f = open((xml_path + file.rsplit( ".", 1 )[ 0 ] ) + ".xml", "w") # write/create a new xml file
        
        f.write("<annotation>") #for some unknow reason this line is missing, had to replace manually
        f.write("\n") 
        
        # clone text for filepath source to clone
        with open(filepath) as fp:  
            line = fp.readline()
            cnt = 0
            while line:
                print("{}".format(line.strip()))
                line = fp.readline()  # after reading source xml
                
                # Find lines that need to change : str.replace(old, new[, max])
                newline = line.replace('frame1.jpg', file)

                #continue
                
                f.write(newline)  # now write into new xml
                cnt += 1      # iternate until end of line.
            
        f.close()

