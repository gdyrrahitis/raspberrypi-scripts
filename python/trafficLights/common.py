#!/usr/bin/env python3

import queue
from os import environ
from gpiozero import LED, Buzzer, Button
from gpiozero.pins.pigpio import PiGPIOFactory


try:
    if 'USER' in environ:
        factory = None
    else:
        factory = PiGPIOFactory(host='192.168.0.123')
except KeyError:
    factory = PiGPIOFactory(host='192.168.0.123')

red = LED(14, pin_factory=factory)
amber = LED(15, pin_factory=factory)
green = LED(18, pin_factory=factory)
buzzer = Buzzer(7, pin_factory=factory)
btn = Button(23, pin_factory=factory)
q = queue.Queue()


def worker():
    while True:
        print("Retrieving from queue...")
        seq = q.get(block=True, timeout=None)
        print("Retrieved item from queue")
        seq()
        q.task_done()
