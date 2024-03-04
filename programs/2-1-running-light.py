import RPi.GPIO as GPIO
import time
leds = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
for i in range(3):
    for led in leds:
        GPIO.output(led, 1)
        time.sleep(1)
        GPIO.output(led, 0)
GPIO.output(leds, 0)
GPIO.cleanup()