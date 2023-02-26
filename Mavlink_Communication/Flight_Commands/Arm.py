from pymavlink import mavutil
from Flight_Commands.ACK import *

def arm_drone(master):

    print("\n-----------------------------")
    counter = 0
    while counter < 5:

        print("Try number: ", counter+1)
    
        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            1, 1, 0, 0, 0, 0, 0)
        print("ARM Command sent")

        if ack(master, "COMMAND_ACK", True, 0.5):
            break

        counter += 1