import time
from casanovamacro import *

# while True:
#     print("working from corr", config.cid, config.character, config.flash_hwnd)
#     time.sleep(1)

c = Corruption()
# run_thread(c.read_floor)
# run_thread(c.read_pointer)
# run_thread(c.die_detector)
c.init()

# while True:
#     # c.claim()
#     c.upstair()

print(check_image_existance(CLAIMED_STATE))