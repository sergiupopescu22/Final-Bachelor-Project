import Flight_Commands.global_variables as GVar
from pymavlink import mavutil
import sys

from Flight_Commands.global_variables import *

def create_connection(ngrok):
    print("\n-----------------------")
    print("Establishing Connection to Flight Controller...")
    global master

    print("Connection mode: ", GVar.action_type)

    connection_string = ""

    if GVar.action_type == "simulation":
        connection_string = 'udpin:localhost:14540'
    
    elif GVar.action_type == "real-life-win":
        connection_string = '/dev/serial/by-id/usb-NXP_SEMICONDUCTORS_PX4_FMUK66_v3.x_0-if00'

    elif GVar.action_type == "real-life-rb":
        connection_string = '/dev/serial/by-id/usb-NXP_SEMICONDUCTORS_PX4_FMUK66_v3.x_0-if00'

    try: 
        print("Connected to: ", connection_string)
        master = mavutil.mavlink_connection(connection_string)

        print("\n--> UDP data flow started! Waiting for confirmation heartbeat...")

        while(master.target_system == 0):
            print("\n--> Checking Heartbeat...")
            master.wait_heartbeat()
            print("\n--> Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))

        # master.wait_heartbeat()
        # print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))
        print("\nCONNECTION IS OK!")

        return master

    except:

        print("\nCOULD NOT ESTABLISH A CONNECTION WITH THE FLIGHT CONTROLLER :(\n")
        ngrok.kill()

        sys.exit()



    

    