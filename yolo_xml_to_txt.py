import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join, split
from glob import glob

#TO EDIT
xml_dirs = ['/Users/sunyitao/Documents/XRVision/PSA/extracted_images/xml/060VIDEO/', #needs to end with slashes
           '/Users/sunyitao/Documents/XRVision/PSA/extracted_images/xml/094VIDEO/',
            '/Users/sunyitao/Documents/XRVision/PSA/extracted_images/xml/low/', 
            '/Users/sunyitao/Documents/XRVision/PSA/extracted_images/xml/mid/', 
            '/Users/sunyitao/Documents/XRVision/PSA/extracted_images/xml/top/']

output_txt_dirs = ['/Users/sunyitao/Documents/XRVision/PSA/Yitao/yolo_txt/060VIDEO/',
                   '/Users/sunyitao/Documents/XRVision/PSA/Yitao/yolo_txt/094VIDEO/',
                   '/Users/sunyitao/Documents/XRVision/PSA/Yitao/yolo_txt/low/',
                   '/Users/sunyitao/Documents/XRVision/PSA/Yitao/yolo_txt/mid/',
                   '/Users/sunyitao/Documents/XRVision/PSA/Yitao/yolo_txt/top/']
classes = ['person', 'crane']
image_file_extension = '*jpg' #needs asterisk for glob
output_image_filenames_txt_file_dir = '/Users/sunyitao/darknet' #where to dump train.txt file containing list of image names


def convert(size, box): #size = width, height
    dw = 1./(size[0]) #1/width
    dh = 1./(size[1]) #1/height
    x = (box[0] + box[1])/2.0 - 1 #centre of xmin and xmax
    y = (box[2] + box[3])/2.0 - 1 #centre of ymin and ymax
    w = box[1] - box[0] #xmax - xmin = width for bounding box
    h = box[3] - box[2] #ymax - ymin = height for bounding box
    x = x*dw #centre of xmin and xmax/width
    w = w*dw #bounding box width/ image width
    y = y*dh #centre of ymin and ymax/height
    h = h*dh #bounding box height/ image height
    return (x,y,w,h)

def convert_annotation(i, xml_filename):
    in_file = open(join(xml_dirs[i], xml_filename))
    filename = split(xml_filename)[-1]
    out_file = open(join(output_txt_dirs[i], filename[:-4] + '.txt'), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'): #for each object in the image
        #difficult = obj.find('Difficult').text
        cls = obj.find('name').text
        if cls not in classes: #or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox') #contains xmin xmax ymin ymax tags
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b) #convert(size,box)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

    in_file.close()
    out_file.close()


for count, output_txt_dir in enumerate(output_txt_dirs):
    current_file = split(output_txt_dir[:-1])[-1]
    #comment out if images not present in output txt directory
    """
    image_filenames = sorted(glob(output_txt_dir + image_file_extension))
    list_file = open(join(output_image_filenames_txt_file_dir, current_file + '_train.txt'), 'w')
    for image_filename in image_filenames:
        list_file.write(join(output_txt_dir, image_filename) + '\n')
    list_file.close()
    """

    xml_filenames = sorted(glob(xml_dirs[count] + '*.xml'))
    for xml_filename in xml_filenames:
        convert_annotation(count, xml_filename)



