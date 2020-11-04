'''
Author: Felix Hol
Date: Nov 4 2020
Code to copy all images (e.g. .tiff files) in a directory to another directory and convert to PNG. 
'''

import os
import glob
import cv2 as cv
from joblib import Parallel, delayed
import multiprocessing
from tqdm import tnrange, tqdm
import time

source = '/media/SOURCE_DIR/'
dest = '/home/DESTINATION_DIR/'

num_cores = multiprocessing.cpu_count()
# num_cores = 12

fileList = glob.glob(source + '/*/*.tiff')

print('copying ' + str(len(fileList)) + 'images to ' + dest)

time.sleep(2)

def copyToPNG(f):
    im = cv.imread(f, -1)
    imName = os.path.splitext(os.path.basename(f))[0]
    imDir = os.path.split(os.path.dirname(f))[1]
    newName = dest + imDir + '/' + imName + '.png'
    os.makedirs(os.path.dirname(newName), exist_ok=True)
    cv.imwrite(newName, im, [cv.IMWRITE_PNG_COMPRESSION, 2])   

_=Parallel(n_jobs=num_cores)(delayed(copyToPNG)(i) for i in tqdm(fileList))
