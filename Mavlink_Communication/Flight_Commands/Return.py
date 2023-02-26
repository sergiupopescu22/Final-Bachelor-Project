from pymavlink import mavutil
from Flight_Commands.ACK import *

def set_return(the_connection):
    print("-- Set Return To Launch")
    the_connection.mav.command_long_send(
        the_connection.target_system,
        the_connection.target_component,
        mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,
        0, 0, 0, 0, 0, 0, 0, 0)
    
    ack(the_connection, "COMMAND_ACK", True, 0.5)
    
    