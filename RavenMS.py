# RavenMS.py: class to control the Raven MS helicopter transformer humanoid robot by Tang Woonthai
# Copyright (C) 2022 Vincent Mistler (YouMakeTech)
# Robot and motion stands by Tang Woonthai: https://youtube.com/shorts/nuiew2s-k3U

from Servo import Servo
from time import sleep

class RavenMS:
    def __init__(self):
        print('RavenMS()')

        # lb  human pose
        self.right_foot=Servo(0,initial_position=90-40,position_min=10,position_max=90)
        self.right_lower_leg=Servo(1,initial_position=90-40,position_min=50,position_max=160)
        self.right_upper_leg=Servo(2,initial_position=90+40,position_min=40,position_max=130)
        self.right_hip=Servo(3,initial_position=90-40,position_min=50,position_max=170)
        self.left_hip=Servo(4,initial_position=90+40,position_min=10,position_max=130)
        self.left_upper_leg=Servo(5,initial_position=90-40,position_min=50,position_max=140)
        self.left_lower_leg=Servo(6,initial_position=90+40,position_min=30,position_max=130)
        self.left_foot=Servo(7,initial_position=90+40,position_min=90,position_max=170)
        self.low_body=Servo(9,initial_position=90-40,position_min=30,position_max=80)
        self.upper_body=Servo(10,initial_position=90-40,position_min=0,position_max=100)
                              
        self.lb_servos=[]
        self.lb_servos.append(self.right_foot)      # 0
        self.lb_servos.append(self.right_lower_leg) # 1
        self.lb_servos.append(self.right_upper_leg) # 2
        self.lb_servos.append(self.right_hip)       # 3
        self.lb_servos.append(self.left_hip)        # 4
        self.lb_servos.append(self.left_upper_leg)  # 5
        self.lb_servos.append(self.left_lower_leg)  # 6
        self.lb_servos.append(self.left_foot)       # 7
        self.lb_servos.append(self.low_body)        # 8
        self.lb_servos.append(self.upper_body)      # 9
        
        # Detach the lower body servos before attaching the upper body
        # to avoid conflict between shared PWM channels
        sleep(0.500)
        for ithServo in self.lb_servos:
            ithServo.detach()
        sleep(0.500)
        
        # ub heli pose (stand 17)
        self.right_lower_arm=Servo(11,initial_position=90+10)
        self.right_arm=Servo(12,initial_position=90-89)
        self.right_shoulder=Servo(13,initial_position=90-80)
        self.sd1=Servo(14,initial_position=90)
        self.sd2=Servo(15,initial_position=90)
        self.sd3=Servo(16,initial_position=90)
        self.left_shoulder=Servo(17,initial_position=90+60)
        self.left_arm=Servo(18,initial_position=90+40)
        self.left_lower_arm=Servo(19,initial_position=90+80)
        self.main_rotor=Servo(20,initial_position=0)
        self.tail_rotor=Servo(21,initial_position=0)
        
        self.ub_servos=[]
        self.ub_servos.append(self.right_lower_arm) # 0
        self.ub_servos.append(self.right_arm)       # 1
        self.ub_servos.append(self.right_shoulder)  # 2
        self.ub_servos.append(self.sd1)             # 3
        self.ub_servos.append(self.sd2)             # 4
        self.ub_servos.append(self.sd3)             # 5
        self.ub_servos.append(self.left_shoulder)   # 6
        self.ub_servos.append(self.left_arm)        # 7
        self.ub_servos.append(self.left_lower_arm)  # 8
        self.ub_servos.append(self.main_rotor)      # 9
        self.ub_servos.append(self.tail_rotor)      # 10
        
        # Detach the upper body servos
        sleep(0.500)
        for ithServo in self.ub_servos:
            ithServo.detach()
        sleep(0.500)
        
        # Re-attach the lower body servos
        sleep(0.500)
        for ithServo in self.lb_servos:
            ithServo.attach()
        sleep(0.500)
        
    def delay(self,ms):
        print('RavenMS.delay(' + str(ms) + ')')
        sleep(ms/1000)
    
    def walk(self):
        print('RavenMS.walk()')
        # 1stand 1(100)
        self.lb_servos[0].write(90-40);        #right foot
        self.lb_servos[1].write(90-40+0);        #right lower leg
        self.lb_servos[2].write(90+40-0);        #right upper leg
        self.lb_servos[3].write(90-40);        #right hip
        self.lb_servos[4].write(90+40);       #left hip
        self.lb_servos[5].write(90-40+0);        #left upper leg
        self.lb_servos[6].write(90+40);        #left lower leg
        self.lb_servos[7].write(90+40);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(1000);
        #2stand 2(1100)
        self.lb_servos[0].write(90-40);        #right foot
        self.lb_servos[1].write(90-40+30);        #right lower leg
        self.lb_servos[2].write(90+40-30);        #right upper leg
        self.lb_servos[3].write(90-40);        #right hip
        self.lb_servos[4].write(90+40);       #left hip
        self.lb_servos[5].write(90-40+30);        #left upper leg
        self.lb_servos[6].write(90+40-30);        #left lower leg
        self.lb_servos[7].write(90+40);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(200);
        #3stand r side(1300)
        self.lb_servos[0].write(90-40-11);        #right foot
        self.lb_servos[1].write(90-40+30);        #right lower leg
        self.lb_servos[2].write(90+40-30);        #right upper leg
        self.lb_servos[3].write(90-40-11);        #right hip
        self.lb_servos[4].write(90+40-11);       #left hip
        self.lb_servos[5].write(90-40+30);        #left upper leg
        self.lb_servos[6].write(90+40-30);        #left lower leg
        self.lb_servos[7].write(90+40-11);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(200);
        #4stand r foot(1500)
        self.lb_servos[0].write(90-40-11);        #right foot
        self.lb_servos[1].write(90-40+30);        #right lower leg
        self.lb_servos[2].write(90+40-30);        #right upper leg
        self.lb_servos[3].write(90-40-11);        #right hip
        self.lb_servos[4].write(90+40-11);       #left hip
        self.lb_servos[5].write(90-40+70);        #left upper leg
        self.lb_servos[6].write(90+40-70);        #left lower leg
        self.lb_servos[7].write(90+40-11);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(150);
        #5stand r foot l foot forward(1650)
        self.lb_servos[0].write(90-40-12);        #right foot
        self.lb_servos[1].write(90-40+30);        #right lower leg
        self.lb_servos[2].write(90+40-30);        #right upper leg
        self.lb_servos[3].write(90-40-12);        #right hip
        self.lb_servos[4].write(90+40-12);       #left hip
        self.lb_servos[5].write(90-40+70);        #left upper leg
        self.lb_servos[6].write(90+40-0);        #left lower leg
        self.lb_servos[7].write(90+40-12);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(150);
        #6stand r foot l foot down(1800)
        self.lb_servos[0].write(90-40-12);        #right foot
        self.lb_servos[1].write(90-40+30);        #right lower leg
        self.lb_servos[2].write(90+40-30);        #right upper leg
        self.lb_servos[3].write(90-40-12);        #right hip
        self.lb_servos[4].write(90+40-12);       #left hip
        self.lb_servos[5].write(90-40+50);        #left upper leg
        self.lb_servos[6].write(90+40-0);        #left lower leg
        self.lb_servos[7].write(90+40-12);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(150);
        #7stand r foot l foot front1(1950)
        self.lb_servos[0].write(90-40-6);        #right foot
        self.lb_servos[1].write(90-40+35);        #right lower leg
        self.lb_servos[2].write(90+40-22.5);        #right upper leg
        self.lb_servos[3].write(90-40-6);        #right hip
        self.lb_servos[4].write(90+40-6);       #left hip
        self.lb_servos[5].write(90-40+35);        #left upper leg
        self.lb_servos[6].write(90+40-22.5);        #left lower leg
        self.lb_servos[7].write(90+40-6);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(100);
        #8stand r foot l foot front2(2050)
        self.lb_servos[0].write(90-40-0);        #right foot
        self.lb_servos[1].write(90-40+40);        #right lower leg
        self.lb_servos[2].write(90+40-15);        #right upper leg
        self.lb_servos[3].write(90-40-0);        #right hip
        self.lb_servos[4].write(90+40-0);       #left hip
        self.lb_servos[5].write(90-40+40);        #left upper leg
        self.lb_servos[6].write(90+40-15);        #left lower leg
        self.lb_servos[7].write(90+40-0);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(100);
        #8stand r foot l foot front3(2150)
        self.lb_servos[0].write(90-40+8);        #right foot
        self.lb_servos[1].write(90-40+45);        #right lower leg
        self.lb_servos[2].write(90+40-7.5);        #right upper leg
        self.lb_servos[3].write(90-40+8);        #right hip
        self.lb_servos[4].write(90+40+8);       #left hip
        self.lb_servos[5].write(90-40+35);        #left upper leg
        self.lb_servos[6].write(90+40-22.5);        #left lower leg
        self.lb_servos[7].write(90+40+8);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(100);
        #10stand l side l foot front(2250)
        self.lb_servos[0].write(90-40+16);        #right foot
        self.lb_servos[1].write(90-40+50);        #right lower leg
        self.lb_servos[2].write(90+40-0);        #right upper leg
        self.lb_servos[3].write(90-40+16);        #right hip
        self.lb_servos[4].write(90+40+16);       #left hip
        self.lb_servos[5].write(90-40+30);        #left upper leg
        self.lb_servos[6].write(90+40-30);        #left lower leg
        self.lb_servos[7].write(90+40+16);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(200);
        #11stand l  foot (2450)
        self.lb_servos[0].write(90-40+16);        #right foot
        self.lb_servos[1].write(90-40+70);        #right lower leg
        self.lb_servos[2].write(90+40-70);        #right upper leg
        self.lb_servos[3].write(90-40+16);        #right hip
        self.lb_servos[4].write(90+40+16);       #left hip
        self.lb_servos[5].write(90-40+30);        #left upper leg
        self.lb_servos[6].write(90+40-30);        #left lower leg
        self.lb_servos[7].write(90+40+16);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(150);
        #12stand l foot r foot forward (2600)
        self.lb_servos[0].write(90-40+19);        #right foot
        self.lb_servos[1].write(90-40+0);        #right lower leg
        self.lb_servos[2].write(90+40-70);        #right upper leg
        self.lb_servos[3].write(90-40+16);        #right hip
        self.lb_servos[4].write(90+40+16);       #left hip
        self.lb_servos[5].write(90-40+30);        #left upper leg
        self.lb_servos[6].write(90+40-30);        #left lower leg
        self.lb_servos[7].write(90+40+19);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(150);
        #13stand l foot r foot down(2750)
        self.lb_servos[0].write(90-40+16);        #right foot
        self.lb_servos[1].write(90-40+0);        #right lower leg
        self.lb_servos[2].write(90+40-50);        #right upper leg
        self.lb_servos[3].write(90-40+16);        #right hip
        self.lb_servos[4].write(90+40+16);       #left hip
        self.lb_servos[5].write(90-40+30);        #left upper leg
        self.lb_servos[6].write(90+40-30);        #left lower leg
        self.lb_servos[7].write(90+40+16);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(150);
        #14stand l foot r foot front1(2900)
        self.lb_servos[0].write(90-40+8);        #right foot
        self.lb_servos[1].write(90-40+7.5);        #right lower leg
        self.lb_servos[2].write(90+40-45);        #right upper leg
        self.lb_servos[3].write(90-40+0);        #right hip
        self.lb_servos[4].write(90+40+8);       #left hip
        self.lb_servos[5].write(90-40+22.5);        #left upper leg
        self.lb_servos[6].write(90+40-35);        #left lower leg
        self.lb_servos[7].write(90+40+8);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(100);
        #5stand l foot r foot front2(3000)
        self.lb_servos[0].write(90-40+0);        #right foot
        self.lb_servos[1].write(90-40+15);        #right lower leg
        self.lb_servos[2].write(90+40-40);        #right upper leg
        self.lb_servos[3].write(90-40+0);        #right hip
        self.lb_servos[4].write(90+40+0);       #left hip
        self.lb_servos[5].write(90-40+15);        #left upper leg
        self.lb_servos[6].write(90+40-40);        #left lower leg
        self.lb_servos[7].write(90+40+0);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(100);
        #16stand l foot r foot front3(3100)
        self.lb_servos[0].write(90-40-5);        #right foot
        self.lb_servos[1].write(90-40+22.5);        #right lower leg
        self.lb_servos[2].write(90+40-35);        #right upper leg
        self.lb_servos[3].write(90-40-5);        #right hip
        self.lb_servos[4].write(90+40-5);       #left hip
        self.lb_servos[5].write(90-40+7.5);        #left upper leg
        self.lb_servos[6].write(90+40-45);        #left lower leg
        self.lb_servos[7].write(90+40-5);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(100);
        #17stand r side r foot front(3200)
        self.lb_servos[0].write(90-40-10);        #right foot
        self.lb_servos[1].write(90-40+30);        #right lower leg
        self.lb_servos[2].write(90+40-30);        #right upper leg
        self.lb_servos[3].write(90-40-10);        #right hip
        self.lb_servos[4].write(90+40-10);       #left hip
        self.lb_servos[5].write(90-40+0);        #left upper leg
        self.lb_servos[6].write(90+40-50);        #left lower leg
        self.lb_servos[7].write(90+40-10);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(250);
        #18stand r foot(3450)
        self.lb_servos[0].write(90-40-11);        #right foot
        self.lb_servos[1].write(90-40+30);        #right lower leg
        self.lb_servos[2].write(90+40-30);        #right upper leg
        self.lb_servos[3].write(90-40-11);        #right hip
        self.lb_servos[4].write(90+40-11);       #left hip
        self.lb_servos[5].write(90-40+70);        #left upper leg
        self.lb_servos[6].write(90+40-70);        #left lower leg
        self.lb_servos[7].write(90+40-11);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(150);
        #1stand 1(11750)
        self.lb_servos[0].write(90-40);        #right foot
        self.lb_servos[1].write(90-40+0);        #right lower leg
        self.lb_servos[2].write(90+40-0);        #right upper leg
        self.lb_servos[3].write(90-40);        #right hip
        self.lb_servos[4].write(90+40);       #left hip
        self.lb_servos[5].write(90-40+0);        #left upper leg
        self.lb_servos[6].write(90+40);        #left lower leg
        self.lb_servos[7].write(90+40);        #left foot
        self.lb_servos[8].write(90-40);        #low body
        self.lb_servos[9].write(90-40+0);       #upper body
        self.delay(2000);
        
    def lb_transform_human_heli(self):
        # stand 1
        self.lb_servos[0].write(90-40);        # right foot
        self.lb_servos[1].write(90-40);        # right lower leg
        self.lb_servos[2].write(90+40);        # right upper leg
        self.lb_servos[3].write(90-40);        # right hip
        self.lb_servos[4].write(90+40);       # left hip
        self.lb_servos[5].write(90-40);        # left upper leg
        self.lb_servos[6].write(90+40);        # left lower leg
        self.lb_servos[7].write(90+40);        # left foot
        self.lb_servos[8].write(90-40);        # low body
        self.lb_servos[9].write(90-40);       # upper body
        self.delay(10000);
        
        # stand 2
        self.lb_servos[0].write(90-40);        # right foot
        self.lb_servos[1].write(90-40+80);        # right lower leg
        self.lb_servos[2].write(90+40-80);        # right upper leg
        self.lb_servos[3].write(90-40);        # right hip
        self.lb_servos[4].write(90+40);       # left hip
        self.lb_servos[5].write(90-40+80);        # left upper leg
        self.lb_servos[6].write(90+40-80);        # left lower leg
        self.lb_servos[7].write(90+40);        # left foot
        self.lb_servos[8].write(90-40);        # low body
        self.lb_servos[9].write(90-40);       # upper body
        self.delay(500);

        # stand 3
        self.lb_servos[0].write(90-40);        # right foot
        self.lb_servos[1].write(90-40+80);        # right lower leg
        self.lb_servos[2].write(90+40-80);        # right upper leg
        self.lb_servos[3].write(90-40);        # right hip
        self.lb_servos[4].write(90+40);       # left hip
        self.lb_servos[5].write(90-40+80);        # left upper leg
        self.lb_servos[6].write(90+40-80);        # left lower leg
        self.lb_servos[7].write(90+40);        # left foot
        self.lb_servos[8].write(90-40);        # low body
        self.lb_servos[9].write(90-40+90);       # upper body
        self.delay(500);
        
        # stand 4
        self.lb_servos[0].write(90-40);        # right foot
        self.lb_servos[1].write(90-40+80);        # right lower leg
        self.lb_servos[2].write(90+40-80);        # right upper leg
        self.lb_servos[3].write(90-40);        # right hip
        self.lb_servos[4].write(90+40);       # left hip
        self.lb_servos[5].write(90-40+80);        # left upper leg
        self.lb_servos[6].write(90+40-80);        # left lower leg
        self.lb_servos[7].write(90+40);        # left foot
        self.lb_servos[8].write(90-40+85);        # low body
        self.lb_servos[9].write(90-40+90);       # upper body
        self.delay(500);

        # stand 5
        self.lb_servos[0].write(90-40);        # right foot
        self.lb_servos[1].write(90-40+80);        # right lower leg
        self.lb_servos[2].write(90+40-80);        # right upper leg
        self.lb_servos[3].write(90-40);        # right hip
        self.lb_servos[4].write(90+40);       # left hip
        self.lb_servos[5].write(90-40+80);        # left upper leg
        self.lb_servos[6].write(90+40-80);        # left lower leg
        self.lb_servos[7].write(90+40);        # left foot
        self.lb_servos[8].write(90-40+85);        # low body
        self.lb_servos[9].write(90-40+90);       # upper body
        self.delay(500);
        
    def lb_transform_heli_human(self):
        # stand 1
        self.lb_servos[0].write(90-40);        # right foot
        self.lb_servos[1].write(90-40+80);        # right lower leg
        self.lb_servos[2].write(90+40-80);        # right upper leg
        self.lb_servos[3].write(90-40);        # right hip
        self.lb_servos[4].write(90+40);       # left hip
        self.lb_servos[5].write(90-40+80);        # left upper leg
        self.lb_servos[6].write(90+40-80);        # left lower leg
        self.lb_servos[7].write(90+40);        # left foot
        self.lb_servos[8].write(90-40+90);        # low body
        self.lb_servos[9].write(90-40+90);       # upper body
        self.delay(5000);
        
        # stand 2
        self.lb_servos[0].write(90-40);        # right foot
        self.lb_servos[1].write(90-40+80);        # right lower leg
        self.lb_servos[2].write(90+40-80);        # right upper leg
        self.lb_servos[3].write(90-40);        # right hip
        self.lb_servos[4].write(90+40);       # left hip
        self.lb_servos[5].write(90-40+80);        # left upper leg
        self.lb_servos[6].write(90+40-80);        # left lower leg
        self.lb_servos[7].write(90+40);        # left foot
        self.lb_servos[8].write(90-40+90);        # low body
        self.lb_servos[9].write(90-40+90);       # upper body
        self.delay(500);

        # stand 3
        self.lb_servos[0].write(90-40);        # right foot
        self.lb_servos[1].write(90-40+80);        # right lower leg
        self.lb_servos[2].write(90+40-80);        # right upper leg
        self.lb_servos[3].write(90-40);        # right hip
        self.lb_servos[4].write(90+40);       # left hip
        self.lb_servos[5].write(90-40+80);        # left upper leg
        self.lb_servos[6].write(90+40-80);        # left lower leg
        self.lb_servos[7].write(90+40);        # left foot
        self.lb_servos[8].write(90-40);        # low body
        self.lb_servos[9].write(90-40+90);       # upper body
        self.delay(500);

        # stand 12
        self.lb_servos[0].write(90-40);        # right foot
        self.lb_servos[1].write(90-40+80);        # right lower leg
        self.lb_servos[2].write(90+40-80);        # right upper leg
        self.lb_servos[3].write(90-40);        # right hip
        self.lb_servos[4].write(90+40);       # left hip
        self.lb_servos[5].write(90-40+80);        # left upper leg
        self.lb_servos[6].write(90+40-80);        # left lower leg
        self.lb_servos[7].write(90+40);        # left foot
        self.lb_servos[8].write(90-40);        # low body
        self.lb_servos[9].write(90-40+0);       # upper body
        self.delay(500);
    
        # stand 16
        self.lb_servos[0].write(90-40);        # right foot
        self.lb_servos[1].write(90-40+0);        # right lower leg
        self.lb_servos[2].write(90+40-0);        # right upper leg
        self.lb_servos[3].write(90-40);        # right hip
        self.lb_servos[4].write(90+40);       # left hip
        self.lb_servos[5].write(90-40+0);        # left upper leg
        self.lb_servos[6].write(90+40-0);        # left lower leg
        self.lb_servos[7].write(90+40);        # left foot
        self.lb_servos[8].write(90-40);        # low body
        self.lb_servos[9].write(90-40+0);       # upper body
        self.delay(500);

if __name__ == "__main__":
   ravenms=RavenMS()
#   ravenms.walk()
   
   ravenms.lb_transform_human_heli()
   
   ravenms.delay(5000)
   
   ravenms.lb_transform_heli_human()
