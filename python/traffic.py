#!/usr/bin/env python3

import threading
from signal import pause
# from trafficLights.cars import carSequence
from trafficLights.pedestrians import pedestrianSequence
from trafficLights.common import red, btn, worker


# steadyGreen()
# btn.when_pressed = carSequence
red.on()
btn.when_pressed = pedestrianSequence

th = threading.Thread(target=worker, daemon=True)
th.start()
pause()
