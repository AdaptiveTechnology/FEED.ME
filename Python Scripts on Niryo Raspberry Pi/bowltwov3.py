
#!/usr/bin/env python

from niryo_one_python_api.niryo_one_api import *
import rospy
rospy.init_node('niryo_one_run_python_api_code')

n = NiryoOne()

n.move_joints([-0.021, 0.613, -0.245, 0.04, 0.53, 0.081])
n.move_joints([-0.035, -1.075, 0.248, 0.28400000000000003, -0.313, 1.356])
n.move_joints([-0.097, -1.1500000000000001, 0.211, 0.367, -0.439, 0.8200000000000001])
n.move_joints([-0.201, -1.1320000000000001, 0.162, 0.192, -0.511, 0.035])
n.move_joints([-0.129, -1.224, 0.024, 0.074, -1.223, 0.162])
n.move_joints([-0.129, -0.913, 0.059000000000000004, 0.146, -0.763, 0.02])
n.move_joints([0.985, -0.43, -0.16, -0.866, -0.713, 0.744]) 
