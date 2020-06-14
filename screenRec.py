from time import sleep
import cv2
import numpy as np
from mss import mss
import sys, os
import argparse


# Command line part
parser = argparse.ArgumentParser(description="ScreenRec v.1.5.0",
                                 epilog="A program by Karthikeshwar")
parser.add_argument(
    '-vn', "--videoname", type=str, default="Screen_record", help="Name of the screen record video to be saved"
)
parser.add_argument(
    '-in', "--imagename", type=str, default="Image", help="Name of the screen record video to be saved"
)
parser.add_argument(
    '-s', "--sleep", type=int, help="start recording after 'sleep' seconds"
)
parser.add_argument(
    '-fhd', "--fullhd", help="Start with resolution 1920x1080 (default : 1366x768)", action="store_true"
)
parser.add_argument(
    '-sc', "--silentcapture", help="Capture screen silently without opening the GUI", action="store_true"
)
args = parser.parse_args()


# if you want it to start little late
if args.sleep:
    sleep(args.sleep)


# Folders for storing images/videos
if not os.path.isdir("Images"):
    os.mkdir("Images")

if not os.path.isdir("Videos"):
    os.mkdir("Videos")


# Screen resolution
width = 1366
height = 768

if args.fullhd:
    width = 1920
    height = 1080


# Setting up the window for screenRec
bounding_box = {'top': 0, 'left': 0, 'width': width, 'height': height}


# Stealth capture!
if args.silentcapture:
    sct = mss()
    sct_img = sct.grab(bounding_box)
    frame = np.array(sct_img)

    if args.imagename:
        cv2.imwrite('Images/' + args.imagename + '.png', frame)
        print('Images/' + args.imagename + '.png -- Screenshot saved!')
    else:
        cv2.imwrite('Images/Img' + '.png', frame)
        print('Images/Img' + '.png -- Screenshot saved!')

    sys.exit(0)


# Video name to be saved
video_name = "Screen_record"
if args.videoname:
    video_name = args.videoname


sct = mss()
SCREEN_SIZE = (bounding_box['width'], bounding_box['height'])


img_save = 1  # Counts number of screenshots
mouse_pts = []
frame_num = 0
start_recording = False

# Mouse clicks handler
def get_mouse_points(event, x, y, flags, param):
    global mouseX, mouseY, mouse_pts
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseX, mouseY = x, y
        cv2.circle(frame, (x, y), 10, (0, 0, 255), 10)
        if "mouse_pts" not in globals():
            mouse_pts = []
        mouse_pts.append((x, y))
        print("Point detected")
        # print(mouse_pts)

# Setting up the window
cv2.namedWindow("image")
cv2.setMouseCallback("image", get_mouse_points)

# Setting up the screen recorder
sct_img = sct.grab(bounding_box)
sleep(0.3)  # Wait some time to avoid glitches
frame = np.array(sct_img)
# cv2.imshow('Screen Record', frame)

image = frame

# Help text
text1 = "Select top-left and bottom-right"
text2  = "     corners of the image   "
text3 = "s - screenshot, r - start recording"
text4 = "          q - quit              "
text5 = "   Click anywhere to continue   "
font = cv2.FONT_HERSHEY_SIMPLEX
text_xy = (int(width/2)-300, int(height/2))
fontScale = 1
color = (0, 0, 255)
thickness = 2
image = cv2.putText(image, text1, text_xy, font,
                    fontScale, color, thickness, cv2.LINE_AA)
image = cv2.putText(image, text2, (int(width/2)-300, int(height/2)+50), font,
                    fontScale, color, thickness, cv2.LINE_AA)
image = cv2.putText(image, text3, (int(width/2)-300, int(height/2)+100), font,
                    fontScale, color, thickness, cv2.LINE_AA)
image = cv2.putText(image, text4, (int(width/2)-300, int(height/2)+150), font,
                    fontScale, color, thickness, cv2.LINE_AA)

# To get the portion of the screen to record
while True:

    cv2.imshow("image", image)
    cv2.waitKey(1)

    # print(len(mouse_pts))

    if len(mouse_pts) == 2:
        image = cv2.putText(image, text5, (int(width / 2) - 300, int(height / 2) + 200), font,
                            fontScale, color, thickness, cv2.LINE_AA)

    if len(mouse_pts) >= 3:
        cv2.destroyWindow("image")
        break

    key = cv2.waitKey(33)
    if key == ord('q'):
        print("Quitting...")
        cv2.destroyAllWindows()
        sys.exit(0)
        break


# Now change the window size to record the screen
region_w = abs(mouse_pts[1][0]-mouse_pts[0][0])
region_h = abs(mouse_pts[1][1]-mouse_pts[0][1])
bounding_box = {'top': mouse_pts[0][1], 'left': mouse_pts[0][0],
                'width': region_w, 'height': region_h}



# codec to record the video
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("Videos/"+video_name+".avi", fourcc, 20, (640, 480))


# Main program
while True:
    sct_img = sct.grab(bounding_box)
    frame = np.array(sct_img)
    cv2.imshow('Screen Record', frame)


    if start_recording == True:
        out.write(frame)

    key = cv2.waitKey(33)

    if key == ord('r'):
        start_recording = True
        print("Started recording...")



    elif key == ord('s'):
        if args.imagename:
            cv2.imwrite('Images/'+args.imagename+' '+str(img_save)+'.png', frame)
            print('Images/'+args.imagename+' '+str(img_save)+'.png -- Screenshot saved!')
        else:
            cv2.imwrite('Images/Img '+str(img_save)+'.png', frame)
            print('Images/Img '+str(img_save)+'.png -- Screenshot saved!')
        img_save += 1

    elif key == ord('q'):
        print("Quitting...")
        break


out.release()
print("Recording ended.")
cv2.destroyAllWindows()
