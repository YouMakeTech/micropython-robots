# Servo.py: Servo motor control in MicroPython
# Copyright (C) 2022 Vincent Mistler (YouMakeTech)

from machine import Pin, PWM
from time import sleep
from TriangularMotionProfile import TriangularMotionProfile

class Servo:
    def __init__(self,id,servoMin=640,servoMax=2400,servoCenter=1500, \
                 initialPosition=90.0,positionMin=0,positionMax=180):
        self.microseconds=-1    # servo initial position in µs (initialized by write)
        self.servoMin=servoMin # Pulse width in µs corresponding to 0 degrees
        self.servoMax=servoMax # Pulse width in µs corresponding to 180 degrees
        self.servoCenter=servoCenter # Pulse width in µs corresponding to 90 degrees
        self.positionMin=positionMin # min. commandable position in degrees
        self.positionMax=positionMax # max. commandable position in degrees
        self.id=id # GPIO pin to which the servo is connected
        self.enabled=False # True when the servo is connected to a PWM pin
        self.attach()
        self.write(initialPosition) 
    
    # microseconds=angleToMicroseconds(angle)
    # convert a servo angle to a pulse duration
    # angle is a float between 0 and 180 degrees included
    # microsecconds is the pulse width in us to send to the servo
    def angleToMicroseconds(self,angle):
        if angle<0:
            angle=0
        elif angle>180:
            angle=180
        if angle>=90:
            microseconds=int(self.servoCenter+(angle-90)*((self.servoMax-self.servoCenter)/90.0))
        else:
            microseconds=int(self.servoMin+angle*((self.servoCenter-self.servoMin)/90.0))
        return microseconds
    
    # angle=microsecondsToAngle(microseconds)
    # convert a pulse duration to a servo angle
    # microsecconds is the pulse width in us to send to the servo
    # angle is a float between 0 and 180 degrees included
    def microsecondsToAngle(self,microseconds):
        if microseconds<self.servoMin:
            microseconds=self.servoMin
        elif microseconds>self.servoMax:
            microseconds=self.servoMax
        if microseconds>=self.servoCenter:
            angle=90.0+((microseconds-self.servoCenter)*90.0)/(self.servoMax-self.servoCenter)
        else:
            angle=((microseconds-self.servoMin)*90.0)/(self.servoCenter-self.servoMin)
        return angle
    
    # writeMicroseconds(microseconds)
    # make the servo move by writing a pulse width on the pin
    def writeMicroseconds(self,microseconds):
        if self.enabled:
            if microseconds<self.servoMin:
                microseconds=self.servoMin
            elif microseconds>self.servoMax:
                microseconds=self.servoMax
            self.pin.duty_ns(1000*microseconds)
            self.microseconds=microseconds
            
    # write(angle)
    # move the servo to the specified angle
    # angle is a float between 0 and 180 degrees included
    def write(self,angle):
        if self.enabled:
            if angle<self.positionMin:
                print('Servo.write('+str(angle)+') limited to min. '+str(self.positionMin)+' degrees')
                angle=self.positionMin
            elif angle>self.positionMax:
                print('Servo.write('+str(angle)+') limited to max. '+str(self.positionMax)+' degrees')
                angle=self.positionMax
            else:
                print('Servo.write('+str(angle)+')')
                
            microseconds=self.angleToMicroseconds(angle)
            self.writeMicroseconds(microseconds)
        
    # angle=read()
    # returns the latest commanded position in degrees
    # angle is a float between 0 and 180 degrees included
    def read(self):
        return self.microsecondsToAngle(self.microseconds)
    
    # microseconds=readMicroseconds()
    # returns the latest commanded pulse width in µs
    # microseconds is an integer in us, typically between 640µs and 2400µs
    def readMicroseconds(self):
        return self.microseconds
    
    # trim(servoTrim)
    # adds an offset in µs to the center position (90 degrees)
    # This allows to shift the center position
    # servoTrim is the offset to add in µs (default value=0)
    def trim(self,servoTrim):
        # read the current angular position 
        position=self.read()
        # Add the trim to the servo center pulse width
        self.servoCenter=self.servoCenter+servoTrim
        # Move the servo immediately to see the effect
        self.write(position)
    
    # setServoMin(servoMin)
    # set the pulse width to command for the servo position at 0 degrees
    # servoMin is the pulse width in us (default=640)
    def setServoMin(self,servoMin):
        self.servoMin=servoMin
        # Move the servo immediately to see the effect
        self.write(0.0)
    
    # setServoMax(servoMax)
    # set the pulse width to command for the servo position at 180 degrees
    # servoMax is the pulse width in us (default=2400)
    def setServoMax(self,servoMax):
        self.servoMax=servoMax
        # Move the servo immediately to see the effect
        self.write(180.0)
    
    # setServoCenter(servoCenter)
    # set the pulse width to command for the servo position at 90 degrees
    # servoCenter is the pulse width in us (default=1500)
    def setServoCenter(self,servoCenter):
        self.servoCenter=servoCenter
        # Move the servo immediately to see the effect
        self.write(90.0)

    # microseconds=getServoMin()
    # returns the commanded pulse width for an angle of 0 degrees
    def getServoMin(self):
        return self.servoMin
    
    # microseconds=getServoMax()
    # returns the commanded pulse width for an angle of 180 degrees
    def getServoMax(self):
        return self.servoMax
    
    # microseconds=getServoCenter()
    # returns the commanded pulse width for an angle of 90 degrees
    def getServoCenter(self):
        return self.servoCenter
    
    # restoreDefaults()
    # restores default values for servoMin, servoMax and servoCenter
    def restoreDefaults(self):
        self.servoMin=640
        self.servoMax=2400
        self.servoCenter=1500
    
    # attached()
    # returns True if a pin is attached to the servo
    def attached(self):
        return self.enabled
    
    # attach()
    # enables a servo for PWM control 
    def attach(self):
        self.pin=PWM(Pin(self.id))
        self.pin.freq(50) # Hz
        self.enabled=True
        
    # detach()
    # disables a servo for PWM control
    # the servo ignores all motion commands until re-attached
    # free the PWM channel such that it can be re-used by another pin
    # The Pico exposes 26 GPIO pins but has only 16 PWM channels
    # For example, GP0 and GP16 share the same PWM channel PWM_A[0]
    # and only one GPIO can use the same PWM channel at a time
    # detach() is required when we want to control more than 16
    # servos. The servo remains in the last commanded position when
    # it does not receive any signal!
    #
    # Example usage:
    # >>> from Servo import Servo
    # >>> servo0=Servo(0)
    # >>> servo16=Servo(16)
    # >>> servo0.write(180) # the 2 servos move because they are connected to the same PWM channel
    # >>> servo0.detach()   # detach servo0 in order to move servo16 independently
    # >>> servo16.write(0)  # only servo16 moves, but not servo 0
    # >>> servo16.detach()
    # >>> servo0.attach()
    # >>> servo0.write(90)  # now we only move servo0, servo16 holds its last commanded position
    def detach(self):
        self.pin.deinit()
        Pin(self.id).init(mode=Pin.IN)
        self.enabled=False
        
    def move(self,angle,duration_ms=500):
        if self.enabled:
            microseconds=self.angleToMicroseconds(angle)
            trajectory=TriangularMotionProfile(self.microseconds,microseconds,duration_ms)
            while trajectory.moveInProgress():
                self.writeMicroseconds(int(trajectory.getValue()))
    
