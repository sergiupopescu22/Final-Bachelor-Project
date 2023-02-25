from pymavlink import mavutil

# Connect to the vehicle
connection = mavutil.mavlink_connection('udp:0.0.0.0:14550')  # Replace with the address of your drone

# Wait for the connection to be established
connection.wait_heartbeat()

# Set the target position to San Francisco, CA
lat = 317737600  # 37.7749 degrees N scaled by 1e7
lon = -1224192000  # 122.4194 degrees W scaled by 1e7
alt = 10  # 10 meters above mean sea level
yaw = 0  # Heading angle in radians
vx, vy, vz = 0, 0, 0  # Zero velocity in all directions

# Create the message
msg = connection.mav.set_position_target_global_int_encode(
    0,  # Timestamp (not used)
    1,  # Target system ID (can be any value)
    1,  # Target component ID (can be any value)
    mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,  # Coordinate frame
    0b0000111111111000,  # Use only position and yaw fields
    lat,  # Target latitude in WGS84 coordinates
    lon,  # Target longitude in WGS84 coordinates
    alt,  # Target altitude above mean sea level
    vx,  # Target velocity in x direction (North)
    vy,  # Target velocity in y direction (East)
    vz,  # Target velocity in z direction (Down)
    0,  # Target acceleration in x direction (not used)
    0,  # Target acceleration in y direction (not used)
    0,  # Target acceleration in z direction (not used)
    yaw,  # Target yaw angle
    0,  # Target yaw rate (not used)

)

# Send the message
connection.mav.send(msg)