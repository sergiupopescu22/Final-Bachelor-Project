from pymavlink import mavutil

import Flight_Commands.global_variables as GVar
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
import subprocess
import time
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
    global action_type

    print("\n-----------------------")
    print("Welcome to the drone control center!")
    print("-----------------------")

    master = create_connection()


class Data(BaseModel):
    type: int
    waypoints: Any


@app.post("/command/")
async def read_root(command: Data):

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
        if waypoint_verification(command.waypoints, GVar.latitude, GVar.longitude) is True:
            waypoint_mission(master, command.waypoints)
        else:
            print("Waypoints too far away from starting point!!!!!!")
            
    elif option == 8:
        set_return(master)
    else:
        print("Option not implemented yet!")


@app.get("/info_state/")
async def read_root():

    return {
        "altitude": GVar.altitude,
        "relative_altitude": GVar.relative_alt,
        "latitude": GVar.latitude,
        "longitude": GVar.longitude,
        "arm_state": GVar.arm_state,
        "flight_mode": GVar.fligh_mode,
        "drone_id": DRONE_ID
    }


@app.on_event("startup")
@repeat_every(seconds=0.01)
async def startup_event():
    get_info(master)

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print("\nAs no input was provided, the server will run in simulation state\n")

    elif sys.argv[1] == "real-life":
        GVar.action_type = "real-life"
        setup_process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'mavproxy.py'])
        time.sleep(5)
        setup_process.kill()

    elif sys.argv[1] == "simulation":
        GVar.action_type = "simulation"

    else:
        print("\nThe provided input can not be processed!\n")

    setup()

    uvicorn.run("Drone_Control_Server:app", host="0.0.0.0", port=8000, log_level="info")


