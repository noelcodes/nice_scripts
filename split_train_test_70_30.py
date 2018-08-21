# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 14:55:23 2018

@author: default
"""

import os
from sklearn.cross_validation import train_test_split

path = os.getcwd()
folders = []
folders = ['train','test']
for folder in folders:
    os.mkdir(os.path.join(path,folder))

X = y= os.listdir(path)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

for x in X_train:
    if x.endswith('.jpg'):
        os.rename(path + '/'+x , path + '/train/'+x)

for x in X_test:
    if x.endswith('.jpg'):
        os.rename(path + '/'+x , path + '/test/'+x)


