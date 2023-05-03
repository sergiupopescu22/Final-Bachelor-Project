import subprocess
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

def check_internet_connection():
    try:
        output = subprocess.check_output(['ping', '-c', '3', 'google.com'])
        return True
    except subprocess.CalledProcessError:
        return False
    
def confirm_connection():

    counter = 0

    while counter < 3:
        if check_internet_connection():
            print("Internet connection is active.")
            GPIO.output(led_pin, GPIO.HIGH)
            counter += 1
        else:
            print("No internet connection.")
            GPIO.output(led_pin, GPIO.LOW)
            counter = 0
        time.sleep(1)
    
    print("CONNECTION OK")
    return True
