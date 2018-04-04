import pandas as pd
import h5py
import os
import time

# Create save path if not exist
data_path = 'data'

# Read dataset
filename = os.path.join(data_path, 'ucsd_ped1_01.h5')
hf = h5py.File(filename, 'r')

# Get all groups keys
primary_keys = list(hf.keys())

# Loop through all the root objects
for primary_key in primary_keys:
    start_time = time.time()

    data = hf.get(primary_key)[()]

    print(primary_key, data.shape)
