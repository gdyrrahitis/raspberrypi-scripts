from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep


factory = PiGPIOFactory(host='192.168.0.123')
led = LED(25, pin_factory=factory)

try:
    while True:
        led.on()
        print('LED is on...')
        sleep(1)
        led.off()
        print('LED is off...')
        sleep(1)
except KeyboardInterrupt:
    print('Turning LED off')
    led.off()
    print('Program is exiting...')
