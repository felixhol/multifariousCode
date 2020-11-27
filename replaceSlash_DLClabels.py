'''
author: Felix Hol
date: 2020 Nov
Replace Windows slash to linux slash in DLC labeled dataset (convenient if only part of the
dataset was labeled on windows).
'''

import numpy as np
import pandas as pd
import os
import glob

fileList = glob.glob('/Users/felix/Dropbox/aedes-bbb-2020-11-16_Fe/Invitation_labelled_frames/*/CollectedData_bbb.h5')

for f in fileList:
    df = pd.read_hdf(f)
    os.remove(f)
    df.index = df.index.str.replace(r'\\', '/', regex=True)
    df.to_hdf(f, key="df_with_missing", mode="w")
