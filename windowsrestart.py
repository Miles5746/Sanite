import subprocess
import time

PLACE_ID = "2753915549"
ROBLOX_URI = f"roblox://placeId={PLACE_ID}"

def is_roblox_running():
    result = subprocess.run(
        ["tasklist"],
        stdout=subprocess.PIPE,
        text=True
    )
    return "RobloxPlayerBeta.exe" in result.stdout

def join_blox_fruits():
    subprocess.run(["start", ROBLOX_URI], shell=True)

while True:
    if not is_roblox_running():
        join_blox_fruits()
    time.sleep(3)
