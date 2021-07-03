from posixpath import join
import cv2
import uuid
import os
import time
import subprocess

labels = ["thumbsup", "thumbsdown", "thankyou", "livelong"] # Name for the folder to be created

sample_size = 10 # How many images do we need

IMAGE_PATH = os.path.join("images","collected") #Path


currentdir = os.getcwd() # Current dir

joined = os.path.join( currentdir, IMAGE_PATH) # Joined path
cap = cv2.VideoCapture(0)

# print(joined)

if not os.path.exists(joined):
    os.makedirs(joined) # If images folder are not exists

for label in labels:
    # for each label new path and folders
    new_path = os.path.join(joined, label) 
    # print(new_path)
    if not os.path.exists(new_path):
        os.makedirs(new_path)


for img in range(sample_size):
    print(f"Image number {img}")
    success, frame = cap.read()
    imgname = os.path.join(joined, labels[3], labels[3]+'.'+'{}.jpg'.format(str(uuid.uuid1()))) #select the path and create unique named image names
    cv2.imwrite(imgname, frame) # write image
    cv2.imshow("frame", frame) # show the feed
    time.sleep(2)
        # time.sleep(3)

    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()