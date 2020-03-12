# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
import time
import sys


#参考文献
#https://tool-lab.com/raspberrypi-startup-26/  
#https://github.com/CamJam-EduKit/EduKit3/tree/master/CamJam%20Edukit%203%20-%20RPi.GPIO/Code

#set
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Pin Assignment
r1 = 9
r2 = 10
l1 = 8
l2 = 7

#Set in out
GPIO.setup(r1, GPIO.OUT) 
GPIO.setup(r2, GPIO.OUT) 
GPIO.setup(l1, GPIO.OUT) 
GPIO.setup(l2, GPIO.OUT) 

#関数の定義
#motor_OO( number ) で、モーター制御ができる(はず)

def forward(wait_time):
  GPIO.output(r1, 1)
  GPIO.output(r2, 0)
  GPIO.output(l1, 1)
  GPIO.output(l2, 0)
  print("forward")
  time.sleep(wait_time)

def back(wait_time):
  GPIO.output(r1, 0)
  GPIO.output(r2, 1)
  GPIO.output(l1, 0)
  GPIO.output(l2, 1)
  print("back")
  time.sleep(wait_time)

def right(wait_time):
  GPIO.output(r1, 1)
  GPIO.output(r2, 0)
  GPIO.output(l1, 0)
  GPIO.output(l2, 1)
  print("right")
  time.sleep(wait_time)

def left(wait_time):
  GPIO.output(r1, 0)
  GPIO.output(r2, 1)
  GPIO.output(l1, 1)
  GPIO.output(l2, 0)
  print("left")
  time.sleep(wait_time)
  
def stop(wait_time):
  GPIO.output(r1, 0)
  GPIO.output(r2, 0)
  GPIO.output(l1, 0)
  GPIO.output(l2, 0)
  print("stop")
  time.sleep(wait_time)


#テスト
forward(2)
stop(0.5)
back(2)
stop(0.5)
right(2)
stop(0.5)
left(2)
stop(0.5)
stop(2)


GPIO.cleanup()
