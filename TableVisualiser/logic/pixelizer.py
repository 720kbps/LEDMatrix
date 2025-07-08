import board
import neopixel
import time

NUM_PIXELS = 256  # adjust to your matrix size
PIXEL_PIN = board.D23  # GPIO pin 23
pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, auto_write=False)

# Example: rainbow cycle
def wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

while True:
    for j in range(255):
        for i in range(NUM_PIXELS):
            pixels[i] = wheel((i + j) & 255)
        pixels.show()
        time.sleep(0.01)
