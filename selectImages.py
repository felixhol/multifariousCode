'''
Author: Felx Hol
Date: 2019
Code to pick a subset of images from a list of directories and save as PNGs
'''

import os
import glob
from PIL import Image
import numpy as np
# import pandas as pd

dirList = glob.glob('/mnt/DATA/bloodTaste/19*/M*/')

len(dirList)

saveDir = '/home/felix/biteOscope/aedesFrames/'

for i in dirList:
    os.chdir(i)
    fileList = glob.glob('*.tiff')
    if len(fileList) > 500 and len(fileList) < 5000:
        step = int(np.floor(len(fileList) / 5))   
        for j in range(1, len(fileList), step):
            im = Image.open(fileList[j])
            file, ext = os.path.splitext(fileList[j])
            im.save(saveDir + file + '.png', 'PNG')
    elif len(fileList) > 4999:
        step = int(np.floor(len(fileList) / 15))
        for j in range(1, len(fileList), step):
            im = Image.open(fileList[j])
            file, ext = os.path.splitext(fileList[j])
            im.save(saveDir + file + '.png', 'PNG')