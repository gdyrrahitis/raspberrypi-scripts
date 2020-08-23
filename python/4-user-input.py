import os
import time
from gpiozero import LED

red = LED(18)
yellow = LED(23)
green = LED(24)

while True:
    os.system("clear")
    print("Choose from the following:\n")
    print("1: Red\n2: Yellow\n3: Green\n4: To exit\n")

    try:
        choice = int(input())

        if choice == 4:
            print("Exiting...")
            break

        count = int(input("How many times do you want the LED to flash?\n"))

        blinkFn = lambda light: red if light == 1 else yellow if light == 2 else green if light == 3 else None
        ledChoice = blinkFn(choice)

        if ledChoice is not None:
            print("Flashing...")
            while count > 0:
                print("{} is high".format(ledChoice))
                ledChoice.on()
                time.sleep(1)
                ledChoice.off()
                print("{} is low".format(ledChoice))
                time.sleep(2)
                count -= 1
    except:
        print("A valid choice and count should be provided.")
