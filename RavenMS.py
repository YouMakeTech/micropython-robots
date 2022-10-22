# RavenMS.py: class to control the Raven MS helicopter transformer humanoid robot by Tang Woonthai
# Copyright (C) 2022 Vincent Mistler (YouMakeTech)
# Robot and motion stands by Tang Woonthai: https://youtube.com/shorts/nuiew2s-k3U

from Servo import Servo
from time import sleep

class RavenMS:
    def __init__(self):
        print('RavenMS()')

        # lb  human pose
        self.rightFoot=Servo(0,initialPosition=90-40,positionMin=10,positionMax=90)
        self.rightLowerLeg=Servo(1,initialPosition=90-40,positionMin=50,positionMax=160)
        self.rightUpperLeg=Servo(2,initialPosition=90+40,positionMin=40,positionMax=130)
        self.rightHip=Servo(3,initialPosition=90-40,positionMin=50,positionMax=170)
        self.leftHip=Servo(4,initialPosition=90+40,positionMin=10,positionMax=130)
        self.leftUpperLeg=Servo(5,initialPosition=90-40,positionMin=50,positionMax=140)
        self.leftLowerLeg=Servo(6,initialPosition=90+40,positionMin=30,positionMax=130)
        self.leftFoot=Servo(7,initialPosition=90+40,positionMin=90,positionMax=170)
        self.lowBody=Servo(9,initialPosition=90-40,positionMin=30,positionMax=80)
        self.upperBody=Servo(10,initialPosition=90-40,positionMin=0,positionMax=100)
                              
        self.lowerBodyServos=[]
        self.lowerBodyServos.append(self.rightFoot)      # 0
        self.lowerBodyServos.append(self.rightLowerLeg) # 1
        self.lowerBodyServos.append(self.rightUpperLeg) # 2
        self.lowerBodyServos.append(self.rightHip)       # 3
        self.lowerBodyServos.append(self.leftHip)        # 4
        self.lowerBodyServos.append(self.leftUpperLeg)  # 5
        self.lowerBodyServos.append(self.leftLowerLeg)  # 6
        self.lowerBodyServos.append(self.leftFoot)       # 7
        self.lowerBodyServos.append(self.lowBody)        # 8
        self.lowerBodyServos.append(self.upperBody)      # 9
        
