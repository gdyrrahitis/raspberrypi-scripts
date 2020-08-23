from time import sleep
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host='192.168.0.123')

button = Button(23, pin_factory=factory)

print("-----------")
print("Button and GPIO")
print("-----------")

while True:
    if button.is_pressed:
        print("Button is pressed")
        sleep(1)
    else:
        pass
        # os.system("cls")
        # print("Waiting you to press the button")
    sleep(0.5)