if __name__ == "__main__":
    # Attach a servo to GPIO pin 0
    servo=Servo(0)
    
    # Check conversions from angles to microseconds
    assert(servo.angleToMicroseconds(0)==640)
    assert(servo.angleToMicroseconds(90)==1500)
    assert(servo.angleToMicroseconds(180)==2400)
    
    # Check conversions from microseconds to angles
    assert(servo.microsecondsToAngle(640)==0)
    assert(servo.microsecondsToAngle(1500)==90)
    assert(servo.microsecondsToAngle(2400)==180)
    
    # attached returns true when a servo is attached
    assert(servo.attached())
    
    # check default values
    assert(servo.getServoMin()==640)
    assert(servo.getServoCenter()==1500)
    assert(servo.getServoMax()==2400)
    
    # Move the servo to 0 degrees (min. position)
    servo.write(0)
    assert(servo.read()==0)
    assert(servo.readMicroseconds()==640)
    sleep(1) # second
    
    # Move the servo to 90 degrees (center position)
    servo.write(90)
    assert(servo.read()==90)
    assert(servo.readMicroseconds()==1500)
    sleep(1) # second
    
    # Move the servo to 180 degrees (max. position)
    servo.write(180)
    assert(servo.read()==180)
    assert(servo.readMicroseconds()==2400)
    sleep(1) # second
    
    # Return to 0 degrees
    servo.write(90)

    # Servo trim
    servo.trim(50)
    assert(servo.getServoCenter()==1550)
    sleep(1) # second
    
    servo.trim(-100)
    assert(servo.getServoCenter()==1450)
    sleep(1) # second
    
    servo.trim(50)
    assert(servo.getServoCenter()==1500)
    sleep(1) # second
    
    # Servo Min./Max.
    servo.setServoMax(2300)
    sleep(1) # second
    servo.setServoMax(2400)
    sleep(1) # second
    servo.setServoMin(700)
    sleep(1) # second
    servo.setServoMax(640)
    sleep(1) # second
    servo.setServoCenter(1600)
    sleep(1) # second
    servo.setServoCenter(1500)
    sleep(1) # second
    
    # Return to 90 degrees
    servo.restoreDefaults()
    servo.write(90)
    
    # Detach the servo
    servo.detach()
    assert(servo.attached()==False)
    servo.write(0) # should not move
    sleep(0.5)
    servo.attach()
    assert(servo.attached())
    