# importing necessary packages
from imutils.video import VideoStream
import imutils
import numpy as np
import argparse
import time
import cv2

# construct the arguments parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--videopath", required=True, help="path of the video file")
args = vars(ap.parse_args())



print("[INFO] starting video stream, please wait...")
vs = VideoStream(src=0).start()
time.sleep(3)

while True:
   
    frame = vs.read()
    frame = imutils.resize(frame, width=1000, height=1000)  #resizeing the image size


    #machine learning model function here 
    


    # show the output frame
    cv2.imshow("Face detector from camera stream", frame)

    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    
cv2.destroyAllWindows()
vs.stop()
