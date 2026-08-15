import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

np.random.seed(0)
n = 200
t = np.arange(n)
x = np.sin(2*np.pi*0.05*t)
h = np.array([1.0, 0, 0.5, 0, 0.2])
y = np.convolve(x,h,mode='full')

y_noisy = y + 0.05*np.random.randn(len(y))

N = len(y_noisy)

x_est = np.fft.fft(y_noisy, N)
H = np.fft.fft(h,N)
H_safe = np.where(np.abs(H) < 1e-3,1e-3,H)
x_recovered = x_est / H_safe
x_recovered = np.real(np.fft.ifft(x_recovered))
print("Max |H|:", np.max(np.abs(H)))
print("Min |H|:", np.min(np.abs(H)))
print("Number of near-zero H values:", np.sum(np.abs(H) < 1e-3))

fig, axs = plt.subplots(4, 1, figsize=(8, 9))
axs[0].plot(x); axs[0].set_title("1. Clean signal x[n]")
axs[1].stem(h); axs[1].set_title("2. Channel impulse response h[n] (multipath)")
axs[2].plot(y_noisy); axs[2].set_title("3. Received distorted signal y = x*h + noise")
axs[3].plot(x_recovered[:n]); axs[3].set_title("4. Recovered signal after FFT equalization")
plt.tight_layout()
plt.show()
print("Original vs recovered (first 10 samples):")
print("x:        ", np.round(x[:10], 3))
print("recovered:", np.round(x_recovered[:10], 3))