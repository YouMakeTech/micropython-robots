# Servo.py: Servo motor control in MicroPython
# Copyright (C) 2022 Vincent Mistler (YouMakeTech)

from machine import Pin, PWM
from time import sleep

class Servo:
    def __init__(self,id,servo_min=640,servo_max=2400,servo_center=1500, \
                 initial_position=90.0,position_min=0,position_max=180):
        self.microseconds=-1    # servo initial position in µs (initialized by write)
        self.servo_min=servo_min # Pulse width in µs corresponding to 0 degrees
        self.servo_max=servo_max # Pulse width in µs corresponding to 180 degrees
        self.servo_center=servo_center # Pulse width in µs corresponding to 90 degrees
        self.position_min=position_min # min. commandable position in degrees
        self.position_max=position_max # max. commandable position in degrees
        self.id=id # GPIO pin to which the servo is connected
        self.enabled=False # True when the servo is connected to a PWM pin
        self.attach()
        self.write(initial_position) 
    
    # microseconds=angle_to_microseconds(angle)
    # convert a servo angle to a pulse duration
    # angle is a float between 0 and 180 degrees included
    # microsecconds is the pulse width in us to send to the servo
    def angle_to_microseconds(self,angle):
        if angle<0:
            angle=0
        elif angle>180:
            angle=180
        if angle>=90:
            microseconds=int(self.servo_center+(angle-90)*((self.servo_max-self.servo_center)/90.0))
        else:
            microseconds=int(self.servo_min+angle*((self.servo_center-self.servo_min)/90.0))
        return microseconds
    
    # angle=microseconds_to_angle(microseconds)
    # convert a pulse duration to a servo angle
    # microsecconds is the pulse width in us to send to the servo
    # angle is a float between 0 and 180 degrees included
    def microseconds_to_angle(self,microseconds):
        if microseconds<self.servo_min:
            microseconds=self.servo_min
        elif microseconds>self.servo_max:
            microseconds=self.servo_max
        if microseconds>=self.servo_center:
            angle=90.0+((microseconds-self.servo_center)*90.0)/(self.servo_max-self.servo_center)
        else:
            angle=((microseconds-self.servo_min)*90.0)/(self.servo_center-self.servo_min)
        return angle
    
    # write_microseconds(microseconds)
    # make the servo move by writing a pulse width on the pin
    def write_microseconds(self,microseconds):
        if self.enabled:
            if microseconds<self.servo_min:
                microseconds=self.servo_min
            elif microseconds>self.servo_max:
                microseconds=self.servo_max
            self.pin.duty_ns(1000*microseconds)
            self.microseconds=microseconds
            
    # write(angle)
    # move the servo to the specified angle
    # angle is a float between 0 and 180 degrees included
    def write(self,angle):
        if self.enabled:
            if angle<self.position_min:
                print('Servo.write('+str(angle)+') limited to min. '+str(self.position_min)+' degrees')
                angle=self.position_min
            elif angle>self.position_max:
                print('Servo.write('+str(angle)+') limited to max. '+str(self.position_max)+' degrees')
                angle=self.position_max
            else:
                print('Servo.write('+str(angle)+')')
                
            microseconds=self.angle_to_microseconds(angle)
            self.write_microseconds(microseconds)
        
    # angle=read()
    # returns the latest commanded position in degrees
    # angle is a float between 0 and 180 degrees included
    def read(self):
        return self.microseconds_to_angle(self.microseconds)
    
    # microseconds=read_micro_seconds()
    # returns the latest commanded pulse width in µs
    # microseconds is an integer in us, typically between 640µs and 2400µs
    def read_microseconds(self):
        return self.microseconds
    
    # trim(servo_trim)
    # adds an offset in µs to the center position (90 degrees)
    # This allows to shift the center position
    # servo_trim is the offset to add in µs (default value=0)
    def trim(self,servo_trim):
        # read the current angular position 
        position=self.read()
        # Add the trim to the servo center pulse width
        self.servo_center=self.servo_center+servo_trim
        # Move the servo immediately to see the effect
        self.write(position)
    
    # set_servo_min(servo_min)
    # set the pulse width to command for the servo position at 0 degrees
    # servo_min is the pulse width in us (default=640)
    def set_servo_min(self,servo_min):
        self.servo_min=servo_min
        # Move the servo immediately to see the effect
        self.write(0.0)
    
    # set_servo_max(servo_max)
    # set the pulse width to command for the servo position at 180 degrees
    # servo_max is the pulse width in us (default=2400)
    def set_servo_max(self,servo_max):
        self.servo_max=servo_max
        # Move the servo immediately to see the effect
        self.write(180.0)
    
    # set_servo_center(servo_center)
    # set the pulse width to command for the servo position at 90 degrees
    # servo_center is the pulse width in us (default=1500)
    def set_servo_center(self,servo_center):
        self.servo_center=servo_center
        # Move the servo immediately to see the effect
        self.write(90.0)

    # microseconds=get_servo_min()
    # returns the commanded pulse width for an angle of 0 degrees
    def get_servo_min(self):
        return self.servo_min
    
    # microseconds=get_servo_max()
    # returns the commanded pulse width for an angle of 180 degrees
    def get_servo_max(self):
        return self.servo_max
    
    # microseconds=get_servo_center()
    # returns the commanded pulse width for an angle of 90 degrees
    def get_servo_center(self):
        return self.servo_center
    
    # restore_defaults()
    # restores default values for servo_min, servo_max and servo_center
    def restore_defaults(self):
        self.servo_min=640
        self.servo_max=2400
        self.servo_center=1500
    
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
    
