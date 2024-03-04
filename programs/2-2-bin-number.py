import RPi.GPIO as GPIO
import time
from random import randint
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
# number = [randint(0, 1) for _ in range(len(dac))]
number = 255
number_2 = [int(x) for x in bin(number)[2:]]
for _ in range(len(dac)-len(bin(number)[2:])):
    number_2.insert(0, 0)

print(number_2)
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number_2)
time.sleep(1)
GPIO.output(dac, 0)
GPIO.cleanup()
