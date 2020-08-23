#!/usr/bin/env python3

import time
import random
from .common import buzzer, red, green, amber


def pedestrianTraffic():
    red.on()
    time.sleep(4)
    red.off()
    green.on()
    seconds_to_beep = random.randint(4, 7)
    total = 0
    while True:
        buzzer.on()
        time.sleep(0.2)
        buzzer.off()
        time.sleep(0.15)
        total += 0.35

        if total >= seconds_to_beep:
            break

    total = 0
    while True:
        red.off()
        green.on()
        buzzer.on()
        time.sleep(0.5)
        green.off()
        buzzer.off()
        time.sleep(0.5)
        total += 1

        if total >= 4:
            break

    amber.on()
    time.sleep(6)
    amber.off()
    red.on()


def action1():
    buzzer.on()
    time.sleep(0.5)
    buzzer.off()


def action2():
    green.on()
    time.sleep(0.7)
    green.off()


def pedestrianSequence():
    time.sleep(20)
    pedestrianTraffic()
