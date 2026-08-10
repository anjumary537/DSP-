import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

fs = 500
t = np.linspace(0, 1, fs, endpoint = True)
signal_5hz = np.sin(2*np.pi*5*t)
noise = np.random.normal(0, 0.5, size=len(t))
combined_signal = signal_5hz + noise


sos = signal.butter(4, 10, fs=500, btype='low', output='sos')
filtered_signal = signal.sosfilt(sos, combined_signal)

plt.plot(t, combined_signal, label='Noisy Signal')
plt.plot(t, filtered_signal, label='Filtered Signal', linewidth=2)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Butterworth Low-Pass Filter')
plt.legend()
plt.show()

