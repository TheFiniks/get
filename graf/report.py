import time
import matplotlib.pyplot as plt
import numpy as np

with open('settings (1).txt', 'r') as f:
    setting = f.readlines()

with open('data (1).txt', 'r') as f:
    data = np.array(['0\n'])
    data = np.append(data, f.readlines())
    l = len(data)
    add = []
    for i in range(l):
        data[i] = (data[i][:-1])
    for i in range(l):
        add.append(int(data[i]))
    data = np.array(add)
    data = data * float(setting[1])

exp_duration = 9.86
measurements_time = np.linspace(0, exp_duration, l)

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(measurements_time, data, '.-', color='blue', label='V(t)', linewidth=1, markersize=6)

plt.xlabel('Время, с')
plt.ylabel('Напряжение, B')
plt.title('Процесс заряда и разряда конденсатора в RC-цепочке')

plt.minorticks_on()
plt.xticks(np.arange(min(measurements_time), max(measurements_time), 2))
plt.yticks(np.arange(min(data), max(data), 0.5))
plt.grid(which='major', color='grey')
plt.grid(which='minor', linestyle=':', color='grey')
plt.tight_layout()

ind_time_max = 366
t1 = float('{:.2f}'.format(ind_time_max / l * exp_duration))
t2 = float('{:.2f}'.format(exp_duration-t1))

plt.text(2, 1.9, f'Время зарядки = {t1} c', color='black')
plt.text(6, 1.5, f'Время разрядки = {t2} c', color='black')
plt.xlim([0, 10])
plt.ylim([0, 2.8])

plt.legend()
plt.savefig('report.svg')
plt.show()