#         # Detach the lower body servos before attaching the upper body
#         # to avoid conflict between shared PWM channels
#         sleep(0.500)
#         for ithServo in self.lowerBodyServos:
#             ithServo.detach()
#         sleep(0.500)
#         
#         # ub heli pose (stand 17)
#         self.rightLowerArm=Servo(11,initialPosition=90+10)
#         self.rightArm=Servo(12,initialPosition=90-89)
#         self.rightShoulder=Servo(13,initialPosition=90-80)
#         self.sd1=Servo(14,initialPosition=90)
#         self.sd2=Servo(15,initialPosition=90)
#         self.sd3=Servo(16,initialPosition=90)
#         self.leftShoulder=Servo(17,initialPosition=90+60)
#         self.leftArm=Servo(18,initialPosition=90+40)
#         self.leftLowerArm=Servo(19,initialPosition=90+80)
#         self.mainRotor=Servo(20,initialPosition=0)
#         self.tailRotor=Servo(21,initialPosition=0)
#         
#         self.upperBodyServos=[]
#         self.upperBodyServos.append(self.rightLowerArm) # 0
#         self.upperBodyServos.append(self.rightArm)       # 1
#         self.upperBodyServos.append(self.rightShoulder)  # 2
#         self.upperBodyServos.append(self.sd1)             # 3
#         self.upperBodyServos.append(self.sd2)             # 4
#         self.upperBodyServos.append(self.sd3)             # 5
#         self.upperBodyServos.append(self.leftShoulder)   # 6
#         self.upperBodyServos.append(self.leftArm)        # 7
#         self.upperBodyServos.append(self.leftLowerArm)  # 8
#         self.upperBodyServos.append(self.mainRotor)      # 9
#         self.upperBodyServos.append(self.tailRotor)      # 10
#         
#         # Detach the upper body servos
#         sleep(0.500)
#         for ithServo in self.upperBodyServos:
#             ithServo.detach()
#         sleep(0.500)
#         
#         # Re-attach the lower body servos
#         sleep(0.500)
#         for ithServo in self.lowerBodyServos:
#             ithServo.attach()
#         sleep(0.500)
        
    def delay(self,ms):
        print('RavenMS.delay(' + str(ms) + ')')
        sleep(ms/1000)
    
    def walk(self):
        print('RavenMS.walk()')
        # 1stand 1(100)
        self.lowerBodyServos[0].write(90-40);        #right foot
        self.lowerBodyServos[1].write(90-40+0);        #right lower leg
        self.lowerBodyServos[2].write(90+40-0);        #right upper leg
        self.lowerBodyServos[3].write(90-40);        #right hip
        self.lowerBodyServos[4].write(90+40);       #left hip
        self.lowerBodyServos[5].write(90-40+0);        #left upper leg
        self.lowerBodyServos[6].write(90+40);        #left lower leg
        self.lowerBodyServos[7].write(90+40);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(1000);
        #2stand 2(1100)
        self.lowerBodyServos[0].write(90-40);        #right foot
        self.lowerBodyServos[1].write(90-40+30);        #right lower leg
        self.lowerBodyServos[2].write(90+40-30);        #right upper leg
        self.lowerBodyServos[3].write(90-40);        #right hip
        self.lowerBodyServos[4].write(90+40);       #left hip
        self.lowerBodyServos[5].write(90-40+30);        #left upper leg
        self.lowerBodyServos[6].write(90+40-30);        #left lower leg
        self.lowerBodyServos[7].write(90+40);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(200);
        #3stand r side(1300)
        self.lowerBodyServos[0].write(90-40-11);        #right foot
        self.lowerBodyServos[1].write(90-40+30);        #right lower leg
        self.lowerBodyServos[2].write(90+40-30);        #right upper leg
        self.lowerBodyServos[3].write(90-40-11);        #right hip
        self.lowerBodyServos[4].write(90+40-11);       #left hip
        self.lowerBodyServos[5].write(90-40+30);        #left upper leg
        self.lowerBodyServos[6].write(90+40-30);        #left lower leg
        self.lowerBodyServos[7].write(90+40-11);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(200);
        #4stand r foot(1500)
        self.lowerBodyServos[0].write(90-40-11);        #right foot
        self.lowerBodyServos[1].write(90-40+30);        #right lower leg
        self.lowerBodyServos[2].write(90+40-30);        #right upper leg
        self.lowerBodyServos[3].write(90-40-11);        #right hip
        self.lowerBodyServos[4].write(90+40-11);       #left hip
        self.lowerBodyServos[5].write(90-40+70);        #left upper leg
        self.lowerBodyServos[6].write(90+40-70);        #left lower leg
        self.lowerBodyServos[7].write(90+40-11);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(150);
        #5stand r foot l foot forward(1650)
        self.lowerBodyServos[0].write(90-40-12);        #right foot
        self.lowerBodyServos[1].write(90-40+30);        #right lower leg
        self.lowerBodyServos[2].write(90+40-30);        #right upper leg
        self.lowerBodyServos[3].write(90-40-12);        #right hip
        self.lowerBodyServos[4].write(90+40-12);       #left hip
        self.lowerBodyServos[5].write(90-40+70);        #left upper leg
        self.lowerBodyServos[6].write(90+40-0);        #left lower leg
        self.lowerBodyServos[7].write(90+40-12);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(150);
        #6stand r foot l foot down(1800)
        self.lowerBodyServos[0].write(90-40-12);        #right foot
        self.lowerBodyServos[1].write(90-40+30);        #right lower leg
        self.lowerBodyServos[2].write(90+40-30);        #right upper leg
        self.lowerBodyServos[3].write(90-40-12);        #right hip
        self.lowerBodyServos[4].write(90+40-12);       #left hip
        self.lowerBodyServos[5].write(90-40+50);        #left upper leg
        self.lowerBodyServos[6].write(90+40-0);        #left lower leg
        self.lowerBodyServos[7].write(90+40-12);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(150);
        #7stand r foot l foot front1(1950)
        self.lowerBodyServos[0].write(90-40-6);        #right foot
        self.lowerBodyServos[1].write(90-40+35);        #right lower leg
        self.lowerBodyServos[2].write(90+40-22.5);        #right upper leg
        self.lowerBodyServos[3].write(90-40-6);        #right hip
        self.lowerBodyServos[4].write(90+40-6);       #left hip
        self.lowerBodyServos[5].write(90-40+35);        #left upper leg
        self.lowerBodyServos[6].write(90+40-22.5);        #left lower leg
        self.lowerBodyServos[7].write(90+40-6);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(100);
        #8stand r foot l foot front2(2050)
        self.lowerBodyServos[0].write(90-40-0);        #right foot
        self.lowerBodyServos[1].write(90-40+40);        #right lower leg
        self.lowerBodyServos[2].write(90+40-15);        #right upper leg
        self.lowerBodyServos[3].write(90-40-0);        #right hip
        self.lowerBodyServos[4].write(90+40-0);       #left hip
        self.lowerBodyServos[5].write(90-40+40);        #left upper leg
        self.lowerBodyServos[6].write(90+40-15);        #left lower leg
        self.lowerBodyServos[7].write(90+40-0);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(100);
        #8stand r foot l foot front3(2150)
        self.lowerBodyServos[0].write(90-40+8);        #right foot
        self.lowerBodyServos[1].write(90-40+45);        #right lower leg
        self.lowerBodyServos[2].write(90+40-7.5);        #right upper leg
        self.lowerBodyServos[3].write(90-40+8);        #right hip
        self.lowerBodyServos[4].write(90+40+8);       #left hip
        self.lowerBodyServos[5].write(90-40+35);        #left upper leg
        self.lowerBodyServos[6].write(90+40-22.5);        #left lower leg
        self.lowerBodyServos[7].write(90+40+8);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(100);
        #10stand l side l foot front(2250)
        self.lowerBodyServos[0].write(90-40+16);        #right foot
        self.lowerBodyServos[1].write(90-40+50);        #right lower leg
        self.lowerBodyServos[2].write(90+40-0);        #right upper leg
        self.lowerBodyServos[3].write(90-40+16);        #right hip
        self.lowerBodyServos[4].write(90+40+16);       #left hip
        self.lowerBodyServos[5].write(90-40+30);        #left upper leg
        self.lowerBodyServos[6].write(90+40-30);        #left lower leg
        self.lowerBodyServos[7].write(90+40+16);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(200);
        #11stand l  foot (2450)
        self.lowerBodyServos[0].write(90-40+16);        #right foot
        self.lowerBodyServos[1].write(90-40+70);        #right lower leg
        self.lowerBodyServos[2].write(90+40-70);        #right upper leg
        self.lowerBodyServos[3].write(90-40+16);        #right hip
        self.lowerBodyServos[4].write(90+40+16);       #left hip
        self.lowerBodyServos[5].write(90-40+30);        #left upper leg
        self.lowerBodyServos[6].write(90+40-30);        #left lower leg
        self.lowerBodyServos[7].write(90+40+16);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(150);
        #12stand l foot r foot forward (2600)
        self.lowerBodyServos[0].write(90-40+19);        #right foot
        self.lowerBodyServos[1].write(90-40+0);        #right lower leg
        self.lowerBodyServos[2].write(90+40-70);        #right upper leg
        self.lowerBodyServos[3].write(90-40+16);        #right hip
        self.lowerBodyServos[4].write(90+40+16);       #left hip
        self.lowerBodyServos[5].write(90-40+30);        #left upper leg
        self.lowerBodyServos[6].write(90+40-30);        #left lower leg
        self.lowerBodyServos[7].write(90+40+19);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(150);
        #13stand l foot r foot down(2750)
        self.lowerBodyServos[0].write(90-40+16);        #right foot
        self.lowerBodyServos[1].write(90-40+0);        #right lower leg
        self.lowerBodyServos[2].write(90+40-50);        #right upper leg
        self.lowerBodyServos[3].write(90-40+16);        #right hip
        self.lowerBodyServos[4].write(90+40+16);       #left hip
        self.lowerBodyServos[5].write(90-40+30);        #left upper leg
        self.lowerBodyServos[6].write(90+40-30);        #left lower leg
        self.lowerBodyServos[7].write(90+40+16);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(150);
        #14stand l foot r foot front1(2900)
        self.lowerBodyServos[0].write(90-40+8);        #right foot
        self.lowerBodyServos[1].write(90-40+7.5);        #right lower leg
        self.lowerBodyServos[2].write(90+40-45);        #right upper leg
        self.lowerBodyServos[3].write(90-40+0);        #right hip
        self.lowerBodyServos[4].write(90+40+8);       #left hip
        self.lowerBodyServos[5].write(90-40+22.5);        #left upper leg
        self.lowerBodyServos[6].write(90+40-35);        #left lower leg
        self.lowerBodyServos[7].write(90+40+8);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(100);
        #5stand l foot r foot front2(3000)
        self.lowerBodyServos[0].write(90-40+0);        #right foot
        self.lowerBodyServos[1].write(90-40+15);        #right lower leg
        self.lowerBodyServos[2].write(90+40-40);        #right upper leg
        self.lowerBodyServos[3].write(90-40+0);        #right hip
        self.lowerBodyServos[4].write(90+40+0);       #left hip
        self.lowerBodyServos[5].write(90-40+15);        #left upper leg
        self.lowerBodyServos[6].write(90+40-40);        #left lower leg
        self.lowerBodyServos[7].write(90+40+0);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(100);
        #16stand l foot r foot front3(3100)
        self.lowerBodyServos[0].write(90-40-5);        #right foot
        self.lowerBodyServos[1].write(90-40+22.5);        #right lower leg
        self.lowerBodyServos[2].write(90+40-35);        #right upper leg
        self.lowerBodyServos[3].write(90-40-5);        #right hip
        self.lowerBodyServos[4].write(90+40-5);       #left hip
        self.lowerBodyServos[5].write(90-40+7.5);        #left upper leg
        self.lowerBodyServos[6].write(90+40-45);        #left lower leg
        self.lowerBodyServos[7].write(90+40-5);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(100);
        #17stand r side r foot front(3200)
        self.lowerBodyServos[0].write(90-40-10);        #right foot
        self.lowerBodyServos[1].write(90-40+30);        #right lower leg
        self.lowerBodyServos[2].write(90+40-30);        #right upper leg
        self.lowerBodyServos[3].write(90-40-10);        #right hip
        self.lowerBodyServos[4].write(90+40-10);       #left hip
        self.lowerBodyServos[5].write(90-40+0);        #left upper leg
        self.lowerBodyServos[6].write(90+40-50);        #left lower leg
        self.lowerBodyServos[7].write(90+40-10);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(250);
        #18stand r foot(3450)
        self.lowerBodyServos[0].write(90-40-11);        #right foot
        self.lowerBodyServos[1].write(90-40+30);        #right lower leg
        self.lowerBodyServos[2].write(90+40-30);        #right upper leg
        self.lowerBodyServos[3].write(90-40-11);        #right hip
        self.lowerBodyServos[4].write(90+40-11);       #left hip
        self.lowerBodyServos[5].write(90-40+70);        #left upper leg
        self.lowerBodyServos[6].write(90+40-70);        #left lower leg
        self.lowerBodyServos[7].write(90+40-11);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(150);
        #1stand 1(11750)
        self.lowerBodyServos[0].write(90-40);        #right foot
        self.lowerBodyServos[1].write(90-40+0);        #right lower leg
        self.lowerBodyServos[2].write(90+40-0);        #right upper leg
        self.lowerBodyServos[3].write(90-40);        #right hip
        self.lowerBodyServos[4].write(90+40);       #left hip
        self.lowerBodyServos[5].write(90-40+0);        #left upper leg
        self.lowerBodyServos[6].write(90+40);        #left lower leg
        self.lowerBodyServos[7].write(90+40);        #left foot
        self.lowerBodyServos[8].write(90-40);        #low body
        self.lowerBodyServos[9].write(90-40+0);       #upper body
        self.delay(2000);
        
    def lb_transform_human_heli(self):
        # stand 1
        self.lowerBodyServos[0].write(90-40);        # right foot
        self.lowerBodyServos[1].write(90-40);        # right lower leg
        self.lowerBodyServos[2].write(90+40);        # right upper leg
        self.lowerBodyServos[3].write(90-40);        # right hip
        self.lowerBodyServos[4].write(90+40);       # left hip
        self.lowerBodyServos[5].write(90-40);        # left upper leg
        self.lowerBodyServos[6].write(90+40);        # left lower leg
        self.lowerBodyServos[7].write(90+40);        # left foot
        self.lowerBodyServos[8].write(90-40);        # low body
        self.lowerBodyServos[9].write(90-40);       # upper body
        self.delay(10000);
        
        # stand 2
        self.lowerBodyServos[0].write(90-40);        # right foot
        self.lowerBodyServos[1].write(90-40+80);        # right lower leg
        self.lowerBodyServos[2].write(90+40-80);        # right upper leg
        self.lowerBodyServos[3].write(90-40);        # right hip
        self.lowerBodyServos[4].write(90+40);       # left hip
        self.lowerBodyServos[5].write(90-40+80);        # left upper leg
        self.lowerBodyServos[6].write(90+40-80);        # left lower leg
        self.lowerBodyServos[7].write(90+40);        # left foot
        self.lowerBodyServos[8].write(90-40);        # low body
        self.lowerBodyServos[9].write(90-40);       # upper body
        self.delay(500);

        # stand 3
        self.lowerBodyServos[0].write(90-40);        # right foot
        self.lowerBodyServos[1].write(90-40+80);        # right lower leg
        self.lowerBodyServos[2].write(90+40-80);        # right upper leg
        self.lowerBodyServos[3].write(90-40);        # right hip
        self.lowerBodyServos[4].write(90+40);       # left hip
        self.lowerBodyServos[5].write(90-40+80);        # left upper leg
        self.lowerBodyServos[6].write(90+40-80);        # left lower leg
        self.lowerBodyServos[7].write(90+40);        # left foot
        self.lowerBodyServos[8].write(90-40);        # low body
        self.lowerBodyServos[9].write(90-40+90);       # upper body
        self.delay(500);
        
        # stand 4
        self.lowerBodyServos[0].write(90-40);        # right foot
        self.lowerBodyServos[1].write(90-40+80);        # right lower leg
        self.lowerBodyServos[2].write(90+40-80);        # right upper leg
        self.lowerBodyServos[3].write(90-40);        # right hip
        self.lowerBodyServos[4].write(90+40);       # left hip
        self.lowerBodyServos[5].write(90-40+80);        # left upper leg
        self.lowerBodyServos[6].write(90+40-80);        # left lower leg
        self.lowerBodyServos[7].write(90+40);        # left foot
        self.lowerBodyServos[8].write(90-40+85);        # low body
        self.lowerBodyServos[9].write(90-40+90);       # upper body
        self.delay(500);

        # stand 5
        self.lowerBodyServos[0].write(90-40);        # right foot
        self.lowerBodyServos[1].write(90-40+80);        # right lower leg
        self.lowerBodyServos[2].write(90+40-80);        # right upper leg
        self.lowerBodyServos[3].write(90-40);        # right hip
        self.lowerBodyServos[4].write(90+40);       # left hip
        self.lowerBodyServos[5].write(90-40+80);        # left upper leg
        self.lowerBodyServos[6].write(90+40-80);        # left lower leg
        self.lowerBodyServos[7].write(90+40);        # left foot
        self.lowerBodyServos[8].write(90-40+85);        # low body
        self.lowerBodyServos[9].write(90-40+90);       # upper body
        self.delay(500);
        
    def lb_transform_heli_human(self):
        # stand 1
        self.lowerBodyServos[0].write(90-40);        # right foot
        self.lowerBodyServos[1].write(90-40+80);        # right lower leg
        self.lowerBodyServos[2].write(90+40-80);        # right upper leg
        self.lowerBodyServos[3].write(90-40);        # right hip
        self.lowerBodyServos[4].write(90+40);       # left hip
        self.lowerBodyServos[5].write(90-40+80);        # left upper leg
        self.lowerBodyServos[6].write(90+40-80);        # left lower leg
        self.lowerBodyServos[7].write(90+40);        # left foot
        self.lowerBodyServos[8].write(90-40+90);        # low body
        self.lowerBodyServos[9].write(90-40+90);       # upper body
        self.delay(5000);
        
        # stand 2
        self.lowerBodyServos[0].write(90-40);        # right foot
        self.lowerBodyServos[1].write(90-40+80);        # right lower leg
        self.lowerBodyServos[2].write(90+40-80);        # right upper leg
        self.lowerBodyServos[3].write(90-40);        # right hip
        self.lowerBodyServos[4].write(90+40);       # left hip
        self.lowerBodyServos[5].write(90-40+80);        # left upper leg
        self.lowerBodyServos[6].write(90+40-80);        # left lower leg
        self.lowerBodyServos[7].write(90+40);        # left foot
        self.lowerBodyServos[8].write(90-40+90);        # low body
        self.lowerBodyServos[9].write(90-40+90);       # upper body
        self.delay(500);

        # stand 3
        self.lowerBodyServos[0].write(90-40);        # right foot
        self.lowerBodyServos[1].write(90-40+80);        # right lower leg
        self.lowerBodyServos[2].write(90+40-80);        # right upper leg
        self.lowerBodyServos[3].write(90-40);        # right hip
        self.lowerBodyServos[4].write(90+40);       # left hip
        self.lowerBodyServos[5].write(90-40+80);        # left upper leg
        self.lowerBodyServos[6].write(90+40-80);        # left lower leg
        self.lowerBodyServos[7].write(90+40);        # left foot
        self.lowerBodyServos[8].write(90-40);        # low body
        self.lowerBodyServos[9].write(90-40+90);       # upper body
        self.delay(500);

        # stand 12
        self.lowerBodyServos[0].write(90-40);        # right foot
        self.lowerBodyServos[1].write(90-40+80);        # right lower leg
        self.lowerBodyServos[2].write(90+40-80);        # right upper leg
        self.lowerBodyServos[3].write(90-40);        # right hip
        self.lowerBodyServos[4].write(90+40);       # left hip
        self.lowerBodyServos[5].write(90-40+80);        # left upper leg
        self.lowerBodyServos[6].write(90+40-80);        # left lower leg
        self.lowerBodyServos[7].write(90+40);        # left foot
        self.lowerBodyServos[8].write(90-40);        # low body
        self.lowerBodyServos[9].write(90-40+0);       # upper body
        self.delay(500);
    
        # stand 16
        self.lowerBodyServos[0].write(90-40);        # right foot
        self.lowerBodyServos[1].write(90-40+0);        # right lower leg
        self.lowerBodyServos[2].write(90+40-0);        # right upper leg
        self.lowerBodyServos[3].write(90-40);        # right hip
        self.lowerBodyServos[4].write(90+40);       # left hip
        self.lowerBodyServos[5].write(90-40+0);        # left upper leg
        self.lowerBodyServos[6].write(90+40-0);        # left lower leg
        self.lowerBodyServos[7].write(90+40);        # left foot
        self.lowerBodyServos[8].write(90-40);        # low body
        self.lowerBodyServos[9].write(90-40+0);       # upper body
        self.delay(500);

if __name__ == "__main__":
   ravenms=RavenMS()
   ravenms.walk()
   
   ravenms.lb_transform_human_heli()
   
   ravenms.delay(5000)
   
   ravenms.lb_transform_heli_human()
