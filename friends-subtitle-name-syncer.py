from os import listdir, rename
from os.path import isfile, join

# folder_name = 'C:/Users\pc\Desktop/Friends S06 720p BluRay x264 PaHe.in/'.replace('\\', '/')
folder_name = 'H:\TV Series\Friends Season 1-10 COMPLETE 720p BrRip x264 [PAHE.in]\Friends S10 720p BluRay x264 PaHe.in/'.replace('\\', '/')

"""
video: Friends.S03E02.720p.BluRay.x264.195MB-PAHE.in.mkv
srt: Friends.S03E02.720p.BluRay.x264-PSYCHD.srt
"""

if __name__ == '__main__':

    files = [f for f in listdir(folder_name) if isfile(join(folder_name, f))]

    srt_dict = {}
    video_file_name = ''

    # Get the video filename
    for file in files:
        filename_components = file.split('.')
        if 'mkv' in filename_components[-1]:
            video_file_name = filename_components[:-1]
            break

    # Loop through the srt files and rename to video filename
    for file in files:
        filename_components = file.split('.')
        if 'srt' in filename_components[-1]:
            new_filename = ''.join(str(e) + '.' for e in filename_components[:4]) + ''.join(
                str(f) + '.' for f in video_file_name[4:]) + 'srt'
            rename(folder_name + file, folder_name + new_filename)
