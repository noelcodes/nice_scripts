import win32api
import numpy as np
import cv2
import os
import msvcrt

def vid2frame(vidcap, vid_lst):
    count = 0 
    speed = 200

    while(vidcap.isOpened()):
    
        ret, frame = vidcap.read()
        a = win32api.GetKeyState(0x01)
        
        if msvcrt.kbhit():
            key = msvcrt.getch()
            speed = speed_control(speed,key)

        if ret==True and a < 0:
            cv2.imwrite(main_path + "/" + vid_lst + "/" + "frame%d.jpg" % count, frame)     # save frame as JPEG file      
            print(vid_lst + "/" + "frame%d.jpg" % count)
            count += 1
            cv2.imshow('frame',frame)
            
            if cv2.waitKey(speed) & 0xFF == ord('q'): 
                break
        
        elif ret==True and a >= 0:
            cv2.imshow('frame',frame)
            if cv2.waitKey(speed) & 0xFF == ord('q'): 
                break       
        else:
            break
    
    vidcap.release()
    cv2.destroyAllWindows()


def getvideoname(path):
    list_path = []
    for subdir, dirs, files in os.walk(path):
        for file in files:
            #print os.path.join(subdir, file)
            #filepath = subdir + '/' + file
            filepath = file
    
            if filepath.endswith(".avi"):
                list_path.append(filepath)
                #print(list_path)
    return list_path

def ensure_dir(directory):
    directory = directory[:-4]
    if not os.path.exists(directory):
        os.makedirs(directory)

def exe_vid2frame():
    for vid_name in getvideoname(main_path):
        ensure_dir(vid_name)
        video = cv2.VideoCapture(vid_name)
        vid2frame(video, vid_name[:-4])

def ask_path():
    print("Enter the path that contains the video file.")
    print("Default is : %s" %os.getcwd())
    print("Press 'Enter' to use default, else enter new path below:")
    main_path = input()
    if main_path == "":
        print("use default")
        main_path = os.getcwd()
    else:
        print("New video path is : %s" %main_path)
    return main_path

def speed_control(speed_now, keycode):
        if keycode == 80: #Down arrow
            print("slow down = %s" %speed_now)
            speed_now = speed_now * 2
        elif keycode == 72: #Up arrow
            print("speed up = %s" %speed_now)
            speed_now = speed_now / 2
        elif keycode == 13: #Enter=pause
            os.system("pause")

        else:
            
            return speed_now
        return speed_now


main_path = ask_path()
exe_vid2frame()





