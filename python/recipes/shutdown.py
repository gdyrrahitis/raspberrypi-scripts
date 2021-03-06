from gpiozero import Button
from subprocess import check_call
from signal import pause


def shutdown():
    check_call(['sudo', 'poweroff'])


btn = Button(23, hold_time=5)
btn.when_held = shutdown

pause()
