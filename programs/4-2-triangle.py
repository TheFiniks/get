import RPi.GPIO as GPIO
import time
def dec2bin(value):
    return [int(bit) for bit in bin(int(value))[2:].zfill(8)]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
voltage_range = 3.3
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
try:
    period = float(input('Введите период в секундах: '))
    c = 0
    flag = '+'
    while True:
        GPIO.output(dac, dec2bin(c))
        time.sleep(period / 2**len(dac)/2)
        if c < 256 and flag == '+':
            c += 1
        if c == 256:
            flag = '-'
        if c != 0 and flag == '-':
            c -= 1
        elif c == 0:
            flag = '+'
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

