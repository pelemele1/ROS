import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/robotserver/Desktop/git/ROS/create3_examples_ws/install/create3_teleop'
