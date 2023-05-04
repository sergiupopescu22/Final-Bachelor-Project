import subprocess
import time
import aioping
import asyncio
import Flight_Commands.global_variables as GVar
import aiohttp
import urllib

if GVar.action_type == "real-life-rb":
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    led_pin = 17
    GPIO.setup(led_pin, GPIO.OUT)

async def check_internet_connection_async():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://www.google.com') as response:
                if response.status == 200:
                    return True
                else:
                    return False
    except Exception:
        return False

def check_internet_connection():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except:
        return False
    
def confirm_connection():

    counter = 0

    while counter < 3:
        if check_internet_connection():
            print("Internet connection is active.")
            if GVar.action_type == "real-life-rb":
                GPIO.output(led_pin, GPIO.HIGH)
            counter += 1
        else:
            print("No internet connection.")
            if GVar.action_type == "real-life-rb":
                GPIO.output(led_pin, GPIO.LOW)
            counter = 0
        time.sleep(1)
    
    print("CONNECTION OK")
    return True
