from pymavlink import mavutil

from Flight_Commands.MakeConnection import *
from Flight_Commands.Arm import *
from Flight_Commands.Disarm import *
from Flight_Commands.Taskeoff import *
from Flight_Commands.Land import *
from Flight_Commands.SetPosition import *
from Flight_Commands.WayPointMission import *
from Flight_Commands.ACK import *
from Flight_Commands.Return import *
from Flight_Commands.GetInfo import *

from fastapi import FastAPI
from fastapi import BackgroundTasks
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi_utils.tasks import repeat_every
from typing import Any

DRONE_ID = "03DF7Y2JK"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Replace "*" with your list of allowed HTTP methods
    allow_headers=["*"],  # Replace "*" with your list of allowed headers
)

def setup():
    global master

    print("\n-----------------------")
    print("Welcome to the drone control center!")
    print("-----------------------")

    master = create_connection()

class Data(BaseModel):
    type: int
    waypoints: Any

@app.post("/command/")
async def read_root(command: Data):

    global latitude
    global longitude

    option = command.type
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
        get_info(master)
    elif option == 6:
        # go_to_location()
        print("Option not working yet! :(")
    elif option == 7:
        if waypoint_verification(command.waypoints, latitude, longitude) is True:
            waypoint_mission(master, command.waypoints)
        else:
            print("Waypoints too far away from starting point!!!!!!")
            
    elif option == 8:
        set_return(master)
    else:
        print("Option not implemented yet!")

    # global altitude
    # altitude = 0

@app.get("/info_state/")
async def read_root():

    global altitude
    global relative_alt
    global latitude
    global longitude
    global arm_state
    global fligh_mode

    # info = get_info(master)

    # return {
    #     "altitude": info.alt/1000,
    #     "relative_altitude": info.relative_alt/1000,
    #     "latitude": latitude,
    #     "longitude": longitude,
    #     "arm_state": arm_state,
    #     "flight_mode": fligh_mode,
    # }

    return {
        "altitude": altitude,
        "relative_altitude": relative_alt,
        "latitude": latitude,
        "longitude": longitude,
        "arm_state": arm_state,
        "flight_mode": fligh_mode,
        "drone_id": DRONE_ID
    }

def get_info(the_connection):

    global altitude
    global relative_alt
    global latitude
    global longitude
    global arm_state
    global fligh_mode

    msg = the_connection.recv_match(type='GLOBAL_POSITION_INT', blocking=False)
    # arm_status = master.recv_match(type='HEARTBEAT', blocking=True)
    # if arm_status:
    #     if arm_status.basemode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED:
    #         arm_state = "ARMED"
    #     else:
    #         arm_state = "NOT ARMED"

    altitude = msg.alt//100/10
    relative_alt = msg.relative_alt//100/10
    latitude = msg.lat/10000000
    longitude = msg.lon/10000000

    # print(msg.relative_alt)

@app.on_event("startup")
@repeat_every(seconds=0.01)
async def startup_event():
    get_info(master)

if __name__ == "__main__":

    setup()

    uvicorn.run("Drone_Control_Server:app", host="0.0.0.0", port=8000, log_level="info")


