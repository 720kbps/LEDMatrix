import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 256        # Number of LED pixels.
LED_PIN = 23          # GPIO pin (18 is PWM).
LED_FREQ_HZ = 800000  # LED signal frequency (usually 800kHz)
LED_DMA = 10          # DMA channel to use for generating signal
LED_BRIGHTNESS = 64   # Brightness (0-255)
LED_INVERT = False    # True to invert signal (NPN transistor level shift)
LED_CHANNEL = 0       # Set to '1' for GPIOs 13, 19, 41, 45, or 53

# Initialize strip
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT,
                   LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# Function to set all LEDs to one color
def color_wipe(color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

# Example usage
try:
    while True:
        color_wipe(Color(255, 0, 0))  # Red
        color_wipe(Color(0, 255, 0))  # Green
        color_wipe(Color(0, 0, 255))  # Blue
except KeyboardInterrupt:
    # Turn off LEDs on Ctrl+C
    color_wipe(Color(0, 0, 0))
