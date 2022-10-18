# servoTest.py: move a servo motor using PWM in pure MicroPython (no library) 
# Copyright (C) 2022 Vincent Mistler (YouMakeTech)

from machine import Pin, PWM
from time import sleep

servo=PWM(Pin(0))
servo.freq(50) # Hz

while True:
    servo.duty_ns(640000)
    sleep(1) # second
    servo.duty_ns(1500000) # Center
    sleep(1) # second
    servo.duty_ns(2400000)
    sleep(1) # second
    