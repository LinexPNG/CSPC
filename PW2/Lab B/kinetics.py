import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

data = np.loadtxt('kinetics.csv', delimiter=',', skiprows=1)
t, C = data[:, 0], data[:, 1]
C0 = C[0]

def total_error(k):
    k_val = k[0] if isinstance(k, (list, np.ndarray)) else k
    return np.sum((C - C0 * np.exp(-k_val * t))**2)

res = minimize(total_error, x0=[0.5], bounds=[(0, 5)], method="SLSQP")
fitted_k = res.x[0]
print("Fitted k:", fitted_k)

t_line = np.linspace(min(t), max(t), 200)
C_fit = C0 * np.exp(-fitted_k * t_line)

plt.figure(figsize=(8, 5))
plt.scatter(t, C, color='red', label='Measured Data')
plt.plot(t_line, C_fit, color='blue', label=f'Fitted Curve (k={fitted_k:.4f})')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.grid(True)
plt.savefig('kinetics.png')