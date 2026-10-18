import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

def k_imbalance(x):
    return ((2 * x)**2) / ((a - x) * (b - x)) - K

x_newton = newton(k_imbalance, x0=0.5)

res_slsqp = minimize(lambda x: k_imbalance(x[0])**2, x0=[0.5], bounds=[(0, 0.999)], method="SLSQP")
x_slsqp = res_slsqp.x[0]

print("Newton x:", x_newton)
print("SLSQP x:", x_slsqp)

nH2 = a - x_slsqp
nI2 = b - x_slsqp
nHI = 2 * x_slsqp
print(f"Equilibrium amounts -> H2: {nH2:.4f}, I2: {nI2:.4f}, HI: {nHI:.4f}")

x_vals = np.linspace(0, 0.99, 200)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, a - x_vals, label='H2', color='blue')
plt.plot(x_vals, b - x_vals, label='I2', color='green')
plt.plot(x_vals, 2 * x_vals, label='HI', color='orange')
plt.axvline(x=x_slsqp, color='red', linestyle='--', label=f'Equilibrium x={x_slsqp:.4f}')
plt.xlabel('Extent x')
plt.ylabel('Amount (mol)')
plt.legend()
plt.grid(True)
plt.savefig('equilibrium.png')