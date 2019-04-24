#!/usr/bin/env python

from niryo_one_python_api.niryo_one_api import *
import rospy
rospy.init_node('niryo_one_run_python_api_code')

n = NiryoOne()

n.calibrate_manual()  

