from cv2 import cv
import win32api
import win32gui, win32con
import sys
import time

posx = 0
posy = 0


########### You can add any type of a blob in to this algo ####################
########### For example you can use a nose detection algorythm in here##########
def getthresholdedimg(im):
    imghsv = cv.CreateImage(cv.GetSize(im), 8, 3)
    cv.CvtColor(im, imghsv, cv.CV_BGR2HSV)  # Convert image from RGB to HSV
    imgthreshold = cv.CreateImage(cv.GetSize(im), 8, 1)
    cv.InRangeS(imghsv, cv.Scalar(23, 100, 100), cv.Scalar(25, 255, 255), imgthreshold)  ## catch the orange yellow blob
    return imgthreshold


#################################################################################

def getpositions(im):
    leftmost = 0
    rightmost = 0
    topmost = 0
    bottommost = 0
    temp = 0
    for i in range(im.width):
        col = cv.GetCol(im, i)
        if cv.Sum(col)[0] != 0.0:
            rightmost = i
            if temp == 0:
                leftmost = i
                temp = 1
    for i in range(im.height):
        row = cv.GetRow(im, i)
        if cv.Sum(row)[0] != 0.0:
            bottommost = i
            if temp == 1:
                topmost = i
                temp = 2
    return (leftmost, rightmost, topmost, bottommost)


capture = cv.CaptureFromCAM(0)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 720)
frame = cv.QueryFrame(capture)
test = cv.CreateImage(cv.GetSize(frame), 8, 3)
cv.NamedWindow("output")
previous_x = 0
previous_y = 0
while (1):
    frame = cv.QueryFrame(capture)
    cv.Flip(frame, frame, 1)
    imdraw = cv.CreateImage(cv.GetSize(frame), 8, 3)  # we make all drawings on imdraw.
    imgyellowthresh = getthresholdedimg(frame)  # we get coordinates from imgyellowthresh
    cv.Erode(imgyellowthresh, imgyellowthresh, None, 1)  # eroding removes small noises
    (leftmost, rightmost, topmost, bottommost) = getpositions(imgyellowthresh)
    if (leftmost - rightmost != 0) or (topmost - bottommost != 0):
        lastx = posx
        lasty = posy
        posx = cv.Round((rightmost + leftmost) / 2)
        posy = cv.Round((bottommost + topmost) / 2)
        if lastx != 0 and lasty != 0:
            win32api.SetCursorPos((posx, posy))

    cv.Add(test, imdraw, test)
    cv.ShowImage("output", test)
    if cv.WaitKey(10) >= 0:
        break
cv.DestroyWindow("output")