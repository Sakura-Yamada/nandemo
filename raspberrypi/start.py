import RPi.GPIO as GPIO
import time
import sys
import time
import cv2
import numpy as np


URL = "http://192.168.0.121:8080/?action=stream"
cap = cv2.VideoCapture(URL)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

r1 = 9
r2 = 10
l1 = 8
l2 = 7

Frequency = 20
DutyCycle = 50
Stop = 0



#Set in out
GPIO.setup(r1, GPIO.OUT)
GPIO.setup(r2, GPIO.OUT)
GPIO.setup(l1, GPIO.OUT)
GPIO.setup(l2, GPIO.OUT)

pwm_r1 = GPIO.PWM(r1, Frequency)
pwm_r2 = GPIO.PWM(r2, Frequency)
pwm_l1 = GPIO.PWM(l1, Frequency)
pwm_l2 = GPIO.PWM(l2, Frequency)

pwm_r1.start(Stop)
pwm_r2.start(Stop)
pwm_l1.start(Stop)
pwm_l2.start(Stop)



def forward(wait_time):
    pwm_r1.ChangeDutyCycle(DutyCycle)
    pwm_r2.ChangeDutyCycle(Stop)
    pwm_l1.ChangeDutyCycle(DutyCycle)
    pwm_l2.ChangeDutyCycle(Stop)
    print("forward")
    time.sleep(wait_time)
 
def back(wait_time):
    pwm_r1.ChangeDutyCycle(Stop)
    pwm_r2.ChangeDutyCycle(DutyCycle)
    pwm_l1.ChangeDutyCycle(Stop)
    pwm_l2.ChangeDutyCycle(DutyCycle)
    print("back")
    time.sleep(wait_time)
 
def right(wait_time):
    pwm_r1.ChangeDutyCycle(DutyCycle)
    pwm_r2.ChangeDutyCycle(Stop)
    pwm_l1.ChangeDutyCycle(Stop)
    pwm_l2.ChangeDutyCycle(DutyCycle)
    print("right")
    time.sleep(wait_time)
 
def left(wait_time):
    pwm_r1.ChangeDutyCycle(Stop)
    pwm_r2.ChangeDutyCycle(DutyCycle)
    pwm_l1.ChangeDutyCycle(DutyCycle)
    pwm_l2.ChangeDutyCycle(Stop)
    print("left")
    time.sleep(wait_time)
  
def m_stop(wait_time):
    pwm_r1.ChangeDutyCycle(Stop)
    pwm_r2.ChangeDutyCycle(Stop)
    pwm_l1.ChangeDutyCycle(Stop)
    pwm_l2.ChangeDutyCycle(Stop)
    print("stop")
    time.sleep(wait_time)


def area_check():
    while True:
        ret,frame = cap.read()
  
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    
        lo_color = np.array([40,50,50])
        hi_color = np.array([70,200,200])
        mask = cv2.inRange(hsv,lo_color,hi_color)
    
#肌色[0,30,60][20,150,255]
#黄色[56,100,100]
#緑色[120,100,100]
#赤色[0,100,100]
  
  
      
        contours, hierarchy = cv2.findContours(mask,1,2)       
        
         
        if len(contours) == 0:
            continue
      
        area_list = [cv2.contourArea(cnt) for cnt in contours]      
        big_index = np.argmax(area_list)        
        Area = area_list[big_index]
        big_area = contours[big_index]
        M = cv2.moments(big_area)
        
        print("Area = ",Area)
        return Area

        try:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        except ZeroDivisionError:
            continue

        if cx >= 213 & cx <= 426:
            print("Middle")
            print(cx)
        if cx < 213:
            print("Right")
            print(cx)
        if cx > 426:
            print("Left")
            print(cx)

    cv2.circle(frame,(cx,cy),5,(255,0,0),-1)


    only_color = cv2.bitwise_and(frame,frame,mask=mask)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(gray,100,200)

    ret,binary = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

    cv2.imshow("show image",frame)
    cv2.imshow("show mask",mask)



def size_area(Area):
    Area = area_check()
    
    if Area < 600:
        move = LEFT
    elif 600 <= Area and Area <= 6000:
        move = GO
    elif 6000 < Area:
        move = STOP
    else:
        move = STOP

    return move


while True:
    area_check()
    size_area(Area)
    if move == LEFT:
        left(2)
    elif move == GO:
        forward(2)
    elif move == STOP:
        m_stop(0.5)
    else:
        m_stop(0.5)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cv2.destroyAllWindows()
