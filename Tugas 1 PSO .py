# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 22:07:03 2023

@author: ACER
"""

import numpy as np
import matplotlib.pyplot as plt
import pywt

# ID
print("Nama : Alfa Naufal Afif Lintang Madani")
print("NRP : 5009211062")

# parameter sinyal
amplitude = 1
frequency = 7
phase = 0

# sinyal sinus asli
t = np.linspace(0, 2*np.pi, 100)
signal = amplitude * np.sin(frequency * t + phase)

# sinyal sinus yang terkena noise
noise = np.random.normal(0, 0.5, len(signal))
noisy_signal = signal + noise

# sinyal yang difilter menggunakan wavelet filter
wavelet = 'db4'
coeffs = pywt.wavedec(noisy_signal, wavelet)
level = 5
threshold = 0.5
filtered_coeffs = [pywt.threshold(coeff, threshold) if i > 0 else coeff for i, coeff in enumerate(coeffs)]
filtered_signal = pywt.waverec(filtered_coeffs, wavelet)

# plot sinyal asli
plt.figure(figsize=(10, 6))
plt.subplot(311)
plt.plot(t, signal)
plt.title("Sinyal Asli")
plt.ylabel("Amplitudo")

# plot sinyal yang terkena noise
plt.subplot(312)
plt.plot(t, noisy_signal)
plt.title("Sinyal Asli yang Terkena Noise")
plt.ylabel("Amplitudo")

# plot sinyal yang difilter
plt.subplot(313)
plt.plot(t, filtered_signal)
plt.title("Sinyal yang Sudah di Filter")
plt.xlabel("Waktu (s)")
plt.ylabel("Amplitudo")

plt.subplots_adjust(hspace=0.6)
plt.show()