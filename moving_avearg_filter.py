import numpy as np
import matplotlib.pyplot as plt

def moving_average(signal, window=5):
    half = window // 2
    result = []
    for i in range(len(signal)):
        start = max(0, i - half)
        end = min(len(signal), i + half + 1)
        window_values = signal[start:end]
        avg = sum(window_values) / len(window_values)
        result.append(avg)
    return np.array(result)

# generate a simple test signal both versions will use
test_signal = [10, 20, 30, 40, 50, 40, 30, 20, 10]
print("Python output:", moving_average(test_signal, window=3))