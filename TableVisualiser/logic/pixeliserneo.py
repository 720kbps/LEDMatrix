#!/usr/bin/env python3
"""Minimal Pi5Neo LED test: light one pixel, then turn it off."""

import time

from pi5neo import Pi5Neo

LED_COUNT = 256
TEST_PIXEL = 0
ON_COLOR = (0, 255, 0)  # Green
PAUSE_SECONDS = 3


def _create_strip() -> Pi5Neo:
    """Try common Pi5Neo constructor signatures."""
    try:
        return Pi5Neo('/dev/spidev0.0', LED_COUNT, 800)
    except TypeError:
        try:
            return Pi5Neo(LED_COUNT, '/dev/spidev0.0')
        except TypeError:
            return Pi5Neo(LED_COUNT)


def _set_pixel(strip: Pi5Neo, index: int, rgb: tuple[int, int, int]) -> None:
    r, g, b = rgb

    if hasattr(strip, 'set_led_color'):
        strip.set_led_color(index, r, g, b)
        return
    if hasattr(strip, 'set_led'):
        strip.set_led(index, r, g, b)
        return
    if hasattr(strip, 'set_pixel'):
        strip.set_pixel(index, rgb)
        return

    # Fallback for list-like implementations.
    strip[index] = rgb


def _show(strip: Pi5Neo) -> None:
    if hasattr(strip, 'update_strip'):
        strip.update_strip()
    elif hasattr(strip, 'show'):
        strip.show()
    elif hasattr(strip, 'write'):
        strip.write()


def main() -> None:
    strip = _create_strip()

    _set_pixel(strip, TEST_PIXEL, ON_COLOR)
    _show(strip)

    print(f'Pixel {TEST_PIXEL} ON: {ON_COLOR}')
    time.sleep(PAUSE_SECONDS)

    _set_pixel(strip, TEST_PIXEL, (0, 0, 0))
    _show(strip)
    print(f'Pixel {TEST_PIXEL} OFF')


if __name__ == '__main__':
    main()

