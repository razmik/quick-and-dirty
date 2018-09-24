import cv2


if __name__ == '__main__':

    filename = 'E:/Data/Anomaly_Dataset/ped1/testing_videos/01.avi'

    video = cv2.VideoCapture(0)

    fps = video.get(cv2.CAP_PROP_FPS)
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    count = video.get(cv2.CAP_PROP_FRAME_COUNT)

    print(fps, width, height, count)