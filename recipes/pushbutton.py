from gpiozero import LED, Button
from gpiozero.pins.pigpio import PiGPIOFactory


factory = PiGPIOFactory(host='192.168.0.123')
led = LED(25, pin_factory=factory)
button = Button(2, pin_factory=factory)


def button_pressed():
    led.on()


def button_released():
    led.off()


button.when_pressed = button_pressed
button.when_released = button_released

input('Press any button...')
