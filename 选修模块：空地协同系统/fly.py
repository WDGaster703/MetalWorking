from robomaster import robot
import robomaster
import time
if __name__=='__main__':
	robomaster.config.LOCAL_IP_STR="192.168.10.2"
	tl_drone=robot.Drone()
	tl_drone.initialize()
	tl_flight=tl_drone.flight

	tl_flight.takeoff().wait_for_completed()
	tl_flight.rc(a=40,b=0,c=0,d=0)
	time.sleep(3)
	tl_flight.rc(a=0,b=0,c=0,d=0)
	tl_flight.rc(a=0,b=40,c=0,d=0)
	time.sleep(3)
	tl_flight.rc(a=0,b=0,c=0,d=0)
	tl_flight.rc(a=-40,b=0,c=0,d=0)
	time.sleep(3)
	tl_flight.rc(a=0,b=0,c=0,d=0)
	tl_flight.rc(a=0,b=-40,c=0,d=0)
	time.sleep(3)
	tl_flight.rc(a=0,b=0,c=0,d=0)
	tl_flight.land().wait_for_completed()
	tl_drone.close()
