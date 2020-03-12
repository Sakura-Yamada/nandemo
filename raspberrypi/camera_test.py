import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
import sys

URL = "http://192.168.0.121:8080/?action=stream"

cap = cv2.VideoCapture(URL)


def area:
    while True:
        ret,frame = cap.read()

        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


        lo_color = np.array([20,100,100])
        hi_color = np.array([66,255,255])
        mask = cv2.inRange(hsv,lo_color,hi_color)

#肌色[0,30,60][20,150,255]
#黄色[56,100,100]
#緑色[120,100,100]
#赤色[0,100,100]



        _, contours, hierarchy = cv2.findContours(mask,1,2)
  
        if len(contours) == 0:
            continue
  
        area_list = [cv2.contourArea(cnt) for cnt in contours]
  
        big_index = np.argmax(area_list)
  
        Area = area_list[big_index]

        print("Area = ",Area)

        big_area = contours[big_index]
  
        M = cv2.moments(big_area)
  
        try:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        except ZeroDivisionError:
            print("error")
            continue
  
  
    print("X = ",cx)
    print("Y = ",cy)
  
  
  
  #黄色だけ検出
    only_color = cv2.bitwise_and(frame,frame,mask=mask)
  
    cv2.imshow("show mask!",mask)
    #cv2.imshow("show image",frame)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cv2.destroyAllWindows()



#5cm 160000

#10cm 60000 

#15cm 33000





