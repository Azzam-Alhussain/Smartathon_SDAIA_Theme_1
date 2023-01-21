# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 03:17:53 2023

@author: Valeri
"""

import cv2
import numpy as np
import csv
import pandas as pd
import os


train_file=pd.read_csv("train_1.csv")
#test_file=pd.read_csv("dataset/test.csv")

if "train" not in os.listdir("."):
    os.mkdir("train")

if "train/labels" not in os.listdir("."):
    os.mkdir("train/labels")
    
classes = train_file['name'].unique()
classes_id={}
r=2
rr=0.24

train_data={}
for index,item in enumerate(train_file['image_path']):
    classes_id[int(train_file['class'][index])]=train_file['name'][index]
    xmax=train_file['xmax'][index]
    xmin=train_file['xmin'][index]
    ymax=train_file['ymax'][index]
    ymin=train_file['ymin'][index]
    name=train_file['name'][index]
    w=xmax-xmin
    h=ymax-ymin
    if item not in train_data:
      train_data[item]=[]
      
    train_data[item].append([train_file['class'][index], int((xmin+w*rr)*r), int((ymin+h*rr)*r), int((xmax-w*rr)*r), int((ymax-h*rr)*r)])

"""
test_data={}
for index,item in enumerate(test_file['image_path']):
    
    xmax=test_file['xmax'][index]
    xmin=test_file['xmin'][index]
    ymax=test_file['ymax'][index]
    ymin=test_file['ymin'][index]
    name=test_file['name'][index]
    w=xmax-xmin
    h=ymax-ymin
    if item not in test_data:
      test_data[item]=[]
      
    test_data[item].append([test_file['class'][index], int((xmin+w*rr)*r), int((ymin+h*rr)*r), int((xmax-w*rr)*r), int((ymax-h*rr)*r)])
"""   

for item_name in train_data:
    #img=cv2.imread(f"dataset/images/{item_name}")
    H,W,_= (1080,1920,3)
    with open(f"train/labels/{item_name[:-4]}.txt","w") as f:
        for item in train_data[item_name]:
            L=["{} {} {} {} {}\n".format(int(item[0]), round(((item[1]+item[3])/2)/W,6), round(((item[2]+item[4])/2)/H,6), round(((item[3]-item[1]))/W,6), round(((item[4]-item[2]))/H,6))]
            f.writelines(L)
"""        
for item_name in test_data:
    img=cv2.imread(f"dataset/images/{item_name}")
    H,W,_=img.shape
    with open(f"test/labels/{item_name[:-4]}.txt","w") as f:
        for item in test_data[item_name]:
            #f.write(f"{int(item[0])} {((item[1]+item[3])/2)/W} {((item[2]+item[4])/2)/H} {((item[3]-item[1]))/W} {((item[4]-item[2]))/H}")
            #f.write('\n')
            L=["{} {} {} {} {}\n".format(int(item[0]), round(((item[1]+item[3])/2)/W,6), round(((item[2]+item[4])/2)/H,6), round(((item[3]-item[1]))/W,6), round(((item[4]-item[2]))/H,6))]
            f.writelines(L)
"""
            
with open("train/labels/classes.txt","w") as f:
    for i in range(len(classes_id)):
        f.write(classes_id[i])
        f.write('\n')
"""        
with open("test/labels/classes.txt","w") as f:
    for i in range(len(classes_id)):
        f.write(classes_id[i])
        f.write('\n')
"""
