import cv2
import time
from os import mkdir
import win32gui,win32con 

try :
    mkdir('footage')
except FileExistsError:
    pass

def minimizeWindow():
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window, win32con.SW_MINIMIZE)

def cctv():
    video = cv2.VideoCapture(0)
    video.set(3,640)
    video.set(4,480)
    width = video.get(3)
    height = video.get(4)
    print("The video resolution is ",width," x ",height)
    print("Help-- \n1.Press esc to exit. \n2.Press m to minimize.")
    fourcc = cv2.videoWriter_fourcc(*'XVID')
    date_time = time.strftime(" recording %H-%M-%d -%m -%y ")
    output = cv2.VideoWriter('footages/'+date_time+' .mp4',fourcc,20.0,(640,480))

    while video.isOpened():
        check , frame = video.read()
        if check:
          frame = cv2.flip(frame,1)

          t = time.ctime()
          cv2.rectangle(frame, (5, 5, 100, 20), (255, 255, 255), cv2.FILLED)
          cv2.putText(frame, "Camera 1", (20, 20),
                        cv2.FONT_HERSHEY_DUPLEX, 0.5, (5, 5, 5), 2)
          cv2.putText(frame, t, (420, 460),
                        cv2.FONT_HERSHEY_DUPLEX, 0.5, (5, 5, 5), 1)
    
          cv2.imshow('CCTV camera', frame)
          output.write(frame)

          # Close window when user presses the ESC key
          if cv2.waitKey(1) == 27:
            print("Video footage saved in current directory.\n Be safe & Secure")
            break
          # Call minimizeWindow method when user presses 'm'
          elif cv2.waitKey(1) == ord('m'):
            minimizeWindow()
        else:
           print("Can't open this camera. Select another or check its configuration.")
           break
        video.release()
        output.release()
        cv2.destroyAllWindows()

    print("*" * 80 + "\n" + " " * 30 + "Welcome to CCTV software\n" + "*" * 80)
    ask = int(input('Do you want to start CCTV?\n1. Yes\n2. No\n>>> '))
    if ask == 1:
      cctv()
    elif ask == 2:
      print("Bye bye! Be safe & secure!")
    exit



    
