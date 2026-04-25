import time

from pi5neo import Pi5Neo
from PIL import Image

LED_COUNT = 256
TIMER = 10 #seconds

def _create_strip() -> Pi5Neo:
    # Use explicit keyword args supported by recent Pi5Neo releases.
    return Pi5Neo('/dev/spidev0.0', num_leds=LED_COUNT, spi_speed_khz=800)


def _show(strip: Pi5Neo) -> None:
    strip.update_strip()


def _clear(strip: Pi5Neo) -> None:
    # Clear all LEDs so old frame data is not left visible.
    strip.clear_strip()
    _show(strip)

def _import_image(path: str) -> Image.Image:
    img = Image.open(path).convert('RGB')
    return img

def main() -> None:
    strip = _create_strip()
    _clear(strip)
    print('Cleared strip')

    img = _import_image('../images/pixil-frame-0.png')
    width, height = img.size()
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            strip.set_pixel_color(y * width + x, r, g, b)

    time.sleep(TIMER)
    _clear(strip)
    print('Cleared strip')

if __name__ == '__main__':
    main()
