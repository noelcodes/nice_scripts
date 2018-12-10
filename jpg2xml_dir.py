# This script generates xml files from jpg.
# It assumes the whole iamge as the XY cooridinates.
# Put this script only 1 level outside the folder of images.
# The generated xml will be stored together with where the jpg is.

import os
from PIL import Image

path = "D:/xrvision/xrvision_dataset/CAR dataset/converted"

i = 0
for subdir, dirs, files in os.walk(path):
    for file in files:
        if 'jpg' in file[4:]:
            noel_path = (str(subdir) + "/" + str(file))
            print(file)
            print(noel_path)
            brand_name = (subdir[len(path)+1:])

    # do something
            f = open(( noel_path.rsplit( ".", 1 )[ 0 ] ) + ".xml", "w") #creates a new file using the .jpg filename, but with the .fsv extension
            f.write("<annotation>") #write to the text file
            f.write("\n")  
            f.write("    <folder>" + os.path.basename(path) + "</folder>") 	
            f.write("\n")        
            f.write("    <filename>" + file + "</filename>") 	
            f.write("\n")        
            f.write("    <path>" + os.path.join(path,file) + "</path>") 	
            f.write("\n")        
            f.write("    <source>\n<database>Unknown</database>\n    </source>") 	
            f.write("\n")  
            f.write("    <size>") 
            f.write("\n")  
            with Image.open(noel_path) as img:
                width, height = img.size
            f.write("        <width>" + str(width) + "</width>")     
            f.write("\n")
            f.write("        <height>" + str(height) + "</height>")
            f.write("\n")  
            f.write("        <depth>3</depth>") 
            f.write("\n")  
            f.write("    </size>") 
            f.write("\n")        
            f.write("    <segmented>0</segmented>") 	
            f.write("\n")        
            f.write("    <object>")
            f.write("\n")
            f.write("        <name>" + brand_name + "</name>")
            f.write("\n")		
            f.write("        <pose>Unspecified</pose>\n        <truncated>1</truncated>\
            \n        <difficult>0</difficult>") 
            f.write("\n")        
            f.write("        <bndbox>")
            f.write("\n")   
            f.write("            <xmin>0</xmin>") 
            f.write("\n")   
            f.write("            <ymin>0</ymin>")   
            f.write("\n")        
            f.write("            <xmax>" + str(width) + "</xmax>")     
            f.write("\n")
            f.write("            <ymax>" + str(height) + "</ymax>")
            f.write("\n") 
            f.write("        </bndbox>\n    </object>\n</annotation>") 
            f.close()
##    
    # done something

                   