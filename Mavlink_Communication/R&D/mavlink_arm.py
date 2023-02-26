from pymavlink import mavutil
import time

print("Before connection")

# master = mavutil.mavlink_connection('/dev/serial/by-id/usb-NXP_SEMICONDUCTORS_PX4_FMUK66_v3.x_0-if00')
master = mavutil.mavlink_connection('udpin:localhost:14540')

print("After connection")

master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))

#the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)

#msg = the_connection.recv_match(type='COMMAND_ACK',blocking=True)
#print(msg)

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 1, 0, 0, 0, 0, 0)

# wait until arming confirmed (can manually check with master.motors_armed())
print("Waiting for the vehicle to arm")
#master.motors_armed_wait()
print('Armed!')
msg = master.recv_match(type='COMMAND_ACK',blocking=True)
print(msg)

time.sleep(5)

print("DISARM !!!")

# Disarm
# master.arducopter_disarm() or: 
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    0, 0, 0, 0, 0, 0, 0)


