from gpiozero import Buzzer, LED, MotionSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

try:
    factory = PiGPIOFactory(host='192.168.0.221')
    pir = MotionSensor(17, pin_factory=factory)
    red = LED(18, pin_factory=factory)
    blue = LED(24, pin_factory=factory)
    buzzer = Buzzer(22, pin_factory=factory)

    print("Waiting for PIR to settle")
    pir.wait_for_no_motion()
    print("PIR Module Test (Any key to exit)")

    def motion():
        print("Motion detected")
        for x in range(0, 3):
            buzzer.on()
            red.on()
            sleep(0.2)
            red.off()
            blue.on()
            sleep(0.2)
            blue.off()
            buzzer.off()
            sleep(0.2)

    def no_motion():
        print("No motion")

    pir.when_motion = motion
    pir.when_no_motion = no_motion
except KeyboardInterrupt:
    print("Quiting...")

input("Press any key to exit...")
