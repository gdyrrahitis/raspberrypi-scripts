import time
from gpiozero import LED

red = LED(18)
yellow = LED(23)
green = LED(24)

while True:
    red.on()
    yellow.on()
    green.on()
    time.sleep(1)
    red.off()
    yellow.off()
    green.off()
    time.sleep(1)
