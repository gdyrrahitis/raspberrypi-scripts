from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host='192.168.0.122')
red = LED(18, pin_factory=factory)

# 18
# 23
# 24

# led.on()
# sleep(1)
# led.off()
# sleep(1)

yellow = LED(23, pin_factory=factory)
green = LED(24, pin_factory=factory)
red.on()
sleep(2)
yellow.on()
sleep(2)
green.on()
sleep(2)
red.off()
sleep(2)
yellow.off()
sleep(2)
green.off()

array = [1, 2, 3, 2, 1]
for a in array:
    red.on()
    yellow.on()
    green.on()
    sleep(a)
    red.off()
    yellow.off()
    green.off()
    sleep(a)
