# This script crops an image according to xml bounding box, then skrink 
# to percentage 10%, then multiply and populate a blank image (size ideally same as webcam),
# then save as a new file, then creates a new xml of many bounding box of the new file.
# XML label is the base folder name itself.

from __future__ import print_function
import numpy as np
import glob
import cv2
import os
from PIL import Image
import mmap

########################################
path = "C:/PSA/robust6/txt"
os.chdir(path)

        
i = 1
g = 1
for ori_file in glob.glob("*.jpg"):
    
    xml_file = (ori_file[:-4]+".xml")
    with open(xml_file,'r') as f:
        data=''.join(f.readlines())
        
        xmin = int(float(data[data.index('<xmin>')+6:data.index('</xmin>')]))
        xmax = int(float(data[data.index('<xmax>')+6:data.index('</xmax>')]))
        ymin = int(float(data[data.index('<ymin>')+6:data.index('</ymin>')]))
        ymax = int(float(data[data.index('<ymax>')+6:data.index('</ymax>')]))
        
        
    img = Image.open(ori_file)
    area = (xmin, ymin, xmax, ymax)
    cropped_img = img.crop(area)

## resize original    
    percent = 1  # resize in percent 0 - 1 (1=no change)
    new_image = cropped_img.resize( [int(percent * s) for s in cropped_img.size] )    
   
    # image orignal size
    #width, height = image.size
# custom size
    width = 1920
    height = 1080
    blank_img = Image.new('RGB', (width, height), (255, 255, 255))

    for w in range(0, int(blank_img.width/new_image.width)+1):
        for h in range(0, int(blank_img.height/new_image.height)+1):
            position = ((blank_img.width - (new_image.width)*w) , (blank_img.height - (new_image.height)*h ))
            blank_img.paste(new_image, position)

    new_file = ori_file[:-4] + "_" + str(g) + ".jpg"
    blank_img.save(new_file)
# looking for xmin, xmax, ymin, ymax
    
    
    f = open(( new_file.rsplit( ".", 1 )[ 0 ] ) + ".xml", "w") #creates a new file using the .jpg filename, but with the .fsv extension
    f.write("<annotation>") #write to the text file
    f.write("\n")  
    f.write("<folder>" + os.path.basename(path) + "</folder>") 	
    f.write("\n")        
    f.write("<filename>" + new_file + "</filename>") 	
    f.write("\n")        
    f.write("<path>" + os.path.join(path,new_file) + "</path>") 	
    f.write("\n")        
    f.write("<source>\n<database>Unknown</database>\n</source>") 	
    f.write("\n")  
    f.write("<size>") 
    f.write("\n")  
    with Image.open(new_file) as img_xml:
        width, height = img_xml.size
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



    for w in range(1, int(blank_img.width/new_image.width)+1):
        for h in range(1, int(blank_img.height/new_image.height)+1):
            position = ((blank_img.width - (new_image.width)*w) , (blank_img.height - (new_image.height)*h ))
            
            new_xmin = (blank_img.width - (new_image.width)*w)
            new_ymin = (blank_img.height - (new_image.height)*h )
            new_xmax = new_xmin + new_image.width
            new_ymax = new_ymin + new_image.height
            
            f.write("<object>")
            f.write("\n")
            f.write("<name>" + os.path.basename(path) + "</name>")
            f.write("\n")		
            f.write("<pose>Unspecified</pose>\n<truncated>0</truncated>\
            \n<difficult>0</difficult>") 
            f.write("\n")        
            f.write("<bndbox>")
            f.write("\n")   
            f.write("<xmin>" + str(new_xmin) + "</xmin>") 
            f.write("\n")   
            f.write("<ymin>" + str(new_ymin) + "</ymin>") 
            f.write("\n")        
            f.write("<xmax>" + str(new_xmax) + "</xmax>")     
            f.write("\n")
            f.write("<ymax>" + str(new_ymax) + "</ymax>")
            f.write("\n") 
            f.write("</bndbox>\n</object>\n") 
    f.write("</annotation>") 
    f.close()


    

