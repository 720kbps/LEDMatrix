# LED Matrix Project

Project is running on the Raspberry Pi 5 and uses a NeoPixel LED matrix to display various patterns and animations.

## Libraries Used
- NeoPixel Library: Used to control the NeoPixel LED matrix.

Used data pin is GPIO pin 18

## Installation
1. When just imaging the Rpi make sure to go throuhgh the setup process and connect to Wi-Fi.
2. Update the system and install necessary libraries
3. If ssh is still not working with user@hostname.local try enabling ssh on the Pi
4. Clone the repository and navigate to the project directory
5. Run the main script to start the LED matrix animations

The default spidev kernel buffer is 4096 bytes, which supports up to ~170 LEDs. For larger strips, increase the buffer by appending to the single line in /boot/firmware/cmdline.txt and rebooting:
```bash
spidev.bufsiz=32768
```
For RGBW strips the per-LED byte cost is higher (32 bytes vs. 24), so adjust accordingly.


**kylobit@raspberrypi**
1337