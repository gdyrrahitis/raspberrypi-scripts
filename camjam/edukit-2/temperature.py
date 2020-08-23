# from gpiozero import LED, Buzzer
from w1thermsensor import W1ThermSensor
from time import sleep


# red = LED(18)
# blue = LED(24)
# buzzer = Buzzer(22)
sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature(W1ThermSensor.DEGREES_C)
    print("{} Celsius".format(temperature))

    # if temperature <= 10.0:
    #     if red.is_lit:
    #         red.off()

    #     if buzzer.is_active:
    #         buzzer.off()

    #     if not blue.is_lit:
    #         blue.on()

    # if temperature > 10.0 and temperature < 50.0:
    #     if blue.is_lit:
    #         blue.off()

    #     if red.is_lit:
    #         red.off()

    #     if buzzer.is_active:
    #         buzzer.off()

    # if temperature >= 50.0:
    #     if not red.is_lit:
    #         red.on()

    #     if temperature < 70.0:
    #         if buzzer.is_active:
    #             buzzer.off()

    # if temperature >= 70.0:
    #     if not buzzer.is_active:
    #         buzzer.on()
    sleep(1)
