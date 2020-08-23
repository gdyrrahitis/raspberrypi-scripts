from gpiozero import PWMLED, MCP3008
from time import sleep
from operator import truediv

pot = MCP3008(0)
led = PWMLED(17)
g2 = PWMLED(27)
g3 = PWMLED(22)
g4 = PWMLED(5)

g5 = PWMLED(6)
g6 = PWMLED(26)
g7 = PWMLED(23)

g8 = PWMLED(24)
g9 = PWMLED(25)
g10 = PWMLED(16)

leds = [led, g2, g3, g4, g5, g6, g7, g8, g9, g10]


def light_up(index):
    global leds
    the_led = leds[index]
    substractor = truediv(index, 10)
    if the_led.value < 1.0:
        print('substractor: {}\npot: {}'.format(substractor, pot.value))
        v = pot.value - substractor
        if v < 0:
            v = 0
        elif v > 0.1:
            v = 0.1

        print('value {}\n\n'.format(v))
        the_led.value = v * 10

    start = index + 1

    if start < len(leds):
        for l in leds[start:]:
            l.value = 0


try:
    while True:
        if pot.value < 0.001:
            for l in leds:
                l.value = 0
        elif pot.value > 0.001 and pot.value <= 0.1:
            light_up(0)
        elif pot.value > 0.1 and pot.value <= 0.2:
            light_up(1)
        elif pot.value > 0.2 and pot.value <= 0.3:
            light_up(2)
        elif pot.value > 0.3 and pot.value <= 0.4:
            light_up(3)
        elif pot.value > 0.4 and pot.value <= 0.5:
            light_up(4)
        elif pot.value > 0.5 and pot.value <= 0.6:
            light_up(5)
        elif pot.value > 0.6 and pot.value <= 0.7:
            light_up(6)
        elif pot.value > 0.7 and pot.value <= 0.8:
            light_up(7)
        elif pot.value > 0.8 and pot.value <= 0.9:
            light_up(8)
        elif pot.value > 0.9 and pot.value <= 1.0:
            light_up(9)

        sleep(0.1)
except KeyboardInterrupt:
    print('Exiting...')
    exit()
