from os import listdir
from os.path import isfile, join
import cv2

root_folder_path = "E:\Projects\gsom\src/applications/adl_activity_accel\output".replace('\\', '/')
out_filename = "E:/Projects/gsom/src/applications/adl_activity_accel/output/ADL_classes_sf_0.5_T_3_mage_1000_3FPS.avi".replace('\\', '/')

if __name__ == '__main__':

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(out_filename, fourcc, 3, (1200, 1000))

    folders = [f for f in listdir(root_folder_path)]

    for idx, folder_path in enumerate(folders):

        if 'ADL_classes_sf_0.5_T_3_mage_1000' != folder_path:
            continue

        folder_path = join(root_folder_path, folder_path)
        files = sorted([f for f in listdir(folder_path) if isfile(join(folder_path, f))])

        print('video', idx+1)

        for f in files:

            if '.DS_Store' in f:
                continue

            f = folder_path + '/' + f
            im = cv2.imread(f)
            im = cv2.resize(im, (1200, 1000))

            frame = im  # cv2.flip(im, 0)
            out.write(frame)
            cv2.imshow('display', frame)
            cv2.waitKey(2)

        cv2.waitKey(0)

    out.release()
    cv2.destroyAllWindows()
