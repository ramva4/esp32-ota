# Version $Id$

import machine
import time

version_attr = "$Id$"
print("main.py v$Id$")

print("Starting blink")

# Most ESP32 dev boards have the LED on GPIO2, some on GPIO5
led = machine.Pin(2, machine.Pin.OUT)

while True:
    led.value(1)  # Turn LED on (or led.on())
    time.sleep(0.5) # Wait 0.5 seconds
    led.value(0)  # Turn LED off (or led.off())
    time.sleep(0.5) # Wait 0.5 seconds

