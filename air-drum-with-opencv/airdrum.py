#onemotion.com
import cv2
import numpy as np
import pyautogui
import imutils

def Press(key):
    pyautogui.press(key)

cap = cv2.VideoCapture(0);

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame = imutils.resize(frame,height=700, width=900)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowred = np.array([131,90,106])
    highred = np.array([255,255,255])

    lowblue = np.array([40,150,116])
    highblue = np.array([255,255,255])

    red_mask = cv2.inRange(hsv, lowred, highred)
    blue_mask = cv2.inRange(hsv, lowblue, highblue)

    # image/frame, start_point, end_point, color, thickness
    cv2.rectangle(frame, (0,0), (200,150), (255,0,0),1)
    cv2.putText(frame,'RIDE',(70,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (210,0), (430,150), (0,0,255),1)
    cv2.putText(frame,'RIDE BELL',(245,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)
    cv2.rectangle(frame, (440,0), (650,150), (255,0,0),1)
    cv2.putText(frame,'HITHAT close',(445,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (660,0), (900,150), (0,0,255),1)
    cv2.putText(frame,'CRASH',(730,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)


    cv2.rectangle(frame, (0,160), (50,370), (255,0,0),1)
    cv2.putText(frame,'SNARE',(10,290),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (0,380), (50,570), (0,0,255),1)
    cv2.putText(frame,'SNARE RIM',(10,500),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)
    
    cv2.rectangle(frame, (850,160), (900,370), (255,0,0),1)
    cv2.putText(frame,'HIT HAT',(770,290),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (850,380), (900,570), (0,0,255),1)
    cv2.putText(frame,'HIT HAT OPEN',(670,500),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)


    cv2.rectangle(frame, (0,580), (200,700), (255,0,0),1)
    cv2.putText(frame,'TOM HI',(50,640),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (210,580), (430,700), (0,0,255),1)
    cv2.putText(frame,'TOM MID',(250,640),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)
    cv2.rectangle(frame, (440,580), (650,700), (255,0,0),1)
    cv2.putText(frame,'TOM LOW',(480,640),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (660,580), (900,700), (0,0,255),1)
    cv2.putText(frame,'KICK',(740,640),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)

    #for the red Object
    contours,hierachy=cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    #startpoint, endpoint, color, thickness
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
        print((x,y))   
        if x > 0 and y > 0 and x < 200 and y < 150:
            Press('7') #RIDE
            break      
        if x > 210 and y > 0  and x < 430 and y < 150:
            Press('8') #RIDE BELL
            break      
        if x > 440 and y > 0 and x < 650 and y < 150:
            Press('6') #HIT HAT CLOSE
            break      
        if x > 660 and y > 0 and x < 900 and y < 150:
            Press('9') #CRASH
            break      
        
        
        if x > 0 and y > 160 and x < 50 and y < 370:
            Press('2') #SNARE
            break      
        if x > 0 and y > 380 and x < 50 and y < 570:
            Press('3') #SNARE RIM
            break      
        if x > 850 and y > 160 and x < 900 and y < 370:
            Press('4') #HIT HAT 
            break      
        if x > 850 and y > 380 and x < 900 and y < 570:
            Press('5') #HIT HAT OPEN 
            break      
        
        
        if x > 0 and y > 580 and x < 200 and y < 700:
            Press('q') #TOM HI
            break      
        if x > 210 and y > 580 and x < 430 and y < 700:
            Press('w') #TOM MID
            break      
        if x > 440 and y > 580 and x < 650 and x < 700:
            Press('e') #TOM LOW 
            break      
        if x > 660 and y > 580 and x < 900 and y < 700:
            Press('1') #HIT HAT OPEN 
            break      
        break
    
    #for the blue Object
    contours,hierachy=cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    #startpoint, endpoint, color, thickness
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
        print((x,y))
        if x > 0 and y > 0 and x < 200 and y < 150:
            Press('7') #RIDE
            break      
        if x > 210 and y > 0  and x < 430 and y < 150:
            Press('8') #RIDE BELL
            break      
        if x > 440 and y > 0 and x < 650 and y < 150:
            Press('6') #HIT HAT CLOSE
            break      
        if x > 660 and y > 0 and x < 900 and y < 150:
            Press('9') #CRASH
            break      
        
        
        if x > 0 and y > 160 and x < 50 and y < 370:
            Press('2') #SNARE
            break      
        if x > 0 and y > 380 and x < 50 and y < 570:
            Press('3') #SNARE RIM
            break      
        if x > 850 and y > 160 and x < 900 and y < 370:
            Press('4') #HIT HAT 
            break      
        if x > 850 and y > 380 and x < 900 and y < 570:
            Press('5') #HIT HAT OPEN 
            break      
        
        
        if x > 0 and y > 580 and x < 200 and y < 700:
            Press('q') #TOM HI
            break      
        if x > 210 and y > 580 and x < 430 and y < 700:
            Press('w') #TOM MID
            break      
        if x > 440 and y > 580 and x < 650 and x < 700:
            Press('e') #TOM LOW 
            break      
        if x > 660 and y > 580 and x < 900 and y < 700:
            Press('1') #HIT HAT OPEN 
            break           
        break
    
    
    cv2.imshow("frame", frame)
    # cv2.imshow("mask", mask)
    # cv2.imshow("res", res)
 
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
