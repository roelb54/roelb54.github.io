from scipy.integrate import odeint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

state_0 = [1, 1, 1]

def model(a, b, c):

    def lorenz(state, t):
        X, Y, Z = state
        dX = a * X + Y * Z
        dY = b * (Y-Z)
        dZ = -X*Y + c*Y -Z
        return [dX, dY, dZ]
    
    return lorenz

times = np.linspace(0, 100, 10001)
params = {'a':-8/3, 'b':-10, 'c': 28}

out = odeint(model(**params), state_0, times)

df = pd.DataFrame({'t': times, 'X':out[:,0], 'Y': out[:,1],'Z':out[:,2] }).set_index('t')

df.plot(subplots=True, layout=(2,2), color='blue')

plt.show()