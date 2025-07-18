from robomaster import robot
import robomaster
import time

if __name__=='__main__':
	ep_robot=robot.Robot()
	ep_robot.initialize(conn_type="sta",sn="3JKCK1600302MR")
	ep_chassis=ep_robot.chassis
	ep_blaster=ep_robot.blaster

	x_val=0.5
	y_val=0.5
	z_val=30
	
	ep_chassis.move(x=x_val,y=0,z=0,xy_speed=0.7).wait_for_completed()
	ep_chassis.move(x=0,y=-y_val,z=0,xy_speed=0.7).wait_for_completed()
	ep_chassis.move(x=0,y=0,z=z_val,z_speed=45).wait_for_completed()
	ep_blaster.fire(fire_type="water",times=5)
	
	ep_robot.close()
