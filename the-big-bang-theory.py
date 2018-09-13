from os import listdir, rename
from os.path import isfile, join

# folder_name = 'C:/Users\pc\Desktop/Friends S06 720p BluRay x264 PaHe.in/'.replace('\\', '/')
folder_name = 'F:/TV Series/The Big Bang Theory/Season 6/'.replace('\\', '/')

"""
video: 01x02 - The Big Bran Hypothesis.avi
srt: The Big Bang Theory - 1x02 - The Big Bran Hypothesis.HDTV.XOR.en.srt
"""

if __name__ == '__main__':

    movie_files = [f for f in listdir(folder_name) if isfile(join(folder_name, f))]
    subs_files = [f for f in listdir(folder_name+'subs') if isfile(join(folder_name+'subs', f))]

    srt_dict = {}
    video_files = {}

    def get_sub_file_name(key):

        for file in subs_files:
            if key in file and 'HDTV' in file:
                return join(folder_name+'subs', file)


    # Get the video filename
    for file in movie_files:
        filename_components = file.split('.')
        if 'avi' in filename_components[-1]:

            # key = file.split(' ')[0]
            # key = key[1:]
            key = file.split(' -')[0].replace('The Big Bang Theory ', '')
            # key = key[:1] + 'x' + key[1:]

            sub_file_name = get_sub_file_name(key)
            print(sub_file_name, 'to', join(folder_name, file.replace('.avi', '.srt')))
            rename(sub_file_name, join(folder_name, file.replace('.avi', '.srt')))

    # Loop through the srt files and rename to video filename
    # for file in subs_files:
    #     filename_components = file.split('.')
    #     if 'srt' in filename_components[-1]:
    #         new_filename = ''.join(str(e) + '.' for e in filename_components[:4]) + ''.join(
    #             str(f) + '.' for f in video_file_name[4:]) + 'srt'
    #         rename(folder_name + file, folder_name + new_filename)
