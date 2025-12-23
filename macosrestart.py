import subprocess
import time

PLACE_ID = "2753915549"
ROBLOX_URI = f"roblox://placeId={PLACE_ID}"

CHECK_INTERVAL = 3  # seconds between checks

def is_roblox_running():
    result = subprocess.run(
        ["pgrep", "-x", "RobloxPlayer"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

def join_blox_fruits():
    subprocess.run(["open", ROBLOX_URI])

def on_roblox_started():
    print("Watcher is Ready! If roblox crashes, will go back to the game!")

print("Roblox watchdog started...")

was_running = False

while True:
    running = is_roblox_running()

    # Roblox just crashed or was closed
    if not running and was_running:
        print("Roblox crashed. Rejoining Blox Fruits...")
        join_blox_fruits()

    # Roblox not running at all
    elif not running:
        print("Roblox not running. Joining Blox Fruits...")
        join_blox_fruits()

    # Roblox just started
    elif running and not was_running:
        on_roblox_started()

    was_running = running
    time.sleep(CHECK_INTERVAL)
