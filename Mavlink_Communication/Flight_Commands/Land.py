from pymavlink import mavutil
from Flight_Commands.ACK import *
import Flight_Commands.global_variables as GVar

def land(master):
    print("\n-----------------------------")
    print("Aquiring the current position...")
    lat_float = 0.0
    lon_float = 0.0

    lat_float = GVar.latitude
    lon_float = GVar.longitude

    counter = 0
    while counter < 5:

        print("Try number: ", counter+1)
    
        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_NAV_LAND,
            0,
            0, 0, 0, 0, lat_float, lon_float, 5)
        print("Land Command sent")

        if ack(master, "COMMAND_ACK", True, 0.5):
            GVar.emergency_land = True
            break

        counter += 1
    