#!/usr/bin/env python2
import rospy,sys
import moveit_commander
from geometry_msgs.msg import Pose
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

rospy.init_node('grasp_object')
arm = moveit_commander.MoveGroupCommander("manipulator")
grp = moveit_commander.MoveGroupCommander("gripper")
grp.set_named_target('open')
grp.go(wait=True)
arm.set_named_target('base')
arm.go(wait=True)
arm.set_joint_value_target([-0.21957805043352518, -1.097296859939564, 1.8945345194815335,
                            -2.366067038969164, -1.571228181260084, -1.0061550793898952])
arm.go(wait=True)
pose = arm.get_current_pose().pose
pose.position.z -= 0.05
arm.set_pose_target(pose)
arm.go(wait=True)
grp.set_named_target('close')
grp.go(wait=True)
pose = arm.get_current_pose().pose
pose.position.z += 0.05
arm.set_pose_target(pose)
arm.go(wait=True)
