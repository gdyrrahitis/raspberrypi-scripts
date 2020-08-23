from nameko.rpc import rpc
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep


class GreetingService:
    name = "greeting_service"

    def __init__(self):
        factory = PiGPIOFactory(host='192.168.0.123')
        self.red = LED(18, pin_factory=factory)
        self.yellow = LED(23, pin_factory=factory)
        self.green = LED(24, pin_factory=factory)

    @rpc
    def hello(self, name):
        return "Hello {}!!!".format(name)

    @rpc
    def blink(self, id):
        if id == 1:
            self.red.on()
            sleep(3)
            self.red.off()
            sleep(1)

        if id == 2:
            self.yellow.on()
            sleep(3)
            self.yellow.off()
            sleep(1)

        if id == 3:
            self.green.on()
            sleep(3)
            self.green.off()
            sleep(1)

        if id == 4:
            self.red.on()
            self.yellow.on()
            sleep(3)
            self.red.off()
            self.yellow.off()
            sleep(1)
