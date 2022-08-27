from  gpiozero import AngularServo
from time import sleep

temp1=1
time = 0
count = 1

servo = AngularServo(18, min_pulse_width=0.0006,max_pulse_width = 0.0025)
servo.angle = 5



while True:
    servo.angle = 90
    sleep(5)
    servo.angle = 5
    sleep(10)
        