# CSPC Lab
# CSPC - Computer Science for Physics and Chemistry

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- Python simulation environment with NumPy and Pytest, tracked via Git and hosted on GitHub.

**Speed comparison (loop vs NumPy):**
- numpy : 0.00616 s

**Tests:** all passing? (yes)

**Conclusion:**
- The environment was successfully configured, all tests passed, and NumPy executed the large simulation in just 0.00616 seconds.
## PW1 --- Lab B
The observed data shows exponential decay over time, decreasing from the initial count. The observed data matches the analytical law extremely well. The Snakemake pipeline automates figure generation whenever source data or the plotting script changes.
## PW2 --- Lab A

* **Mean Acceleration:** -9.81 m/s²
* **Why acceleration is noisy:** Differentiation magnifies measurement noise. Taking two derivatives (position -> velocity -> acceleration) significantly increases the noise level compared to the smooth position data.
* **Integration observation:** Integration acts as a cumulative sum which suppresses random noise, successfully restoring the original position data within about 1 meter accuracy.
