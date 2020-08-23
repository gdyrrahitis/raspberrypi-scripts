from os import system
from time import sleep
from gpiozero import Buzzer
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory('192.168.0.123')
buzzer = Buzzer(22, pin_factory=factory)


def element(tfrom, tto):
    buzzer.on()
    sleep(tfrom)
    buzzer.off()
    sleep(tto)


def dot():
    element(0.1, 0.2)


def dash():
    element(0.3, 0.1)


def letterSpace():
    sleep(0.2)


def wordSpace():
    sleep(0.6)


def morseLetterS():
    for i in range(3):
        dot()


def morseLetterO():
    for i in range(3):
        dash()


def SOS():
    morseLetterS()
    letterSpace()
    morseLetterO()
    letterSpace()
    morseLetterS()
    wordSpace()


system("clear")
count = input("How many times you want to produce SOS morse code?")
count = int(count)

while count > 0:
    SOS()
    count -= 1
