import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)


GPIO.output(17, GPIO.HIGH)

time.sleep(1)

GPIO.output(17, GPIO.LOW)

time.sleep(1)
GPIO.output(17, GPIO.HIGH)

time.sleep(1)

ngrok = subprocess.Popen("/home/sergiu/Desktop/Final-Bachelor-Project/Mavlink_Communication/ngrok_conn.sh", shell=True)

GPIO.output(17, GPIO.LOW)

GPIO.cleanup()