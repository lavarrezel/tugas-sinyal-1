# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 07:08:16 2023

@author: ACER
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ID
print("Nama : Alfa Naufal Afif Lintang Madani")
print("NRP : 5009211062")

# parameter sinyal
amplitude = 1
frequency = 1000
phase = 0

# sinyal sinus asli
t = np.linspace(0, 2*np.pi, 100)
sinyal_asli = amplitude * np.sin(frequency * t + phase)

# sinyal sinus yang terkena noise
noise = 0.5 * np.random.normal(0, 1, len(t))
sinyal_noise = sinyal_asli + noise

# sinyal yang difilter menggunakan Low Pass Filter 
cutoff_frequency = 50
order = 4
b, a = signal.butter(order, cutoff_frequency / (0.5 * frequency), btype='low')
sinyal_filter = signal.lfilter(b, a, sinyal_noise)

# plot sinyal asli
plt.figure(figsize=(12, 9))
plt.subplot(311)
plt.plot(t, sinyal_asli)
plt.title("Sinyal Asli")

# plot sinyal yang terkena noise
plt.subplot(312)
plt.plot(t, sinyal_noise)
plt.title("Sinyal Asli yang Terkena Noise")

# plot sinyal yang difilter
plt.subplot(313)
plt.plot(t, sinyal_filter)
plt.title("Sinyal yang Sudah di Filter")

plt.subplots_adjust(hspace=0.4)
plt.show()