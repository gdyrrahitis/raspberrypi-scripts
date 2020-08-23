import os
import math
from waveshare_epd import epd2in9
from PIL import Image, ImageDraw, ImageFont
from w1thermsensor import W1ThermSensor
from time import sleep

dirname = os.path.dirname(__file__)
bmp_file_path = os.path.join(dirname, 'Weather-Thermometer-icon.bmp')
sensor = W1ThermSensor()
font24 = ImageFont.truetype(
        '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)
CELSIUS_SYMBOL = u'\u00b0' + 'C'

try:
    epd = epd2in9.EPD()
    print('Initializing EPD device')
    epd.init(epd.lut_full_update)
    epd.Clear(0xFF)
    print('Cleared screen')
    previous_temp = -99999

    while True:
        temp = sensor.get_temperature(W1ThermSensor.DEGREES_C)

        if (math.floor(abs(temp - previous_temp)) != 0):
            print('Refreshing screen')
            previous_temp = temp
            HImage = Image.new('1', (epd.height, epd.width), 255)
            draw = ImageDraw.Draw(HImage)
            print('{} '.format(round(temp)) + CELSIUS_SYMBOL)

            draw.text((10, 0), 'Room temperature', font=font24, fill=0)
            text = '{} '.format(round(temp)) + CELSIUS_SYMBOL
            draw.text((65, 55), text, font=font24, fill=0)

            bmp = Image.open(bmp_file_path)
            HImage.paste(bmp, (10, 45))
            epd.display(epd.getbuffer(HImage))
        else:
            print('Temperature hasn\'t changed, no need to refresh screen')

        sleep(10)
except IOError as e:
    epd.Clear(0xFF)
    epd.sleep()
    print('Error: {}'.format(str(e)))
    exit()
except KeyboardInterrupt:
    epd.Clear(0xFF)
    epd.sleep()
    print('Exiting...')
    exit()
