from gpiozero import LED
from signal import pause
from random import randint


def set_source():
    while True:
        yield randint(0, 1)


led = LED(18)
led.source_delay = 1
led.source = set_source()
# led.source = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

pause()
