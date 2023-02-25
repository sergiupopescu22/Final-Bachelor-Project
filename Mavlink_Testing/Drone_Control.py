from pymavlink import mavutil
import time

master = ""

def create_connection():
    print("\n-----------------------")
    print("Establishing Connection to Flight Controller...")

    # master = mavutil.mavlink_connection('/dev/serial/by-id/usb-NXP_SEMICONDUCTORS_PX4_FMUK66_v3.x_0-if00')
    global master
    master = mavutil.mavlink_connection('udpin:localhost:14540')

    print("Connection created! Waiting for confirmation heartbeat...")

    master.wait_heartbeat()
    print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))
    print("Connection is OK!")

def arm_drone():

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

        print('Waiting for confirmation...')
        msg = master.recv_match(type='COMMAND_ACK',blocking=True, timeout=0.5)
        if msg:
            print(msg)
            break

        else:
            print("Command failed! Trying again...\n")

        counter += 1
    
def disarm_drone():
    print("\n-----------------------------")
    counter = 0
    while counter < 5:

        print("Try number: ", counter+1)
    
        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            0, 21196, 0, 0, 0, 0, 0)
        print("DISARM Command sent")
        
        print('Waiting for confirmation...')
        msg = master.recv_match(type='COMMAND_ACK',blocking=True, timeout=0.5)
        if msg:
            print(msg)
            break

        else:
            print("Command failed! Trying again...\n")

        counter += 1
        # time.sleep(0.5)

def show_messages():
    while True:
        # msg = master.recv_match(type='LOCAL_POSITION_NED', blocking=True)
        msg = master.recv_match()
        print(msg)

def takeoff():

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

def land():
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
            mavutil.mavlink.MAV_CMD_NAV_LAND,
            0,
            0, 0, 0, 0, lat_float, lon_float, 5)
        print("Land Command sent")

        print('Waiting for confirmation...')
        msg = master.recv_match(type='COMMAND_ACK',blocking=True, timeout=0.5)
        if msg:
            print(msg)
            break

        else:
            print("Command failed! Trying again...\n")

        counter += 1

def go_to_location():
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
        msg = master.mav.set_position_target_global_int_encode(
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
        
        master.mav.send(msg)
        print("Land Command sent")

        print('Waiting for confirmation...')
        msg = master.recv_match(type='COMMAND_ACK',blocking=True, timeout=0.5)
        if msg:
            print(msg)
            break

        else:
            print("Command failed! Trying again...\n")

        counter += 1

def main():
    print("\n-----------------------")
    print("Welcome to the drone control center!")
    print("-----------------------")

    create_connection()
    
    while True:

        print("\n-----------------------")
        print("Pick an option:")
        print("--- 1. Arm the drone")
        print("--- 2. Disarm the drone")
        print("--- 3. Takeoff")
        print("--- 4. Land")
        print("--- 5. Show received messages")
        print("--- 6. Go to Specified Location")
        print("--- 7. Exit program")

        print("\n-----------------------")
        option = int(input ("Select an option: "))
        print("selected option: ", option)

        if option == 1:
            arm_drone()
        elif option == 2:
            disarm_drone()
        elif option == 3:
            takeoff()
        elif option == 4:
            land()
        elif option == 5:
            show_messages()
        elif option == 6:
            go_to_location()
        elif option == 7:
            break
        else:
            print("Option not implemented yet!")
    



if __name__ == "__main__":
    main()


