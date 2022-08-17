import RPi.GPIO as GPIO
from  gpiozero import AngularServo
from time import sleep

in1 = 24
in2 = 23
en = 25
temp1=1
time = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.HIGH)
p=GPIO.PWM(en,1000)

servo = AngularServo(18, min_pulse_width=0.0006,max_pulse_width = 0.0024)
servo.angle = 0

while True:
    if time < 1000:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        time += 1
    elif time == 1000:
        servo.angle = -45
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        time += 1
    elif time > 1500:
        servo.angle = 0
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        time = 0
    else:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        time += 1
    print(time)
        