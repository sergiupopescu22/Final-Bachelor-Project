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

    elif GVar.action_type == "real-life-rb" or GVar.action_type == "real-life-win":

        msg2 = the_connection.recv_match(type='GPS_RAW_INT', blocking=False)

        if msg2 is not None:

            GVar.latitude = msg2.lat/10000000
            GVar.longitude = msg2.lon/10000000
            # # print(GVar.altitude)
            # GVar.relative_alt = msg1.altitude_relative
            # print(GVar.relative_alt)
            # latitude = msg.lat/10000000
            # longitude = msg.lon/10000000


        msg1 = the_connection.recv_match(type='ALTITUDE', blocking=False)

        if msg1 is not None:
            # print(msg1)

            GVar.altitude = msg1.altitude_monotonic
            # print(GVar.altitude)
            GVar.relative_alt = msg1.altitude_relative
            # print(GVar.relative_alt)
            # latitude = msg.lat/10000000
            # longitude = msg.lon/10000000

        




