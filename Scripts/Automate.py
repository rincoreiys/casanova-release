
from time import sleep
try:
    from casanovamacro.Macro.Automate import Automate
    auto = Automate()
    auto.init()
except Exception as e:
    print(e)
finally:
    while True: sleep(1)