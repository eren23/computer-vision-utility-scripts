from posixpath import join
import cv2
import cvlib as cv
import uuid
import os
import time
import subprocess

sample_size = 20 # How many images do we need

IMAGE_PATH = os.path.join("images","collected") #Path


currentdir = os.getcwd() # Current dir

joined = os.path.join( currentdir, IMAGE_PATH) # Joined path
cap = cv2.VideoCapture(0)

# print(joined)

if not os.path.exists(joined):
    os.makedirs(joined) # If images folder are not exists


new_path = os.path.join(joined, "faces") 
# print(new_path)
if not os.path.exists(new_path):
    os.makedirs(new_path)


for img in range(sample_size):
    print(f"Image number {img}")
    success, frame = cap.read()
    face, confidence = cv.detect_face(frame)
    for idx, f in enumerate(face):

        # get corner points of face rectangle        
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]

        # cut the face
        cropped = frame[f[1]:f[3], f[0]:f[2]]
        
        imgname = os.path.join(joined, "faces", "faces"+'.'+'{}.jpg'.format(str(uuid.uuid1()))) #select the path and create unique named image names
        
        # save and show the cropped face
        cv2.imwrite(imgname, cropped) # write image
        cv2.imshow("frame", cropped) # show the feed
        # time.sleep(3)

    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()