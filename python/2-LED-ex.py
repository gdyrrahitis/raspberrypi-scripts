from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory


factory = PiGPIOFactory(host='192.168.0.123')
red = LED(14, pin_factory=factory)
amber = LED(15, pin_factory=factory)
green = LED(18, pin_factory=factory)

red.off()
amber.off()
green.off()

# def myfunc():
#     x = "blah"
#     print(x)


# myfunc()

# red = LED(14)
# yellow = LED(15)
# green = LED(18)

# print("LEDs on")
# red.on()
# yellow.on()
# green.on()

# print("Wait for 5 seconds")
# time.sleep(5)

# print("LEDs off")
# red.off()
# yellow.off()
# green.off()
