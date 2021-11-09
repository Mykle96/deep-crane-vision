import cv2
from tqdm import tqdm
import os
import shutil
import time


# Using the openCV library to extract frames from videos and save them has jpg images.

# ---- Paths -----
TRAINING_VIDEO_PATH = "../videos/training.mp4"
TEST_VIDEO_PATH = "../videos/test.mp4"
# ----------------

# ----- Frame restriction ------
"""
Leave this on if you want to restrict the amount of frames to be processed.
It will restrict it to 500 images. Turning this off will cause the function to
process the entire video.
"""
FRAME_RESTRICTION = True  # Change this to False to turn off.
# -------------------------------


# Change these parameteres for results
path = TRAINING_VIDEO_PATH
number_of_img_in_batch = 50


def amountOfFrames(source):
    total = int(source.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Amount of frames to be processed: ", total "\n")
    return total


def frameExtraction(path):
    loader()
    source = cv2.VideoCapture(path)
    answer = True
    frames = 500

    if path == TEST_VIDEO_PATH:
        storage_path = "./data/test"
        print("Storage path: ", storage_path)
    elif path == TRAINING_VIDEO_PATH:
        storage_path = "./data/training"
        print("Storage path: ", storage_path)
    else:
        print("NB! Path unrecognized")

    if source.isOpened():
        print("Source is open")
    else:
        print("An error has occured: Can't read the frame")

    total_frames = amountOfFrames(source)

    if not FRAME_RESTRICTION:
        while answer:
            prompt = input(
                "You have deactivated frame restriction, are you sure? (y/n)")
            if prompt == ("n"):
                print("FRAME RESTRICTION IS ACTIVATED")
                print("Processing 500 frames \n")
                frameRestrictor(source, frames, storage_path)
                break
            elif prompt == ("y"):
                print("FRAME RESTRICTION IS DEACTIVATED")
                print("Processing ALL frames \n")
                frameRestrictor(source, total_frames, storage_path)
                break
    else:
        print("FRAME RESTRICTION IS ACTIVATED")
        print("Processing 500 frames \n")
        frameRestrictor(source, frames, storage_path)

    return storage_path


def frameRestrictor(source, frames, storage_path):

    for frame in tqdm(range(frames)):  # Extracting frames
        success, image = source.read()
        cv2.imwrite(
            (os.path.join(storage_path, "image"+str(frame)+".jpg")), image)
        if not success:
            print("Process complete")
            source.release()


def loader():
    print("=" * 25)
    print("Frame extractor starting")
    print("=" * 25)


frameExtraction(path)
# def make_batches(number_of_img_in_batch, storage_path):
#    destination = storage_path + ""
