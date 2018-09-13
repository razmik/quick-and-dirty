import pandas as pd
import h5py
import os
import time

# Create save path if not exist
data_path = 'data'

# Read dataset
filename = os.path.join(data_path, 'rec1487594667.hdf5')
hf = h5py.File(filename, 'r')

# Get all groups keys
primary_keys = list(hf.keys())
secondary_keys = list(hf.get(primary_keys[0]).keys())

# Loop through all the root objects
for primary_key in primary_keys:

    if primary_key == 'dvs':
        print('dvs')
    else:
        continue

    start_time = time.time()

    data = hf.get(primary_key)[secondary_keys[0]][()]

    print('type', type(data))
    print('len', len(data))
    print('shape', data.shape)

    # timestamps = hf.get(primary_key)[secondary_keys[1]][()]
    #
    # df = pd.DataFrame(data)
    # df['timestamp'] = timestamps.tolist()
    #
    # end_time = time.time()
    #
    # df.to_csv(os.path.join(data_path, primary_key + '_data.csv'), index=None)
    # print(primary_key, 'completed in', round(end_time - start_time, 4), 's')
