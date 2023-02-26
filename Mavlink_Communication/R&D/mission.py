import math
from pymavlink import mavutil
import time

#class for fromating the Mission Item
class mission_item:
    def __init__(self, i, current, x, y, z):
        self.seq = i
        self.frame = mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT
        self.command = mavutil.mavlink.MAV_CMD_NAV_WAYPOINT
        self.current = current
        self.auto = 1
        self.param1 = 0.0
        self.param2 = 2.00
        self.param3 = 20.00
        self.param4 = math.nan
        self.param5 = x
        self.param6 = y
        self.param7 = z
        self.mission_type = 0

def arm (the_connection):
    print("-- Arming")

    the_connection.mav.command_long_send(
        the_connection.target_system,
        the_connection.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0, 1, 0, 0, 0, 0, 0 ,0)
    
    ack(the_connection, "COMMAND_ACK")

# def takeoff (the_connection):
    
#     print("-- Takeoff Initiated")

#     the_connection.mav.command_long_send(
#         the_connection.target_system,
#         the_connection.target_component,
#         mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
#         0, 0, 0, 0, math.nan, 0, 0 ,5)
    
#     ack(the_connection, "COMMAND_ACK")

def upload_mission (the_connection, mission_items):

    n = len(mission_items)
    print("-- Sending Message out")
    print("-- Nr of waypoints: ", n)

    the_connection.mav.mission_count_send(
        the_connection.target_system, 
        the_connection.target_component,
        n,
        0
    )

    ack(the_connection, "MISSION_REQUEST")

    for waypoint in mission_items:
        print("-- Creating a waypoint")

        the_connection.mav.mission_item_send(
            the_connection.target_system,
            the_connection.target_component,
            waypoint.seq,
            waypoint.frame,
            waypoint.command,
            waypoint.current,
            waypoint.auto,
            waypoint.param1,
            waypoint.param2,
            waypoint.param3,
            waypoint.param4,
            waypoint.param5,
            waypoint.param6,
            waypoint.param7,
            waypoint.mission_type
        )

        print("-- Waiting for waypoint confirmation ")
        
        if waypoint != mission_items[n-1]:
            print("got here")
            ack(the_connection, "MISSION_REQUEST")

    print("print 2 ")
    # ack(the_connection, "MISSION_REQUEST")
    ack(the_connection, "MISSION_ACK")

def set_return(the_connection):
    print("-- Set Return To Launch")
    the_connection.mav.command_long_send(
        the_connection.target_system,
        the_connection.target_component,
        mavutil.mavlink.MAV_CMA_NAV_RETURN_TO_LAUNCH,
        0, 0, 0, 0, 0, 0, 0, 0)
    
    ack(the_connection, "COMMAND_ACK")

def start_mission(the_connection):
    print("-- Mission Start")
    the_connection.mav.command_long_send(
        the_connection.target_system,
        the_connection.target_component,
        mavutil.mavlink.MAV_CMD_MISSION_START,
        0, 0, 0, 0, 0, 0, 0, 0)


def ack (the_connection, keyword):
    print("-- NEW MESSAGE: " + str(the_connection.recv_match(type=keyword, blocking=True)))

def takeoff(master):

    print("\n-----------------------------")
    print("Aquiring the current position...")
    lat_float = 0.0
    lon_float = 0.0

    msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True, timeout = 1)
    if msg:
        print("Current position: ")
        print("Latitude: ", msg.lat)
        print("Longitude: ", msg.lon)
        lat_float = msg.lat/10**7
        lon_float = msg.lon/10**7
        print("Latitude: ", lat_float )
        print("Longitude: ", lon_float)

    counter = 0
    while counter < 5:

        print("Try number: ", counter+1)
    
        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
            0,
            0, 0, 0, 0, lat_float, lon_float, 5)
        print("ARM Command sent")

        print('Waiting for confirmation...')
        msg = master.recv_match(type='COMMAND_ACK',blocking=True, timeout=0.5)
        if msg:
            print(msg)
            break

        else:
            print("Command failed! Trying again...\n")

        counter += 1

if __name__ == "__main__":
    print("-- Program Started")
    the_connection = mavutil.mavlink_connection('udpin:localhost:14540')


    while(the_connection.target_system == 0):
        print("-- Checking Heartbeat")
        the_connection.wait_heartbeat()
        print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

    mission_waypoints = []

    mission_waypoints.append(
        mission_item(0, 0, 47.397499, 8.544877, 5))
    mission_waypoints.append(
        mission_item(1, 0, 47.397789, 8.543417, 5))
    
    upload_mission(the_connection, mission_waypoints)
    
    
    # arm(the_connection)

    # time.sleep(2)

    # takeoff(the_connection)


    # time.sleep(3)

    # upload_mission(the_connection, mission_waypoints)

    time.sleep(2)


    start_mission(the_connection)

    for mission_item in mission_waypoints:

        print("-- Message Read " +
              str(the_connection.recv_match(
                type = "MISSION_ITEAM_REACHED"
              ))) 
