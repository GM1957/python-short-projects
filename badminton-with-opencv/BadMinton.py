import cv2
import numpy as np
import imutils
import random

cap = cv2.VideoCapture(0)

WIN_HEIGHT = 900
WIN_WIDTH = 900


def MyEllipse(frame,x,y):
    thickness = 2
    line_type = 8
    motion = random.randint(0, 20)
    widthMotion = random.randint(12, 22)
    height = 45
    # cv2.ellipse(frame, (x, y), (height, width), angle, 0, 360, (255, 0, 0), thickness, line_type)
    return cv2.ellipse(frame, (x, y), (height, widthMotion), 90 - motion, 0, 360, (255, 0, 0), thickness, line_type), cv2.ellipse(frame, (x, y), (height, widthMotion), 0 - motion, 0, 360, (255, 0, 0), thickness, line_type), cv2.ellipse(frame, (x, y), (height, widthMotion), 45 - motion, 0, 360, (255, 0, 0), thickness, line_type), cv2.ellipse(frame, (x, y), (height, widthMotion), -45 - motion, 0, 360, (255, 0, 0), thickness, line_type)

def Ball(frame, x, y):
    return cv2.circle(frame, (x, y), 15, (0, 0, 255), -1), MyEllipse(frame,x,y)

# ball center will be in 50th position in Y axis in the starting
winTop = 50

# ball center position in Y axis it will be changing while playing the game initially its same as winTop
ballPosY = 50

# ball center will be in 350th position in X axis in the starting
winMid = 350

# ball center position in X axis it will be changing while playing the game initially its same as winMid
ballPosX = 350

# this isHitten variable will tell ball is hitten by the bat or not based on that we can perform action
isHitten = False

# it will determine in which place of the bat ball has hitten
hitType = ""

isStarted = False
startingCounter = 0

score = 0
isOver = False

# initiating x,y,w,h
x = 0 
y = 0
w = 0 
h = 0

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = imutils.resize(frame, WIN_HEIGHT, WIN_WIDTH)

    if(isStarted == True):
        if(isOver == False):
            cv2.putText(frame,'SCORE: ' + str(score),(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
        elif(isOver == True):
            cv2.putText(frame,'<- GAME OVER ->',(320,350),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),5,cv2.LINE_AA)

        Ball(frame, ballPosX, ballPosY)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lowred = np.array([131, 90, 106])
        highred = np.array([255, 255, 255])
        red_mask = cv2.inRange(hsv, lowred, highred)

        contours, hierachy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
        
        for cnt in contours:
            # collecting the starting x,y and width, height values from the bounding box of the red object
            (x, y, w, h) = cv2.boundingRect(cnt)
            break    
            
        if(ballPosY + 50 > y and ballPosY + 50 < y + h and ballPosX + 50 > x and ballPosX + 50 < x + w):
            if ballPosX > x and ballPosX < x + int(w//3):
                hitType = "left"
            elif ballPosX > x + int(w//3) and ballPosX < x + int(w//3) + int(w//3):
                hitType = "middle"
            elif ballPosX > x + int(w//3) + int(w//3) and ballPosX < x + w:
                hitType = "right"
            else:
                hitType = "middle"
            isHitten = True
            score = score + 1

        if(ballPosY > WIN_HEIGHT):
            isOver = True

        if isHitten == True:
            ballPosY = ballPosY - 10
            if hitType == "left":
                ballPosX = ballPosX - 3
            elif hitType == "middle":
                ballPosX = ballPosX
            elif hitType == "right":
                ballPosX = ballPosX + 3

        if(isHitten == False):
            ballPosY = ballPosY + 10
            if hitType == "left":
                ballPosX = ballPosX - 3
            elif hitType == "middle":
                ballPosX = ballPosX
            elif hitType == "right":
                ballPosX = ballPosX + 3

        if(ballPosY in range(winTop - 50, winTop)):
            isHitten = False
        
        
    
    elif(isStarted == False):
        time = 500
        cv2.putText(frame,'GAME WILL START IN --> ' + str(time - startingCounter),(200,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
        startingCounter = startingCounter + 1
        if startingCounter > time:
            isStarted = True

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
