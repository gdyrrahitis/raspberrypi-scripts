from gpiozero import LightSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep


factory = PiGPIOFactory(host='192.168.0.221')
ldr = LightSensor(27, pin_factory=factory)

while True:
    print(ldr.value)
    sleep(1)
