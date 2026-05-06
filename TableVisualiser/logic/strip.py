from pi5neo import Pi5Neo

LED_COUNT = 256
_strip = None


def get_strip():
    global _strip
    global LED_COUNT
    if _strip is None:
        _strip = _create_strip(LED_COUNT)
    return _strip

def _create_strip(led_count) -> Pi5Neo:
    # Use explicit keyword args supported by recent Pi5Neo releases.
    return Pi5Neo('/dev/spidev0.0', num_leds=led_count, spi_speed_khz=800)
