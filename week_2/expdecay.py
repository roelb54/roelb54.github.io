from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def model(k):

    def derivs(state, t):
        Y = state
        dY = k * state
        return dY
    
    return derivs


t = np.linspace(.1, 10, 101)

state_0 = 1
params = {'k': -1}

out = odeint(model(**params), state_0, t)

plt.plot(t, out)
plt.show()