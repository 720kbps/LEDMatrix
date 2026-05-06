# LED Matrix Project

Project is running on the Raspberry Pi 5 and uses a NeoPixel LED matrix to display various patterns and animations.

## Libraries Used
- NeoPixel Library: Used to control the NeoPixel LED matrix.

Used data pin is GPIO pin 18

## Installation
1. When just imaging the Rpi make sure to go through the setup process and connect to Wi-Fi.
2. Update the system and install necessary libraries
3. If ssh is still not working with user@hostname.local try enabling ssh on the Pi
4. Clone the repository and navigate to the project directory
5. Run the main script to start the LED matrix animations

The default spidev kernel buffer is 4096 bytes, which supports up to ~170 LEDs. For larger strips, increase the buffer by appending to the single line in /boot/firmware/cmdline.txt and rebooting:
```bash
spidev.bufsiz=32768
```
For RGBW strips the per-LED byte cost is higher (32 bytes vs. 24), so adjust accordingly.

## Quick Start
1. SSH into the RPi or let it run headless
2. Get the Rpi IP address using `hostname -I`
3. Activate the virtual environment and navigate to the project directory
3. Run `python manage.py runserver 0.0.0.0:8000` to start the web server
4. Access the web interface by navigating to `http://<RPI_IP_ADDRESS>:8000` in your web browser

**kylobit@raspberrypi**
1337