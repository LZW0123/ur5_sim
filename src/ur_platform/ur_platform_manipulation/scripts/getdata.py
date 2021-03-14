#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from sensor_msgs.msg import JointState

def callback(data):
    rospy.loginfo(data.position)
    
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    # float pos[3],vel[3]
    # pos[0]=data.position
#   pos=msg.position
#   pos[0]=msg.position[0]
#   pos[1]=msg->position[1]
#   pos[2]=msg->position[2]
#   vel[0]=msg->velocity[0]
#   vel[1]=msg->velocity[1]
#   vel[2]=msg->velocity[2]
#   ROS_INFO("I heard: [%f] [%f] [%f] [%f] [%f] [%f]",pos[0],pos[1],pos[2],vel[0],vel[1],vel[2])


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/joint_states", JointState, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()