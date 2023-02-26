from pymavlink import mavutil

def create_connection():
    print("\n-----------------------")
    print("Establishing Connection to Flight Controller...")

    # master = mavutil.mavlink_connection('/dev/serial/by-id/usb-NXP_SEMICONDUCTORS_PX4_FMUK66_v3.x_0-if00')
    global master
    master = mavutil.mavlink_connection('udpin:localhost:14540')

    print("Connection created! Waiting for confirmation heartbeat...")

    while(master.target_system == 0):
        print("-- Checking Heartbeat")
        master.wait_heartbeat()
        print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))

    # master.wait_heartbeat()
    # print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))
    print("Connection is OK!")

    return master