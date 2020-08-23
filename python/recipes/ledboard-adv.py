from gpiozero import LEDBoard
from time import sleep

leds = LEDBoard(14, 15, 18)

for led in leds:
    led.on()
    sleep(1)
    led.off()
