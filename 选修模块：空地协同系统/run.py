import rospy
import robomaster
from time import sleep
from rospy_message_converter import message_converter
from geometry_msgs.msg import TransformStamped
from robomaster import robot

def callback_sans(data):
	global x_sans
	global y_sans
	received_data = message_converter.convert_ros_message_to_dictionary(data)
	x_sans = received_data['transform']['translation']['x']
	y_sans = received_data['transform']['translation']['y']
	
def callback_pyparus(data):
	global x_pyparus
	global y_pyparus
	received_data = message_converter.convert_ros_message_to_dictionary(data)
	x_pyparus = received_data['transform']['translation']['x']
	y_pyparus = received_data['transform']['translation']['y']

if __name__ == '__main__':
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('/vicon/sans/sans', TransformStamped, callback_sans)
	rospy.Subscriber('/vicon/pyparus/pyparus', TransformStamped, callback_pyparus)
	
	ep_robot=robot.Robot()
	ep_robot.initialize(conn_type="sta",sn="3JKCK1600302MR")
	ep_chassis=ep_robot.chassis
	ep_blaster=ep_robot.blaster
	
	while(1): 
		x_val=x_pyparus-x_sans
		y_val=y_pyparus-y_sans	
			
		ep_chassis.move(x=-y_val,y=0,z=0,xy_speed=1).wait_for_completed()
		ep_chassis.move(x=0,y=-x_val,z=0,xy_speed=1).wait_for_completed()

  
		if x_val<0.01 and y_val<0.01:
			break
	ep_chassis.move(x=0,y=0,z=30,z_speed=45).wait_for_completed()
	ep_blaster.fire(fire_type="water",times=5)
 
	ep_robot.close()

