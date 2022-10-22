# TriangularMotionProfile.py: Triangular velocity profile generator in MicroPython
# Used to smooth servo motions and trajectories
# Copyright (C) 2022 Vincent Mistler (YouMakeTech)

from math import sqrt
from time import ticks_ms,sleep_ms

class TriangularMotionProfile:
    def __init__(self,startValue,endValue,duration_ms):
        
        # internal variables
        self._startValue=startValue
        self._endValue=endValue
        self._duration_ms=duration_ms
        self._currentValue=startValue
        self._currentTime=ticks_ms()
        self._startTime=self._currentTime
        self._moveInProgress=True
        
    # Returns the current position for the move
    # should be called as frequently as possible after
    # creating the TriangularMotionProfile object and
    # until isComplete() returns True
    def getValue(self):
        averageVelocity=float((self._endValue-self._startValue)/self._duration_ms)
        maxVelocity=2.0*averageVelocity;
        acceleration=(2.0*maxVelocity)/self._duration_ms;
        halfWayTime=self._startTime+self._duration_ms/2
        endTime=self._startTime+self._duration_ms
        self._currentTime=ticks_ms()
        
        if self._currentTime<self._startTime:
            self._currentValue=self._startValue
            self._moveInProgress=False
        elif self._currentTime<=halfWayTime:
            self._currentValue=self._startValue+0.5*acceleration*(self._currentTime-self._startTime)*(self._currentTime-self._startTime)
            self._moveInProgress=True
        elif self._currentTime<=endTime:
            self._currentValue=self._endValue-0.5*acceleration*(endTime-self._currentTime)*(endTime-self._currentTime)
            self._moveInProgress=True
        else:
            self._currentValue=self._endValue
            self._moveInProgress=False
        return self._currentValue
        
    def moveInProgress(self):
        return self._moveInProgress
      
    def plot(self):
        t0=ticks_ms()
        while self.moveInProgress():
            print(str(ticks_ms()-t0)+','+str(self.getValue()))
            sleep_ms(20)
        
if __name__ == "__main__":
    trajectory=TriangularMotionProfile(500,2500,500)
    trajectory.plot()
    trajectory=TriangularMotionProfile(2500,500,1000)
    trajectory.plot()
