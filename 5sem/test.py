import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(bit) for bit in bin(int(value))[2:].zfill(8)]

# def adc(i, voltage_range):
#     ans = [0 for _ in range(i)]
#     time.sleep(0.5)
#     for value in range(i):
#         ans[value] = 1
#         GPIO.output(dac[value], ans[value])
#         comp_value = GPIO.input(comp)
#         if comp_value == 1:
#             ans[value] = 0
#         GPIO.output(dac[value], ans[value])
#     # GPIO.output(dac, signal)
#     # voltage = value/levels * voltage_range
#     return ans

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
i = len(dac)
levels = 2 ** i
voltage_range = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
#GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
#GPIO.output(troyka, initial)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        ans = 0
        for value in range(i):
            ans += 2**(7-value)
            GPIO.output(dac, dec2bin(ans))
            time.sleep(0.05)
            comp_value = GPIO.input(comp)
            ans -= comp_value*2**(7-value)
        GPIO.output(dac, ans)
        print(ans)
        print(ans/256*voltage_range)
finally:
    GPIO.output(dac, 0)
    #GPIO.output(leds, 0)
    GPIO.cleanup()