#!/usr/bin/env python

#State Machine for Robot

import rospy
from std_msgs.msg import String

state = ''  ## state variable

def handleData(data):
    state = data.data  ## Copy Received data to state variable

def StateMachine():
    rospy.init_node('StateMachine')
    rospy.Subscriber("State", String, handleData)

    while (True):
        if (state == 'Teleoperated'):
            pass # Insert Teleoperated Call Here
        elif (state == 'Autonomous'):
            pass # Insert Autonomous Call Here
        elif (state == 'ArmControl'):
            pass # Insert Arm Control Here
        else:
            pass # State does not exist, perform some sort of error handling
        rospy.spinOnce()

if __name__ == '__main__':
    StateMachine()
