import pandas as pd
import shutil
import os
from os import listdir
from os.path import isfile, join

gtfile = 'C:/Users/pc/Desktop/JunctionDS/ground_truth.csv'
gt_train_file = 'C:/Users/pc/Desktop/JunctionDS/train_clips.csv'
all_image_folder = 'E:/Projects/image-feature-extractor/autoencoder/spatiotemporal_autoencoder/abnormal-spatiotemporal-ae/share/data/videos/junction/training_frames/traffic-junction'
train_folder = 'E:/Data/Anomaly_Dataset/traffic_juction/training'
test_folder = 'E:/Data/Anomaly_Dataset/traffic_juction/testing'

# gt_df = pd.read_csv(gtfile)
#
# for index, row in gt_df.iterrows():
#
#     directory = join(test_folder, '{:02d}'.format(index+1))
#     if not os.path.exists(directory):
#         oldmask = os.umask(000)
#         os.makedirs(directory, 0o0777)
#         os.umask(oldmask)
#
#     start_id = row['frame_start']
#     end_id = row['frame_end']
#
#     for i in range(start_id, end_id+1, 1):
#
#         fname = '{:05d}.jpg'.format(i)
#
#         src = join(all_image_folder, fname)
#         dst = directory
#         # shutil.copy(src, dst)
#
#     print('Created', directory)

print('Creating train directory')
gt_train_df = pd.read_csv(gt_train_file)

for index, row in gt_train_df.iterrows():

    directory = join(train_folder, '{:02d}'.format(index+1))
    if not os.path.exists(directory):
        oldmask = os.umask(000)
        os.makedirs(directory, 0o0777)
        os.umask(oldmask)

    start_id = row['frame_start']
    end_id = row['frame_end']

    for i in range(start_id, end_id+1, 1):

        fname = '{:05d}.jpg'.format(i)

        src = join(all_image_folder, fname)
        dst = directory
        shutil.copy(src, dst)

    print('Created', directory)

