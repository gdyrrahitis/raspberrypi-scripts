from gpiozero import LED, Buzzer, MotionSensor, LightSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host='192.168.0.221')
red = LED(18, pin_factory=factory)
blue = LED(24, pin_factory=factory)
buzzer = Buzzer(22, pin_factory=factory)
pir = MotionSensor(17, pin_factory=factory)
ldr = LightSensor(27, pin_factory=factory)
stopped = False
triggered = False

pir.wait_for_no_motion()

try:
    def on_motion():
        print("On motion called")
        if ldr.value <= 0.0:
            global stopped
            global triggered
            triggered = True
            print("Motion detected, alarm triggered")
            while stopped is False:
                red.on()
                buzzer.on()
                sleep(0.2)
                red.off()
                blue.on()
                sleep(0.2)
                blue.off()
                buzzer.off()
                sleep(0.2)

            if stopped:
                red.off()
                blue.off()
                buzzer.off()
                stopped = False

    def on_idle():
        print("On idle called")
        global triggered
        if triggered:
            print("Stopping the alarm")
            global stopped
            stopped = True
            red.off()
            blue.off()
            buzzer.off()

    pir.when_no_motion = on_idle
    pir.when_motion = on_motion

    print("Alarm is set")
    input("Press any key to exit...")
except KeyboardInterrupt:
    print("Quiting...")
    red.off()
    blue.off()
    buzzer.off()
