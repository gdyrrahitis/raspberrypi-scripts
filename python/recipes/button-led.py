from gpiozero import LED, Button
from signal import pause

led = LED(18)
btn = Button(23)

led.source = btn

pause()
