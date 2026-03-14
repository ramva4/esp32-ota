# Version $Id$

# from machine import Pin, SoftI2C
import ssd1306
# from time import sleep
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

main.py file. It simply prints the ‘Hello, World!‘ message three times in the display.


# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello, World 1!', 0, 0)
oled.text('Hello, World 2!', 0, 10)
oled.text('Hello, World 3!', 0, 20)
        
oled.show()
