from gpiozero import LED, Buzzer
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep


factory = PiGPIOFactory(host='192.168.0.221')
red = LED(18)
blue = LED(24)
buzzer = Buzzer(22)

red.on()
blue.on()
buzzer.on()

sleep(1)
buzzer.off()
sleep(5)

red.off()
blue.off()
