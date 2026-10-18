import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('titration.csv', delimiter=',', skiprows=1)
V, pH = data[:, 0], data[:, 1]

slope = np.gradient(pH, V)
eq_index = np.argmax(slope)
eq_volume = V[eq_index]

print("Equivalence point volume:", eq_volume)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(V, pH, color='green', linewidth=2)
ax1.axvline(x=eq_volume, color='red', linestyle='--', label=f'Equivalence Point: {eq_volume:.2f} mL')
ax1.set_xlabel('Volume of Base')
ax1.set_ylabel('pH')
ax1.legend()
ax1.grid(True)

ax2.plot(V, slope, color='purple', linewidth=2)
ax2.axvline(x=eq_volume, color='red', linestyle='--', label=f'Peak Slope: {eq_volume:.2f} mL')
ax2.set_xlabel('Volume of Base')
ax2.set_ylabel('Slope (dpH/dV)')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('titration.png')