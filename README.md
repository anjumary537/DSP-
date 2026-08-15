# DSP Python Practice

## Goal
Learn core DSP building blocks by implementing them from scratch with NumPy/SciPy, understand the theory behind each, and simulate realistic scenarios like wireless channel distortion and equalization.

## Topics covered so far

- **FFT / IFFT** — converting signals between time and frequency domain
- **Convolution** — modeling how a signal is transformed by a system (e.g. a multipath wireless channel)
- **FFT-based channel equalization** — recovering a clean signal from a distorted + noisy received signal
- **Cross-correlation** — detecting a known pattern hidden inside a noisy signal (signal synchronization)

## Scripts

### `convolution.py`
Simulates a signal passing through a multipath channel (a few delayed, attenuated copies of itself), adds noise, then attempts to recover the original signal using FFT-based equalization (`X(f) = Y(f) / H(f)`).

**What it demonstrates:**
- Building a signal and a channel impulse response
- Convolving them to simulate real-world distortion
- Using FFT to move to frequency domain, where the recovery math is simple division instead of deconvolution
- A subtle bug that inflated the "safe division" clip in the wrong direction (`H_safe = np.where(np.abs(H) > 1e-3, ...)` instead of `<`), and the fix

### `correlation.py`
Hides a known "sync pattern" inside a long noisy signal, then uses cross-correlation to find exactly where it starts — the same principle real receivers use for frame/timing synchronization.

**What it demonstrates:**
- Cross-correlation vs convolution (no flipping of the pattern)
- Detecting a known signal buried in random noise
- Peak detection and correcting `np.correlate`'s index offset back to the true position in the signal

## Coming next

- FIR/IIR filter design and comparison
- Benchmarking `np.convolve` vs `scipy.signal.fftconvolve` on longer signals

## Setup

```bash
pip install numpy scipy matplotlib
python convolution.py
python correlation.py
```
