import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import odeint

def model(k):

    def deriv(y, t):
        dydt = -k * y
        return dydt

    return deriv


t = np.linspace(0, 20, 21)

y0 = 1
params = {'k': 2}

out = odeint(model(**params), y0, t)
plt.plot(t, out)
plt.show()
