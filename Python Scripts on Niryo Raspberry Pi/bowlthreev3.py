#!/usr/bin/env python

from niryo_one_python_api.niryo_one_api import *
import rospy
rospy.init_node('niryo_one_run_python_api_code')

n = NiryoOne()

n.move_joints([-0.021, 0.613, -0.245, 0.04, 0.53, 0.081])
n.move_joints([-0.352, -0.842, 0.10200000000000001, 0.018000000000000002, -0.6910000000000001, 0.132])
n.move_joints([-0.371, -1.201, 0.47300000000000003, -0.20400000000000001, 0.078, 1.291])
n.move_joints([-0.446, -1.268, 0.47000000000000003, -0.2, -0.123, 0.339])
n.move_joints([-0.444, -1.369, 0.384, -0.18, -1.04, 0.066])
n.move_joints([-0.453, -1.041, 0.14200000000000002, -0.048, -0.935, 0.106])
n.move_joints([0.985, -0.43, -0.16, -0.866, -0.713, 0.744]) 
