from travispy import TravisPy
from gpiozero import LED
from signal import pause


red = LED(14)
yellow = LED(15)
green = LED(18)

repository_name = 'gdyrrahitis/pi-commander-mobile'
travis = TravisPy()

try:
    def build_started():
        while True:
            r = travis.repo(repository_name)
            print(f'Started state {r.state}')
            yield r.state == 'started'

    def build_passed():
        while True:
            r = travis.repo(repository_name)
            print(f'Passed state {r.state}')
            yield r.state == 'passed' and r.state != 'started'

    def build_unsuccessful():
        while True:
            r = travis.repo(repository_name)
            print(f'Unsuccessful state {r.state}')
            yield r.state != 'passed' and r.state != 'started'

    green.source = build_passed()
    green.source_delay = 20

    red.source = build_unsuccessful()
    red.source_delay = 20

    yellow.source = build_started()
    yellow.source_delay = 20

    pause()
except KeyboardInterrupt:
    green.off()
    red.off()
    yellow.off()
    print("Exiting...")
