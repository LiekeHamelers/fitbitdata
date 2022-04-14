#%% -  import packages and set variables
import pandas as pd
import numpy as np
import glob
import os

variable = 'distance'
jsonpath = "C:/Users/lieke/OneDrive/Documents/Programmeren/fitbitdata/LiekeHamelers/Physical Activity/"

#%% - Read data
file_list = glob.glob(jsonpath + variable + '*.json')
df = pd.DataFrame()
for file in file_list:
    ent = pd.read_json(file)
    #print(ent)
    if df.empty: 
        df = ent
    else: 
        df = pd.concat([df, ent], axis = 0)

