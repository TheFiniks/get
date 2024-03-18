import RPi.GPIO as GPIO
import time
def dec2bin(value):
    return [int(bit) for bit in bin(int(value))[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]
voltage_range = 3.3
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
# print(dec2bin('10'))
try:
    while True:
        num = input('Введите целое число от 0 до 255: ')
        #num = input()
        if num == 'q':
            break
        if not num.isdigit():
            print('Введите целое нетрицательное число')
            continue
        num = int(num)
        # if not(num == float(num) or num == int(num)):
        #     print('Введите число!')
        #     continue
        # if not num == int(num):
        #     print('Введите целое число!')
        #     continue
        # else:
        #     num = int(num)
        # if num < 0:
        #     print('Введите неотрицательное число')
        #     continue
        if num > 255:
            print('Введите число из заданного диапазона!')
            continue
        ans = dec2bin(num)
        GPIO.output(dac, ans)
        voltage = voltage_range / 2**len(dac) * num
        print("{:.4f}".format(voltage),'V')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
