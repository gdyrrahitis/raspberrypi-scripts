from waveshare_epd import epd2in9
from PIL import Image, ImageDraw, ImageFont
from signal import pause

try:
    font24 = ImageFont.truetype(
        '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)
    epd = epd2in9.EPD()
    print('Initializing EPD device')
    epd.init(epd.lut_full_update)
    epd.Clear(0xFF)
    print('Cleared screen')

    HImage = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(HImage)
    draw.text((10, 0), 'Hello world', font=font24, fill=0)
    print('Displaying frame...')
    epd.display(epd.getbuffer(HImage))
    pause()
except IOError as e:
    print('IO Exception: {}', str(e))
    exit()
except KeyboardInterrupt:
    epd.Clear(0xFF)
    epd.sleep()
    print('Exiting...')
    exit()
