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

def upload_mission (the_connection, mission_items):

    n = len(mission_items)
    print("\n-----------------------")
    print("Sending Request for Mission...")
    print("Nr of waypoints: ", n)

    the_connection.mav.mission_count_send(
        the_connection.target_system, 
        the_connection.target_component,
        n,
        0
    )
    ack(the_connection, "MISSION_REQUEST")


    print("\n-----------------------")
    for waypoint in mission_items:
        print("Creating a waypoint")

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

        print("Sent waypoint request. Waiting for waypoint confirmation... ")
        
        if waypoint != mission_items[n-1]:
            ack(the_connection, "MISSION_REQUEST")

    ack(the_connection, "MISSION_ACK")

def start_mission(the_connection):
    print("-- Mission Start")
    the_connection.mav.command_long_send(
        the_connection.target_system,
        the_connection.target_component,
        mavutil.mavlink.MAV_CMD_MISSION_START,
        0, 0, 0, 0, 0, 0, 0, 0)

def ack (the_connection, keyword):
    print("CONFIRMATION MESSAGE: " + str(the_connection.recv_match(type=keyword, blocking=True)))

def waypoint_mission(master, waypoints):

    mission_waypoints = []
    index = 0

    for waypoint in waypoints:
        mission_waypoints.append(
            mission_item(index, 0, waypoint['lat'], waypoint['lng'], 5))
        print(waypoint)
        index += 1

    # mission_waypoints.append(
    #     mission_item(0, 0, 47.397801, 8.545298, 5))
    # mission_waypoints.append(
    #     mission_item(1, 0, 47.397878, 8.544912, 5))
    # mission_waypoints.append(
    #     mission_item(2, 0, 47.398097, 8.545304, 5))

    upload_mission(master, mission_waypoints)

    start_mission(master)