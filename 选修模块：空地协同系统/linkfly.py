from robomaster import robot
import robomaster
if __name__=='__main__':
	robomaster.config.LOCAL_IP_STR='192.168.10.2'
	tl_drone=robot.Drone()
	tl_drone.initialize()
	version=tl_drone.get_sdk_version()
	print("SDK version:{0}".format(version))
	tl_drone.close()
