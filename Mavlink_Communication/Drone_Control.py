from pymavlink import mavutil
import time

from Flight_Commands.MakeConnection import *
from Flight_Commands.Arm import *
from Flight_Commands.Disarm import *
from Flight_Commands.Taskeoff import *
from Flight_Commands.Land import *
from Flight_Commands.SetPosition import *
from Flight_Commands.WayPointMission import *
from Flight_Commands.ACK import *


def show_messages():
    while True:
        # msg = master.recv_match(type='LOCAL_POSITION_NED', blocking=True)
        msg = master.recv_match()
        print(msg)

def main():

    print("\n-----------------------")
    print("Welcome to the drone control center!")
    print("-----------------------")

    master = create_connection()
    
    while True:

        print("\n-----------------------")
        print("Pick an option:")
        print("--- 1. Arm the drone")
        print("--- 2. Disarm the drone")
        print("--- 3. Takeoff")
        print("--- 4. Land")
        print("--- 5. Show received messages")
        print("--- 6. Go to Specified Location")
        print("--- 7. Create Mission")
        print("--- 8. Retrun")
        print("--- 9. Exit program")

        print("\n-----------------------")
        option = int(input ("Select an option: "))
        print("selected option: ", option)

        if option == 1:
            arm_drone(master)
        elif option == 2:
            disarm_drone(master)
        elif option == 3:
            takeoff(master)
        elif option == 4:
            land(master)
        elif option == 5:
            show_messages()
        elif option == 6:
            # go_to_location()
            print("Option not working yet! :(")
        elif option == 7:
            waypoint_mission(master)
        elif option == 8:
            set_return(master)
        elif option == 9:
            break
        else:
            print("Option not implemented yet!")
    
if __name__ == "__main__":
    main()


