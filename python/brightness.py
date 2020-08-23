from gpiozero import PWMLED
from time import sleep

led = PWMLED(18)

try:
    total = 0
    step = 0.1
    while True:
        led.value = total
        sleep(1)
        total += step
        if total > 1:
            total = 0
except KeyboardInterrupt:
    led.value = 0
    print("Exiting...")
