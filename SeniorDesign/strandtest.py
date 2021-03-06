#!/usr/bin/python2.7
#env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 144      # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
	
# Define functions which animate LEDs in various ways.
def colorWipeArray(strip, color,start,length):
    """Wipe color across display a pixel at a time."""
    i = start
    while(i<=(start+length)):
        strip.setPixelColor(i, color)
        strip.show()
        i += 1
        #time.sleep(wait_ms/1000.0)

# Main program logic follows:
def setColors(RGBWvalues,start,length,stripPin):
	#starting values for usage
	# LED strip configuration:
	LED_COUNT      = 144      # Number of LED pixels.
	LED_PIN        = stripPin      # GPIO pin connected to the pixels (18 uses PWM!).
	#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
	LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
	LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
	LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
	LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
	LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53, '0' for 16 & 18
	
	# Process arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
	args = parser.parse_args()

	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	
	#print ('Press Ctrl-C to quit.')
	#if not args.clear:
		#print('Use "-c" argument to clear LEDs on exit')
	
	try:
            ret = 0
            while True:
                #	colorWipe(strip, Color(255, 0, 0))  # Green wipe
                #	colorWipe(strip, Color(0, 255, 0))  # Red wipe
                #	colorWipe(strip, Color(0, 0, RGBWvalues))  # Blue wipe
                colorWipeArray(strip, Color(RGBWvalues[1], RGBWvalues[0], RGBWvalues[2]),start,length)  # Red wipe
                ret += 1
                if(ret == 5):
                    break
	except KeyboardInterrupt:
            if args.clear:
                colorWipe(strip, Color(0,0,0), 10)


def setColors2(color,column,length,stripPin):
    colorSet = Color(color[1],color[0],color[2])
    LED_COUNT      = 144      # Number of LED pixels.
    LED_PIN        = stripPin      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53, '0' for 16 & 18
	
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	# Intialize the library (must be called once before other functions).
    strip.begin()
	
	#print ('Press Ctrl-C to quit.')
	#if not args.clear:
		#print('Use "-c" argument to clear LEDs on exit')
    #Need to know the location so that we can adequately find the right leds to light up
    try:
        ret = 0
        while True:
                #	colorWipe(strip, Color(255, 0, 0))  # Green wipe
                #	colorWipe(strip, Color(0, 255, 0))  # Red wipe
                #	colorWipe(strip, Color(0, 0, RGBWvalues))  # Blue wipe
           colorWipeArray(strip,colorSet,40-20*(column),length)  # Red wipe
           colorWipeArray(strip,colorSet,82+(40-20*(column)),length)
           ret += 1
           if(ret == 5):
               break
    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)