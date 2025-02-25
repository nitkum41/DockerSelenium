import threading
import subprocess

import os
import time

def run_script(script_name):
    subprocess.run(["python", script_name],shell=True)

if __name__ == "__main__":

    os.startfile("start_docker.bat")

    time.sleep(40)


    script1_thread = threading.Thread(target=run_script, args=("docker_chrome.py",))
    script2_thread = threading.Thread(target=run_script, args=("docker_firefox.py",))

    script1_thread.start()
    script2_thread.start()

    script1_thread.join()
    script2_thread.join()


    os.startfile("stop_docker.bat")
    time.sleep(40)

    print("Both scripts have finished executing.")