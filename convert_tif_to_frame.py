import os
from os import listdir
from os.path import isdir, isfile, join
from PIL import Image


video_root_path = 'E:/Data/UCSD_Anomaly_Dataset/UCSD_Anomaly_Dataset.v1p2'
frame_root_path = 'share/data/videos'
size = (224, 224)


def video_to_frame(dataset, train_or_test):
    video_path = join(video_root_path, dataset, '{}'.format(train_or_test))
    frame_path = join(frame_root_path, dataset, '{}_frames'.format(train_or_test))
    os.makedirs(frame_path, exist_ok=True)

    video_file_folders = [f for f in listdir(video_path) if isdir(join(video_path, f))]

    for video_folder in video_file_folders:

        outfolder = join(frame_path, video_folder)
        os.makedirs(outfolder, exist_ok=True)

        for tiff_filename in [f for f in listdir(join(video_path, video_folder)) if isfile(join(join(video_path, video_folder), f))]:

            if '.DS_Store' in tiff_filename:
                continue

            outfile = join(outfolder, os.path.basename(tiff_filename).split('.')[0]) + '.jpg'

            image = Image.open(os.path.join(join(video_path, video_folder), tiff_filename))
            image = image.convert("RGB")
            image = image.resize(size, Image.ANTIALIAS)
            image.save(outfile, "JPEG", quality=100)

        print('completed', outfolder)


if __name__ == "__main__":

    # ped1
    video_to_frame('UCSDped1', 'training')
    video_to_frame('UCSDped1', 'testing')