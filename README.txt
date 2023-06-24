Hello there! This repo consists of the source code used to control a drone through an internet connnection.
Here are 2 main elements:
-> the web server + web app implemented with FastAPI
-> the user interface implemented with ReactJS


This project is meant to be used with a real drone, but because we are aware that this is very unlikely to 
happen, especially at the beginning, the source code can be tested using the Gazebo simulator, to simulate
the actual drone.

So, if you will use a simulated env, in order to have a running environment you need to follow these steps:

1. Go to https://docs.px4.io/v1.12/en/dev_setup/dev_env_linux_ubuntu.html#gazebo-jmavsim-and-nuttx-pixhawk-targets
 and get the Gazebo env and run it for the deisred drone with the following command: make px4_sitl gz_x500
2. Run the command: pip install -r to install the required packages for the web service
3. Run the command: npm install to install the required packaged for the web interface
4. Run the commnad: python Drone_Control_Server.py -simulation to start the web service on the ,,drone,,
5. Run the command: npm start to start the web interface
6. Have fun :)


If you will have a drone with a Raspberry Pi computer attached to it, you need to follow these steps:

1. Get the source code on the Raspberry Pi (just the web service code is relevant)
2. Run the command: pip install -r to install the required packages for the web service
3. Add in the startup file of the operation system the following command: python Drone_Control_Server.py -simulation
4. Run the command: npm install to install the required packaged for the web interface on the remote computer
5. Run the command: npm start to start the web interface
6. Start the drone and have fun :)

