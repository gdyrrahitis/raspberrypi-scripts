from gpiozero import LEDBoard
from signal import pause


try:
    leds = LEDBoard(14, 15, 18, pwm=True)
    leds.value = (0.2, 0.4, 0.8)

    pause()
except KeyboardInterrupt:
    leds.off()
    print("Exiting...")
