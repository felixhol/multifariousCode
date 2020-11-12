'''
Author: Felix Hol
Date: Nov 12 2020
Code to create a square number of crops (e.g. 2x2, 3x3) of all images (e.g. .png files) in a directory and save 
crops to another directory. 
'''

import os
import glob
import numpy as np
import cv2 as cv


dirList = glob.glob('/Users/felix/biteOscope/aedes-bbb-2020-11-10/invitationFrames/')
saveDir = '/Users/felix/biteOscope/aedes-bbb-2020-11-10/invitationCrops/'
nCrop = 2 ### crops in 1 dimension, will produce nCrop ^ 2 crops

print('cropping data from ' + str(len(dirList)) + 'directories to ' + saveDir + '. Creating ' + str(nCrop*nCrop) + ' crops per image.')


for i in dirList:
    os.chdir(i)
    fileList = glob.glob('*.png')
    im0 = cv.imread(fileList[0], -1)
    imSize = np.shape(im0)
    cropSize = int(imSize[0] / nCrop) - nCrop
    for j in range(1, len(fileList)):
        im = cv.imread(fileList[j], -1)
        file, ext = os.path.splitext(fileList[j])
        N = 0
        for k in range(0, nCrop):
            for l in range(0, nCrop):
                crop = im[k * cropSize : (k + 1) * cropSize, l * cropSize : (l + 1) * cropSize]
                imName = saveDir + file + '_crop' + '%03d' % N + '.png'
                cv.imwrite(imName, crop)
                N +=1 