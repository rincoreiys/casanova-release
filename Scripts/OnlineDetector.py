

from casanovamacro import *
while True:
    if wait_for_image(image_location= ["state/online", (205,15,45,41)], step=1, timeout=60):
        print("true")
        requests.post(f"http://127.0.0.1:3000/character/{config.cid}/online")
    else:
        print("false")
        requests.post(f"http://127.0.0.1:3000/character/{config.cid}/offline")
    time.sleep(1)



