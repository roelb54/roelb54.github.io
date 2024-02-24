from scipy.integrate import odeint
from types import SimpleNamespace
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

state_0 = [1000.0, 1.0, 0.0]
params = {'b': 0.1, 'c': 5.0, 'd':5.0}


def model(b:float, c:float, d:float):

    def SIR(state:[float], t:[float]):
        S, I, R = state
        N = S + I + R
        dS = -b * c * I/N * S
        dI = b * c * I/N * S - I/d
        dR = I/d
        return [dS, dI, dR]
    
    return SIR

t = np.linspace(0, 60, 3001, retstep=True)
v = odeint(model(**params), state_0, t)

plt.plot(t, v[:,0], label='$\\frac{dS}{dt}$')
plt.plot(t, v[:,1], label='$\\frac{dI}{dt}$')
plt.plot(t, v[:,2], label='$\\frac{dR}{dt}$')
plt.legend()
plt.xlabel('days')
plt.xlabel('S, I, R')
plt.show()