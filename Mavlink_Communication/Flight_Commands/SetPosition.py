from pymavlink import mavutil

def go_to_location(master):
    print("\n-----------------------------")
    print("Aquiring the current position...")
    lat_float = 0.0
    lon_float = 0.0
    lat = 0
    lon = 0
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
    while counter < 10:

        print("Try number: ", counter+1)

        lat = 0  # 37.7749 degrees N scaled by 1e7
        lon = 0  # 122.4194 degrees W scaled by 1e7
        alt = 10  # 10 meters above mean sea level
        yaw = 0.0  # Heading angle in radians
        vx, vy, vz = 0, 0, 0  # Zero velocity in all directions

        # Create the message
        # msg = master.mav.set_position_target_global_int_encode(
        master.mav.command_long_send(
                0,  # Timestamp (not used)
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_FRAME_GLOBAL_INT,  # Coordinate frame
                int(0b110111111000),  # Use only position and yaw fields
                4739795, 85436,  # Target latitude in WGS84 coordinates
                  # Target longitude in WGS84 coordinates
                alt,  # Target altitude above mean sea level
                vx,  # Target velocity in x direction (North)
                vy,  # Target velocity in y direction (East)
                vz,  # Target velocity in z direction (Down)
                0,  # Target acceleration in x direction (not used)
                0,  # Target acceleration in y direction (not used)
                0,  # Target acceleration in z direction (not used)
                yaw,  # Target yaw angle
                0.0,  # Target yaw rate (not used)
            )

        # Send the message to the drone
        
        # master.mav.send(msg)
        print("Land Command sent")

        print('Waiting for confirmation...')
        msg = master.recv_match(type='COMMAND_ACK',blocking=True, timeout=0.5)
        if msg:
            print(msg)
            break

        else:
            print("Command failed! Trying again...\n")

        counter += 1