from pi5neo import Pi5Neo
from PIL import Image

DEFAULT_BRIGHTNESS = 0.25  # 0.0 (off) to 1.0 (full)

def _show(strip: Pi5Neo) -> None:
    strip.update_strip()

def _scale_rgb(r: int, g: int, b: int, brightness) -> tuple[int, int, int]:
    return (
        max(0, min(255, int(r * brightness))),
        max(0, min(255, int(g * brightness))),
        max(0, min(255, int(b * brightness))),
    )

def clear(strip: Pi5Neo) -> None:
    # Clear all LEDs so old frame data is not left visible.
    strip.clear_strip()
    _show(strip)
    print('Cleared strip')

def import_image(path: str) -> Image.Image:
    img = Image.open(path).convert('RGB')
    return img

def coords_to_index(x: int, y: int, width: int) -> int:
    if y % 2 == 0:
        return y * width + x
    return y * width + (width - 1 - x)

def update_image(imgPath, strip) -> None:
    clear(strip)
    print('Cleared strip')

    img = import_image(imgPath)
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r, g, b = _scale_rgb(r, g, b, DEFAULT_BRIGHTNESS) # set brightness
            led_index = coords_to_index(x, y, width)
            strip.set_led_color(led_index, r, g, b)
        _show(strip)

    print('Displayed the image')
