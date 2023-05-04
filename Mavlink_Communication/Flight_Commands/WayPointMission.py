import math
from pymavlink import mavutil
from math import radians, sin, cos, sqrt, atan2

def compute_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    # print(lat1, type(lat1))
    # print(lat2, type(lat2))
    # print(lon1, type(lon1))
    # print(lon2, type(lon2))

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    distance = c * r * 1000 # convert to meters

    return distance

def waypoint_verification(waypoints, latitude, longitude):
    
    for waypoint in waypoints:
        print("\n--------------")
        print(waypoint)
        if compute_distance(waypoint["lat"], waypoint["lng"], latitude, longitude) > 40:
            return False
        
    print("Waypoints verified successfully")
    
    return True
    

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

    upload_mission(master, mission_waypoints)

    start_mission(master)