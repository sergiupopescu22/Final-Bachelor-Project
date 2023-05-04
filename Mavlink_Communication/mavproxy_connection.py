import subprocess
import Flight_Commands.global_variables as GVar
import time

def mavproxy_connection():

    if GVar.action_type == "real-life-win":
        setup_process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'mavproxy.py'])
        time.sleep(5)
        setup_process.kill()

    elif GVar.action_type == "real-life-rb":
        setup_process = subprocess.Popen(['mavproxy.py'])
        time.sleep(5)
        setup_process.terminate()

    else:
         pass