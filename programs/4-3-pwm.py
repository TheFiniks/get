import RPi.GPIO as GPIO
import time
def dec2bin(value):
    return [int(bit) for bit in bin(int(value))[2:].zfill(8)]
dac = [2, 3, 4, 17, 27, 22, 10, 9]
n = 7
voltage_range = 3.3
frequancy = 1000
duty_cycle = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac[n], GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
pwm_output1 = GPIO.PWM(dac[n], frequancy)
pwm_output1.start(duty_cycle)
pwm_output2 = GPIO.PWM(21, frequancy)
pwm_output2.start(duty_cycle)
try:
    while True:
        duty_cycle = float(input('Введите коэффициент заполнения: '))
        pwm_output1.ChangeDutyCycle(duty_cycle)
        pwm_output2.ChangeDutyCycle(duty_cycle)
        print(f'Предполагаемое напряжение: {voltage_range*duty_cycle/100} V')
finally:
    GPIO.output(dac[n], 0)
    GPIO.cleanup()