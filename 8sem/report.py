import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
import numpy as np

with open('data.txt', 'r') as f:
    data = np.array(f.readlines())
    for i in range(len(data)):
        data[i] = data[i][:-1]
    print(data)

exp_duration = 6.80193567276001
l = len(data)
measurements_time = np.array([exp_duration*i/l for i in range(l)])

with open('settings.txt', 'r') as f:
    setting = f.readlines()

plt.figure()
plt.plot(measurements_time, data)
plt.xlabel('Время, с')
plt.ylabel('Напряжение на конденсаторе, V')
plt.minorticks_on()               
plt.grid(which='major')
plt.grid(which='minor',linestyle=':')  
plt.tight_layout()
plt.show()