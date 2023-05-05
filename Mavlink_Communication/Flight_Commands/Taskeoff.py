from pymavlink import mavutil
from Flight_Commands.ACK import *
import Flight_Commands.global_variables as GVar
import time

def takeoff(master):

    print("\n-----------------------------")
    print("Aquiring the current position...")
    lat_float = 0.0
    lon_float = 0.0

    # msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True, timeout = 1)
    # if msg:
    #     print("Current position: ")
    #     print("Latitude: ", msg.lat)
    #     print("Longitude: ", msg.lon)
    #     lat_float = msg.lat/10**7
    #     lon_float = msg.lon/10**7
    #     print("Latitude: ", lat_float )
    #     print("Longitude: ", lon_float)

    lat_float = GVar.latitude
    lon_float = GVar.longitude

    if lat_float != "not available yet":

        counter = 0
        while counter < 5:

            print("Try number: ", counter+1)
        
            master.mav.command_long_send(
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
                0,
                0, 0, 0, 0, lat_float, lon_float, 4)
            print("TAKEOFF Command sent")

            if ack(master, "COMMAND_ACK", True, 0.5):
                break

            counter += 1
    
    else:
        print("Not a valid position estimated yet")