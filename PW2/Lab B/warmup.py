import numpy as np
from scipy.optimize import newton, minimize

def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

x_gd = 0.0
lr = 0.05
for _ in range(500):
    step = lr * df(x_gd)
    x_gd -= step
    if abs(step) < 1e-8:
        break
print("2A GD:", x_gd)

res_newton_2a = newton(df, x0=0.0, fprime=d2f)
print("2A Newton:", res_newton_2a)

res_slsqp_2a = minimize(f, x0=[0.0], method="SLSQP")
print("2A SLSQP:", res_slsqp_2a.x[0])

def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

for x0 in [0.0, 2.0]:
    print(f"\n--- Starting from x0 = {x0} ---")
    
    x_gd_2b = x0
    for _ in range(1000):
        step = 0.01 * dg(x_gd_2b)
        x_gd_2b -= step
        if abs(step) < 1e-8:
            break
    print("2B GD:", x_gd_2b)
    
    res_newton_2b = newton(dg, x0=x0, fprime=d2g)
    curvature = d2g(res_newton_2b)
    print("2B Newton:", res_newton_2b, "| d2g:", curvature, "(Min)" if curvature > 0 else "(Max)")
    
    res_slsqp_2b = minimize(g, x0=[x0], method="SLSQP")
    print("2B SLSQP:", res_slsqp_2b.x[0])