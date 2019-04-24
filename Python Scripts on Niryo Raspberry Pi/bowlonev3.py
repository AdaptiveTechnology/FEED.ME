#!/usr/bin/env python

from niryo_one_python_api.niryo_one_api import *
import rospy
rospy.init_node('niryo_one_run_python_api_code')

n = NiryoOne()

n.move_joints([-0.021, 0.613, -0.245, 0.04, 0.53, 0.081])
n.move_joints([0.182, -0.71, 0.043000000000000003, 0.299, -0.611, -0.162])
n.move_joints([0.341, -1.125, 0.234, 0.7030000000000001, -0.539, 1.179])
n.move_joints([0.28, -1.178, 0.231, 0.757, -0.527, 0.116])
n.move_joints([0.201, -1.127, 0.167, 0.7030000000000001, -0.507, -0.405])
n.move_joints([0.152, -1.217, 0.03, 0.146, -1.243, -0.07100000000000001])
n.move_joints([0.985, -0.43, -0.16, -0.866, -0.713, 0.744])  
