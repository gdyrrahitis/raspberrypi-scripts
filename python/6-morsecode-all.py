from time import sleep
from gpiozero import Buzzer
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory('192.168.0.122')
buzzer = Buzzer(7, pin_factory=factory)


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


def word(fun):
    fun()
    letterSpace()


alphabet = {
    "s": lambda: word(morseLetterS),
    "o": lambda: word(morseLetterO),
    " ": lambda: wordSpace()
}

# system("clear")
# userInput = input("Provide an input to be converted to morse code")
sos = "sos    sos"
sos = sos.lower()
sos = " ".join(sos.split())
print(sos)

for c in sos:
    fun = alphabet.get(c)
    fun()
