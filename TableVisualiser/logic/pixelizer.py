import time

from pi5neo import Pi5Neo
from PIL import Image

LED_COUNT = 256
TIMER = 10 #seconds
DEFAULT_BRIGHTNESS = 0.25  # 0.0 (off) to 1.0 (full)

def _create_strip() -> Pi5Neo:
    # Use explicit keyword args supported by recent Pi5Neo releases.
    return Pi5Neo('/dev/spidev0.0', num_leds=LED_COUNT, spi_speed_khz=800)


def _show(strip: Pi5Neo) -> None:
    strip.update_strip()

def _scale_rgb(r: int, g: int, b: int, brightness) -> tuple[int, int, int]:
    return (
        max(0, min(255, int(r * brightness))),
        max(0, min(255, int(g * brightness))),
        max(0, min(255, int(b * brightness))),
    )

def _clear(strip: Pi5Neo) -> None:
    # Clear all LEDs so old frame data is not left visible.
    strip.clear_strip()
    _show(strip)

def _import_image(path: str) -> Image.Image:
    img = Image.open(path).convert('RGB')
    return img

def coords_to_index(x: int, y: int, width: int) -> int:
    if y % 2 == 0:
        return y * width + x
    return y * width + (width - 1 - x)

def main() -> None:
    strip = _create_strip()
    _clear(strip)
    print('Cleared strip')

    img = _import_image('../images/pixil-frame-0.png')
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r, g, b = _scale_rgb(r, g, b, DEFAULT_BRIGHTNESS) # set brightness
            led_index = coords_to_index(x, y, width)
            strip.set_led_color(led_index, r, g, b)
        _show(strip)

    print('Displayed the image')
    time.sleep(TIMER)
    _clear(strip)
    print('Cleared strip')

if __name__ == '__main__':
    main()
