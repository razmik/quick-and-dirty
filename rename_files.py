from os import listdir, rename
from os.path import isfile, join

root_folder_path = "G:/Other/driving_videos/video_imgs_3/".replace('\\', '/')

if __name__ == '__main__':

    folders = [f for f in listdir(root_folder_path)]

    for idx, folder_path in enumerate(folders):

        if '.DS_Store' in folder_path:
            continue

        folder_path = root_folder_path + folder_path
        files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

        print('video', idx+1)

        for f in files:

            if '.DS_Store' in f:
                continue

            fid = f.split('frame_')[1].split('.')[0]
            if len(fid) < 4:
                fid = '0'+fid

                filename = folder_path + '/' + f
                new_filename = folder_path + '/' + f.split('frame_')[0] + 'frame_' + fid + '.jpg'
                rename(filename, new_filename)