
#!/usr/bin/env python

from niryo_one_python_api.niryo_one_api import *
import rospy
rospy.init_node('niryo_one_run_python_api_code')

n = NiryoOne()
 
n.move_joints([-0.021, 0.613, -0.245, 0.04, 0.53, 0.081])
