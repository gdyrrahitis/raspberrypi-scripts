#!/usr/bin/env python3

from .common import q, red, amber, green
from time import sleep


def steadyGreen():
    print("Steady green")
    if red.is_lit:
        red.off()

    if amber.is_lit:
        amber.off()

    green.on()


def steadyAmber(wait):
    print("Steady amber")
    if green.is_lit:
        green.off()

    amber.on()
    sleep(wait)


def steadyRed(wait):
    print("Steady red")
    if amber.is_lit:
        amber.off()

    red.on()
    sleep(wait)


def flashingAmber(wait):
    print("Flashing amber")
    red.off()
    total = 0
    while True:
        amber.on()
        sleep_time = 0.7
        total += sleep_time
        sleep(0.4)
        amber.off()
        sleep(0.3)

        if total >= wait:
            break


def carTraffic():
    sleep(20)
    steadyAmber(3)
    steadyRed(10)
    flashingAmber(7)
    steadyGreen()


def carSequence():
    print("Adding item to queue")
    if q.empty():
        print("Queue is empty, adding traffic sequence...")
        q.put(carTraffic)
        return

    if q.unfinished_tasks > 0 and q.unfinished_tasks == 1:
        print("Adding the next traffic sequence...")
        q.put(carTraffic)
        return
    else:
        print("Ignoring, already requested pedestrian traffic lights.")
