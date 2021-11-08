import cv2
from tqdm import tqdm
import os
import shutil
import time


# Using the openCV library to extract frames from videos and save them has jpg images.

# ---- Paths -----
# Change the paths to fit to where your data lies in your local repository
TRAINING_VIDEO_PATH = "../videos/training.mp4"
TEST_VIDEO_PATH = "../videos/test.mp4"
# ----------------

# Change these parameteres for results
path = TRAINING_VIDEO_PATH
number_of_img_in_batch = 50


def amountOfFrames(source):
    total = int(source.get(cv2.CAP_PROP_FRAME_COUNT))
    return total


def frameExtraction(path):
    loader()
    source = cv2.VideoCapture(path)
    complete = True
    image_path = "img"

    if path == TEST_VIDEO_PATH:
        storage_path = "./data/test"
    elif path == TRAINING_VIDEO_PATH:
        storage_path = "./data/training"
    else:
        print("NB! Path unrecognized")

    if source.isOpened():
        print("Source is open")
        frame_index = 0
        img_index = 0
    else:
        print("An error has occured: Can't read the frame")

    total_frames = amountOfFrames(source)
    print("Amount of frames to be processed: ", total_frames)
    print("Storage path: ", storage_path)

    """
    while complete:
        ret, frame = source.read()
        print(ret)
        if ret:
            name = storage_path+str(frame_index)+'.jpg'
            print(f"Creating file ... {name}")
            cv2.imwrite(name, frame)
            cv2.imshow('frame', frame)
        frame_index += 1
        if frame_index == total_frames - 1:
            complete = False
    source.release()
    """

    for frame in tqdm(range(10)):
        success, image = source.read()
        cv2.imwrite((os.path.join(storage_path, str(frame)+".jpg")), image)
        if not success:
            source.release()
            print("Process complete")

    return storage_path


def loader():
    print("=" * 25)
    print("Frame extractor starting")
    print("=" * 25)


frameExtraction(path)
# def make_batches(number_of_img_in_batch, storage_path):
#    destination = storage_path + ""
