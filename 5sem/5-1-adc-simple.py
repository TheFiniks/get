import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(bit) for bit in bin(int(value))[2:].zfill(8)]

def adc(levels, voltage_range):
    for value in range(levels):
        time.sleep(0.007)
        signal = dec2bin(value)
        GPIO.output(dac, signal)
        voltage = value/levels * voltage_range
        comp_value = GPIO.input(comp)
        if comp_value == 1:
            return value, signal, voltage
            break
        else:
            pass

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
i = len(dac)
levels = 2 ** i
voltage_range = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
#GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
#GPIO.output(troyka, initial)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        print(adc(levels, voltage_range))
finally:
    GPIO.output(dac, 0)
    #GPIO.output(leds, 0)
    GPIO.cleanup()