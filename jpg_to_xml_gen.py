# This code generates XML from Jpg.
# It assumes bbox is the whole image.
# Put script in the same folder as images.

import os
from PIL import Image

list_path = []
path = "D:/xrvision/5_noelcodes/trycodes"

   
import glob
import os
os.chdir(path) #the directory containing your .jpg
for file in glob.glob("*.jpg"): #iterates over all files in the directory ending in .jpg        
        f = open(( file.rsplit( ".", 1 )[ 0 ] ) + ".xml", "w") #creates a new file using the .jpg filename, but with the .fsv extension
        f.write("<annotation>") #write to the text file
        f.write("\n")  
        f.write("<folder>" + os.path.basename(path) + "</folder>") 	
        f.write("\n")        
        f.write("<filename>" + file + "</filename>") 	
        f.write("\n")        
        f.write("<path>" + os.path.join(path,file) + "</path>") 	
        f.write("\n")        
        f.write("</source>\n<database>Unknown</database>\n</source>") 	
        f.write("\n")  
        f.write("<size>") 
        f.write("\n")  
        with Image.open(file) as img:
            width, height = img.size
        f.write("<width>" + str(width) + "</width>")     
        f.write("\n")
        f.write("<height>" + str(height) + "</height>")
        f.write("\n")  
        f.write("<depth>3</depth>") 
        f.write("\n")  
        f.write("</size>") 
        f.write("\n")        
        f.write("<segmented>0</segmented>") 	
        f.write("\n")        
        f.write("<object>")
        f.write("\n")
        f.write("<name>" + os.path.basename(path) + "</name>")
        f.write("\n")		
        f.write("<pose>Unspecified</pose>\n<truncated>0</truncated>\
        \n<difficult>0</difficult>") 
        f.write("\n")        
        f.write("<bndbox>")
        f.write("\n")   
        f.write("<xmin>0</xmin>") 
        f.write("\n")   
        f.write("<ymin>0</ymin>")   
        f.write("\n")        
        f.write("<xmax>" + str(width) + "</xmax>")     
        f.write("\n")
        f.write("<ymax>" + str(height) + "</ymax>")
        f.write("\n") 
        f.write("</bndbox>\n</object>\n</annotation>") 
        f.close()









