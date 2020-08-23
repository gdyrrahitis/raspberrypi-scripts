from gpiozero import MotionSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host='192.168.0.221')
pir = MotionSensor(17, pin_factory=factory)

try:
    print("Waiting for PIR to settle")
    # pir.wait_for_no_motion()

    print("PIR module test (CTLR+C to exit)")

    state = False
    movement = False
    while True:
        state = pir.motion_detected

        if state is True and movement is False:
            print("Motion detected!")
            movement = True
        elif state is False and movement is True:
            print("No motion")
            movement = False

        sleep(0.01)
except KeyboardInterrupt:
    print("Quiting...")
