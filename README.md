# Butterworth Noise Filter

## Overview
A short project demonstrating how to design and apply a Butterworth low-pass 
filter to remove noise from a signal, using Python's scipy.signal library.

## Problem
Real-world signals are often corrupted by noise. This project simulates a 
noisy 5 Hz sine wave and applies a Butterworth low-pass filter to recover 
the underlying clean signal.

## Approach
- Generated a synthetic 5 Hz sine wave with added Gaussian noise
- Designed a Butterworth low-pass filter (scipy.signal.butter) with a 
  configurable cutoff frequency and filter order
- Applied the filter using sosfiltfilt for zero-phase filtering
- Visualized the filter's frequency response (gain vs frequency) to confirm 
  correct cutoff behavior
- Compared filtering results across different filter orders (N=2 vs N=8)

## What I learned
- How filter order affects the sharpness of the frequency cutoff
- The tradeoff between smoothing noise and preserving signal detail
- The difference between analyzing a filter's design (frequency response) 
  vs applying it to real data

## How to run
```bash
pip install numpy scipy matplotlib
python butterworth_filter.py
```

## Tech used
Python, NumPy, SciPy, Matplotlib
