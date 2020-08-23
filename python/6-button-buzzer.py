from gpiozero import Button, Buzzer
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause

factory = PiGPIOFactory('192.168.0.123')
button = Button(23, pin_factory=factory)
buzzer = Buzzer(7, pin_factory=factory)


def pushed():
    buzzer.on()


def released():
    buzzer.off()


button.when_pressed = pushed
button.when_released = released

pause()
