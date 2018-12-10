# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:54:08 2018

@author: Noel Tam
"""

import numpy as np
from skimage.io import imread
from keras.applications.imagenet_utils import decode_predictions

from classification_models import *
from classification_models import preprocess_input

# read and prepare image
x = imread('./rubbish.jpg')
x = preprocess_input(x, size=(224,224))
x = np.expand_dims(x, 0)

# load model
model = ResNet18(input_shape=(224,224,3), weights='imagenet', classes=1000)

# processing image
y = model.predict(x)

# result
print(decode_predictions(y))