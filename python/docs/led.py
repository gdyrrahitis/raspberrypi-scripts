from gpiozero import LED
from time import sleep

led = LED(14)
led.on()
sleep(3)
led.off()
