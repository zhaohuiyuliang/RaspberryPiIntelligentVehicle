import RPi.GPIO as GPIO

import time

GPIO.setwarinings(False)
GPIO.setmode(GPIO.BOARD)

gpio_in1 = 19
gpio_in2 = 23

gpio_in3 = 24
gpio_in4 = 26

GPIO.setup(gpio_in1, GPIO.OUT)
GPIO.setup(gpio_in2, GPIO.OUT)

GPIO.setup(gpio_in3, GPIO.OUT)
GPIO.setup(gpio_in4, GPIO.OUT)

#后左车轮向前旋转
def lForward():
    GPIO.output(gpio_in1, GPIO.LOW)
    GPIO.output(gpio_in1, GPIO.HIGH)
    
#后右边车轮向前旋转
def rForward():
    GPIO.output(gpio_in3, GPIO.HIGH)
    GPIO.output(gpio_in4, GPIO.LOW)
    
#小车前进
def forward():
    lForward()
    rForward()

#后右边车轮后旋转
def rBackground():
    GPIO.output(gpio_in3, GPIO.LOW)
    GPIO.output(gpio_in4, GPIO.HIGH)

#后左边车轮后旋转
def lBackground():
    GPIO.output(gpio_in1, GPIO.HIGH)
    GPIO.output(gpio_in2, GPIO.LOW)
    
#小车倒车
def background():
    rBackground()
    lBackground()

#小车左后轮停止
def lStop():
    GPIO.output(gpio_in1, GPIO.LOW)
    GPIO.output(gpio_in2, GPIO.LOW)

#小车右后轮停止
def rStop():
    GPIO.output(gpio_in3, GPIO.LOW)
    GPIO.output(gpio_in4, GPIO.LOW)

#小车停止
def allStop():
    lStop()
    rStop()
