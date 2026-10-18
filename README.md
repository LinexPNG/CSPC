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

## PW2 --- Lab B

### Part 2: Optimization Methods Comparison
- **Convex function ($f(x)$):** All three methods (Gradient Descent, Newton, and SLSQP) successfully converged to the global minimum at $x \approx 3$[cite: 1].
- **Harder landscape ($g(x)$):** Starting points and algorithms heavily influence the results. From $x_0 = 0$, Newton's method converged to a maximum ($g'' < 0$), whereas starting from $x_0 = 2$ it landed on a minimum ($g'' > 0$)[cite: 2]. Gradient descent and SLSQP reliably navigated local vs global constraints based on initial parameters[cite: 1, 2].

### Part 3: Reaction Rate Fitting
- **Fitted Rate Constant ($k$):** $\approx 0.26$[cite: 3]
- The model curve effectively matches the measured concentration data (saved as `PW2/Lab B/kinetics.png`)[cite: 3].

### Part 4: Chemical Equilibrium
- **Equilibrium Extent ($x$):** $\approx 0.66$
- **Equilibrium Amounts:** $H_2 \approx 0.34$ mol, $I_2 \approx 0.34$ mol, $HI \approx 1.33$ mol[cite: 4].
- Both Newton's root-finding method and SLSQP minimization agreed on the final equilibrium composition (saved as `PW2/Lab B/equilibrium.png`)[cite: 4].

### Part 5: Titration Equivalence Point
- **Equivalence Point:** Detected at $V \approx 50.0$ mL where the slope of the pH curve ($\frac{dpH}{dV}$) reaches its maximum peak (saved as `PW2/Lab B/titration.png`)[cite: 4].
