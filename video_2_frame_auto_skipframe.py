import math
import numpy as np
import os
import glob
import cv2

i = 1
new_path = "C:/XRVISION/test_video/frames_extracted/"
os.chdir(new_path)

vid_path = "C:/XRVISION/test_video/test_video.avi"
vidcap = cv2.VideoCapture(vid_path)
success,image = vidcap.read()

fps = vidcap.get(cv2.CAP_PROP_FPS)
est_video_length_minutes = 164         # Round up if not sure.
est_tot_frames = est_video_length_minutes * 30 * fps  # Sets an upper bound # of frames in video clip

n = 120                             # Desired interval of frames to include
desired_frames = n * np.arange(est_tot_frames) 

for i in desired_frames:
    vidcap.set(1,i-1)                      
    success,image = vidcap.read(1)         # image is an array of array of [R,G,B] values
    frameId = vidcap.get(1)                # The 0th frame is often a throw-away
    cv2.imwrite("frame%d.jpg" % frameId, image)

vidcap.release()
print("Complete")







   

            