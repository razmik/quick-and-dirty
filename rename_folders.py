from os import listdir, rename
from os.path import isfile, join, isdir

root_folder_path = "E:/Projects/image-feature-extractor/spatiotemporal_autoencoder/abnormal-spatiotemporal-ae/share/data/videos/ucsd_ped1/training_frames/".replace('\\', '/')

if __name__ == '__main__':

    folders = [f for f in listdir(root_folder_path)]

    for folder_path in folders:

        if '.DS_Store' in folder_path:
            continue

        current_folder_path = join(root_folder_path, folder_path)
        new_folder_path = join(root_folder_path, folder_path.split('Train0')[1])

        rename(join(root_folder_path, folder_path), new_folder_path)
