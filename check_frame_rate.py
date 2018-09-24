import cv2


if __name__ == '__main__':

    filename = 'E:/Data/Anomaly_Dataset/avenue/testing_videos/01.avi'

    video = cv2.VideoCapture(0)

    fps = video.get(cv2.CAP_PROP_FPS)

    print(fps)