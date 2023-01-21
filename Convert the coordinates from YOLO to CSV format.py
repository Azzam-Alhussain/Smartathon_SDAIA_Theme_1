# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 22:05:30 2023

@author: Valeri
"""

import csv
import os
import numpy as np
import pandas as pd
import numpy as np
import cv2
import json

def find(ch,st): 
    indexes=[]
    index1=0
    while(True):
        if ch in st[index1:]:
            index2=st[index1:].index(ch)
            indexes.append(index1+index2)
            index1=index2+index1+1
        
        else:
            break
    return(indexes)

path="label_abd.zip"
height=1080
width=1920

classes = open("classes.txt","r").readlines()

txt_files=[]
for r,d,f in os.walk(path):
    for file in f:
        if ".txt" in file:
            txt_files.append(f"{r}/{file}")
    
converted_items=[]
for item in txt_files:
    txt=open(item,"r").readlines()
    for line in txt:
        line=line.split()
        sindex=find('/',item)[-1]+1
        converted_items.append([int(line[0]), f"{item[sindex:-4]}.jpg",classes[int(line[0])][:-1],
                         int(float(line[1])*width+(float(line[3])*width/2))//2,
                         int(float(line[1])*width-(float(line[3])*width/2))//2,
                         int(float(line[2])*height+(float(line[4])*height/2))//2,
                         int(float(line[2])*height-(float(line[4])*height/2))//2,
                         ])
        
with open('labels_withfactor.csv','w',newline='') as csvf:
    csvw=csv.writer(csvf)
    for item in converted_items:
        csvw.writerow(item)
        
        
with open('labels_nofactor.csv','w',newline='') as csvf:
    csvw=csv.writer(csvf)
    for item in converted_items:
        c,ip,cn,xmax,xmin,ymax,ymin=item
        w=xmax-xmin
        h=ymax-ymin
        wd=((48*w)/52)/2
        hd=((48*h)/52)/2
        xmaxn=xmax+wd
        xminn=xmin-wd
        ymaxn=ymax+hd
        yminn=ymin-hd
        csvw.writerow([c,ip,cn,int(xmaxn/2),int(xminn/2),int(ymaxn/2),int(yminn/2)])
        
        
