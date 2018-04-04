from os import listdir
from os.path import isfile, join
import cv2

# root_folder_path = "E:\Data/UCSD_Anomaly_Dataset/UCSD_Anomaly_Dataset.v1p2/UCSDped1\Train/".replace('\\', '/')
root_folder_path = "E:\Data/UCSD_Anomaly_Dataset/UCSD_Anomaly_Dataset.v1p2/UCSDped1/testing/".replace('\\', '/')

if __name__ == '__main__':

    folders = [f for f in listdir(root_folder_path)]

    for idx, folder_path in enumerate(folders):

        if '.DS_Store' in folder_path:
            continue

        # if folder_path != 'Test033':
        #     continue

        folder_path = root_folder_path + folder_path
        files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

        print('video', idx+1)

        for f in files:

            if '.DS_Store' in f:
                continue

            f = folder_path + '/' + f
            im = cv2.imread(f)  # read image in greyscale

            cv2.imshow('display', im)
            cv2.waitKey(2)

        cv2.waitKey(0)

    cv2.destroyAllWindows()
