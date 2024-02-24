import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
from typing import Callable


def dy(y: float, k:float) -> float:
    return -k * y

def euler(f:Callable[[float, float], float], y0:float, times:[float]) -> [float]:
    h = times[1] - times[0]

    y = [y0]
    for i in times[1:]:
        y = y + [y[-1] + h * f(y[-1], k)]

    # or
    # y = reduce(lambda y, _: y + [y[-1] + h * f(y[-1], k)], times[1:], [y0])
   
    return y

y0 = 1
k = 0.6
t, h = np.linspace(0, 3, 16, retstep=True)

y = euler(dy, y0, t)
plt.plot(t, y, label=f'$k:{k}$')
plt.plot(t, y0 * np.exp(-k*t), label='$e^{k \\cdot t}$')

plt.legend()
plt.show()



def dy(k:float) -> float:
    return lambda y: -k * y  # return a function requesting y

def model(h: float, dy:Callable[[float], float]):
    g = lambda p: p + h * dy(p) # function to call diff wrt previous value

    return lambda y, _: y + [g(y[-1])] # append next value to current list

y0 = 1
t, h = np.linspace(0, 3, 16, retstep=True) 

params = {'k' : 0.6}
y = reduce(model(h, dy(**params)), t[1:], [y0])

plt.plot(t, y, label=f'${", ".join([f"{k}:{v}" for k, v in params.items()])}$')
plt.plot(t, y0 * np.exp(-k*t), label='$e^{k \\cdot t}$')
plt.legend()
plt.show()


y0 = 1
params = {'k': 2}
t, h = np.linspace(0, 10, 101, retstep=True) 
y = reduce(model(h, dy(**params)), t[1:], [y0])
plt.plot(t, y, label=f'${", ".join([f"{k}:{v}" for k, v in params.items()])}$')
plt.show()



