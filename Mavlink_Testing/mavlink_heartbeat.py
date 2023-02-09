from pymavlink import mavutil
import time

print("Before connection")

the_connection = mavutil.mavlink_connection('/dev/serial/by-id/usb-NXP_SEMICONDUCTORS_PX4_FMUK66_v3.x_0-if00')

print("After connection")

the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

while 1:
	the_connection.wait_heartbeat()
	print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

	msg = the_connection.recv_match(blocking=True)
	print(msg.to_dict())