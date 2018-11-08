from os import listdir
from os.path import isfile, join, isdir
import cv2

root_folder_path = "E:\Data\Vollyball_data/all".replace('\\', '/')
out_filename = "E:\Data\Vollyball_data/vollyball.avi".replace('\\', '/')

resolution = (1280, 720)

if __name__ == '__main__':

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(out_filename, fourcc, 28, resolution)

    files = sorted([f for f in listdir(root_folder_path) if isfile(join(root_folder_path, f))])

    for f in files:

        f = join(root_folder_path, f)
        im = cv2.imread(f)
        im = cv2.resize(im, resolution)

        frame = im
        out.write(frame)
        cv2.imshow('display', frame)
        cv2.waitKey(2)

    cv2.waitKey(0)

    out.release()
    cv2.destroyAllWindows()