if __name__ == "__main__":
    # Attach a servo to GPIO pin 0
    servo=Servo(0)
    
    # Check conversions from angles to microseconds
    assert(servo.angle_to_microseconds(0)==640)
    assert(servo.angle_to_microseconds(90)==1500)
    assert(servo.angle_to_microseconds(180)==2400)
    
    # Check conversions from microseconds to angles
    assert(servo.microseconds_to_angle(640)==0)
    assert(servo.microseconds_to_angle(1500)==90)
    assert(servo.microseconds_to_angle(2400)==180)
    
    # attached returns true when a servo is attached
    assert(servo.attached())
    
    # check default values
    assert(servo.get_servo_min()==640)
    assert(servo.get_servo_center()==1500)
    assert(servo.get_servo_max()==2400)
    
    # Move the servo to 0 degrees (min. position)
    servo.write(0)
    assert(servo.read()==0)
    assert(servo.read_microseconds()==640)
    sleep(1) # second
    
    # Move the servo to 90 degrees (center position)
    servo.write(90)
    assert(servo.read()==90)
    assert(servo.read_microseconds()==1500)
    sleep(1) # second
    
    # Move the servo to 180 degrees (max. position)
    servo.write(180)
    assert(servo.read()==180)
    assert(servo.read_microseconds()==2400)
    sleep(1) # second
    
    # Return to 0 degrees
    servo.write(90)

    # Servo trim
    servo.trim(50)
    assert(servo.get_servo_center()==1550)
    sleep(1) # second
    
    servo.trim(-100)
    assert(servo.get_servo_center()==1450)
    sleep(1) # second
    
    servo.trim(50)
    assert(servo.get_servo_center()==1500)
    sleep(1) # second
    
    # Servo Min./Max.
    servo.set_servo_max(2300)
    sleep(1) # second
    servo.set_servo_max(2400)
    sleep(1) # second
    servo.set_servo_min(700)
    sleep(1) # second
    servo.set_servo_max(640)
    sleep(1) # second
    servo.set_servo_center(1600)
    sleep(1) # second
    servo.set_servo_center(1500)
    sleep(1) # second
    
    # Return to 90 degrees
    servo.restore_defaults()
    servo.write(90)
    
    # Detach the servo
    servo.detach()
    assert(servo.attached()==False)
    servo.write(0) # should not move
    sleep(0.5)
    servo.attach()
    assert(servo.attached())
    