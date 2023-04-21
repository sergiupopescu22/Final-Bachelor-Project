import Flight_Commands.global_variables as GVar

def get_info(the_connection):

    if GVar.action_type == "simulation":

        msg = the_connection.recv_match(type='GLOBAL_POSITION_INT', blocking=False)
        # arm_status = master.recv_match(type='HEARTBEAT', blocking=True)
        # if arm_status:
        #     if arm_status.basemode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED:
        #         arm_state = "ARMED"
        #     else:
        #         arm_state = "NOT ARMED"

        if msg is not None:

            GVar.altitude = msg.alt//100/10
            GVar.relative_alt = msg.relative_alt//100/10
            GVar.latitude = msg.lat/10000000
            GVar.longitude = msg.lon/10000000

    elif GVar.action_type == "real-life":

        msg1 = the_connection.recv_match(type='ALTITUDE', blocking=False)

        if msg1 is not None:

            GVar.altitude = msg.monotonic//100/10
            GVar.relative_alt = msg.altitude_relative//100/10
            # latitude = msg.lat/10000000
            # longitude = msg.lon/10000000



