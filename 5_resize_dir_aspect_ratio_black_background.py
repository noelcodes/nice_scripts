# This script works
# resize to thumbmail size yet maintains aspect ratio
# the remaining background as black
# Optional to turn resulted image to Grayscale.
from scipy.misc import imread
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import scipy

def grayscale(picture):
    res=Image.new(picture.mode, picture.size)
    width, height = picture.size

    for i in range(0, width):
        for j in range(0, height):
            pixel=picture.getpixel((i,j))
            avg=(pixel[0]+pixel[1]+pixel[2])//3
            res.putpixel((i,j),(avg,avg,avg))
    return res
            
            
def black_background_thumbnail(path_to_image, thumbnail_size=(400,400)):
    background = Image.new('RGB', thumbnail_size, "black")    
    source_image = Image.open(path_to_image).convert("RGB")
    source_image.thumbnail(thumbnail_size)
    (w, h) = source_image.size
    background.paste(source_image, ((thumbnail_size[0] - w) // 2, (thumbnail_size[1] - h) // 2 ))
#    background = grayscale(background)  # turn RGB to Grayscale
    return background

path = "D:/xrvision/5_noelcodes/temp"
os.chdir(path)


for subdirs, dirs, files in os.walk(path):
    for file in files:
        img_path = subdirs + "/" + file
        print(img_path)
        img = black_background_thumbnail(img_path)
        img.save(img_path)
        image = imread(img_path, 0)
        print(image.shape)
        image = np.average(image, axis=-1)
        print(image.shape)
        scipy.misc.imsave(img_path, image)


#        plt.imshow(image)
#        plt.show()

os.chdir(path)  


