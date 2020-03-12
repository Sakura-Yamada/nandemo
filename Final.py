##統合するコード


import RPi.GPIO as GPIO
import time
import sys


#set
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Pin Assignment
r1 = 9
r2 = 10
l1 = 8
l2 = 7


Frequency = 20
# How long the pin stays on each cycle, as a percent (here, it's 30%)
DutyCycle = 50
# Setting the duty cycle to 0 means the motors will not turn
Stop = 0


#Set in out
GPIO.setup(r1, GPIO.OUT) 
GPIO.setup(r2, GPIO.OUT) 
GPIO.setup(l1, GPIO.OUT) 
GPIO.setup(l2, GPIO.OUT) 


#SetPWM
pwm_r1 = GPIO.PWM(r1, Frequency)
pwm_r2 = GPIO.PWM(r2, Frequency)
pwm_l1 = GPIO.PWM(l1, Frequency)
pwm_l2 = GPIO.PWM(l2, Frequency)


#setupPWM
pwm_r1.start(Stop)
pwm_r2.start(Stop)
pwm_l1.start(Stop)
pwm_l2.start(Stop)



#関数の定義
#motor_OO( number ) で、モーター制御ができる(はず)

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




GPIO.cleanup()
