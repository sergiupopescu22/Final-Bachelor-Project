import asyncio
from mavsdk import System

def run():
    # Connect to the flight controller
    drone = System()
    drone.connect(system_address="udpin:localhost:14540")

    # Set the flight mode to offboard
    drone.action.set_mode("OFFBOARD")

if __name__ == "__main__":
    run()