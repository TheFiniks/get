import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

def dec2bin(value):
    return [int(bit) for bit in bin(int(value))[2:].zfill(8)]

def adc(i, voltage_range, sampling):
    ans = 0
    for value in range(i):
        ans += 2**(7-value)
        GPIO.output(dac, dec2bin(ans))
        time.sleep(0.007)
        comp_value = GPIO.input(comp)
        ans -= comp_value*2**(7-value)
    return ans, int(ans/sampling*10)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
i = len(dac)
levels = 2 ** i
voltage_range = 3.3
sampling = 256

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    measurements = []
    measurements_time = []

    start_time = time.time() #Начало эксперимента
    capacitor_voltage = 0

    #Начало зарядки конденсатора
    GPIO.output(troyka, GPIO.HIGH)
    while capacitor_voltage <= 0.97*2.66:
        ans, volume = adc(i, voltage_range, sampling)
        capacitor_voltage = ans * voltage_range / sampling
        measurements.append(capacitor_voltage)
        measurements_time.append(time.time())

    #Начало разрядки конденсатора
    while capacitor_voltage >= 0.02*2.66:
        ans, volume = adc(i, voltage_range, sampling)
        capacitor_voltage = ans * sampling / voltage_range
        measurements.append(capacitor_voltage)
        measurements_time.append(time.time())

    end_time = time.time() #Конец измерений
    exp_duration = end_time - start_time

    #Построение графика
    plt.figure()
    plt.plot(measurements_time, measurements)
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение на конденсаторе, V')
    plt.minorticks_on()               
    plt.grid(which='major')
    plt.grid(which='minor',linestyle=':')  
    plt.tight_layout()
    plt.show()

    #Запись данных эксперимента
    with open('data.txt', 'w') as f:
        for measurement in measurements:
            f.write(f'{measurement}')
            f.write('\n')

    with open('settings.txt', 'w') as f:
        average_sampling_rate = len(measurements) / exp_duration
        quantization_step = voltage_range / sampling
        print(f'Длительность эксперимента: {exp_duration}')
        print(f'Период одного измерения: {1/average_sampling_rate}')
        f.write(f'Average Sampling Rate: {average_sampling_rate} Hz/n'+'\n')
        print(f'Средняя частота дискретизации проведенных измерений: {average_sampling_rate}')
        f.write(f'Quantization Step: {quantization_step} V')
        print(f'Шаг квантоания АЦП: {quantization_step}') 

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()