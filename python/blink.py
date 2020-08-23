from gpiozero import LED
from signal import pause

green = LED(18)

try:
    green.blink()
    pause()
except KeyboardInterrupt:
    print("Exiting...")
