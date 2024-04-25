import subprocess
import time
import threading

# Executable paths
executable = 'path_to_executable1.exe'
start_port = ''
start_query_port = ''
mod_list = ''
game_id = ''
processes = []
tile_num = 2


def run_process(path):
    """ Run an executable and monitor it. """
    while True:
        print(f"Starting {path}")
        process = subprocess.Popen(path, shell=True)
        process.wait()
        print(f"{path} has exited. It will be checked for restart conditions.")
        time.sleep(1)


def check_for_updates():
    """ Use steamcmd to check for updates and determine if an update was applied. """
    # Command to check for updates via steamcmd
    cmd = 'steamcmd +login anonymous +app_update 12345 +quit'
    process = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    output = process.stdout
    print(output)
    if "Success" in output:  # Check the appropriate keyword based on your steamcmd output
        return True
    return False


def check_workshop_updates(workshop_ids):
    """ Check for updates on a list of workshop items. """
    updated = False
    for workshop_id in workshop_ids:
        cmd = f'steamcmd +login anonymous +workshop_download_item 12345 {workshop_id} +quit'
        process = subprocess.run(cmd, shell=True, text=True, capture_output=True)
        output = process.stdout
        print(output)
        if "Success" in output:  # Check the appropriate keyword based on your steamcmd output
            updated = True
    return updated


def manage_updates():
    """ Continuously check for updates and restart processes if necessary. """
    while True:
        game_updated = check_for_updates()
        workshop_updated = check_workshop_updates(mod_list)
        if game_updated or workshop_updated:
            print("Update found. Restarting all processes.")
            # Restart processes
            for process in processes:
                process.terminate()
                process.wait()
            start_processes(tile_num)
        time.sleep(1800)


def start_processes(num):
    global processes
    processes = [None] * num
    for i in range(num):
        process = threading.Thread(target=run_process, args=(executable,))
        process.start()
        processes[i] = process


# Start processes initially
start_processes(tile_num)

# Start update manager thread
# update_thread = threading.Thread(target=manage_updates)
# update_thread.start()
