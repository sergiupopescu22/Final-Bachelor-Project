altitude = "not available yet"
relative_alt = "not available yet"
latitude = "not available yet"
longitude = "not available yet"
arm_state = "not available yet"
fligh_mode = "not available yet"

def get_info(the_connection):

    global altitude
    global latitude
    global longitude
    global arm_state
    global fligh_mode
    # while True:
    msg = the_connection.recv_match(type='GLOBAL_POSITION_INT', blocking=False)
    # msg = master.recv_match()
    # print(msg)
    # print(type(msg))
    # print(msg.x)
    # time.sleep(2)
    return msg

    altitude = 0
    print("Altitude: ", msg.alt, altitude)

# GLOBAL_POSITION_INT_COV
# LOCAL_POSITION_NED


