import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

from scipy.integrate import odeint



def modelTIME(omega, mu, muI, muN, beta, c, alpha, x, nu, sigma, gamma, eta, tau, r, Sei, Sen, theta, d):

    def derivs(state, t):
        S, L, I, N = state
        A = S + L + I + N

        labda = beta * (I + c * N)/A

        v = np.array([S, L, I, N, A])
        u = np.array([[-(labda * (1 - alpha)) -(labda * alpha * sigma) -(labda * alpha * (1 - sigma)) -(mu), 0, 0, 0, +(omega)],
                      [+(labda * (1 - alpha)), -((nu + labda * alpha * (1 - x)) * sigma) -((nu +labda * alpha * (1 - x)) * (1 - sigma)) -(mu), +(gamma * Sei * eta * tau + r),  +(gamma * Sen * eta * tau * d + r), 0],
                      [+(labda * alpha * sigma), +((nu + labda * alpha * (1 - x)) * sigma), -(gamma * Sei * eta * tau + r) -(mu + muI), +(theta), 0],
                      [+(labda * alpha * (1 - sigma)), +((nu + labda * alpha * (1 - x)) * (1 - sigma)), 0, -(gamma * Sen * eta * tau * d + r) -(theta) -(mu + muN), 0]])

        return u.dot(v)

    return derivs


def main():
  sns.set()

  state_0 = [80000, 17000, 100, 200] # S, L, I, N

  params = {
    'omega' : 0.01594,
    'mu'    : 0.015,
    'muI'   : 0.20,
    'muN'   : 0.20,
    'beta'  : 14.75, 
    'c'     : 0.25,  # rel_inf
    'alpha' : 0.031,
    'x'     : 0.65,  # p
    'nu'    : 0.002, # v
    'sigma' : 0.4,
    'gamma' : 0,     # 1.4,  #kneg i.e. treatment rate  
    'eta'   : 0.83,  # l_s
    'tau'   : 0.76,  # tneg 
    'r'     : 0.25,
    'Sei'   : 0.82,  # 2015
    'Sen'   : 0.57,  # 2015
    'theta' : 0.02,
    'd'     : 0.8    # rel_d
  }

  times = np.linspace(0, 100, 1001)


  out = odeint(modelTIME(**params), state_0, times)
  df = pd.DataFrame(np.insert(out, 0, times, axis=1), columns=['time', 'S', 'L', 'I', 'N']).set_index('time')

  df['pop']=df[['S','L','I','N']].sum(axis=1)
  print(df.tail())

  state = df.iloc[-1][['S','L','I','N']].to_list()
  
  params['gamma'] = 1.4
  times = np.linspace(0,30,301)

  out = odeint(modelTIME(**params), state, times)
  df = pd.DataFrame(np.insert(out, 0, times, axis=1), columns=['time', 'S', 'L', 'I', 'N']).set_index('time')

  df['pop']=df[['S','L','I','N']].sum(axis=1)
  print(df.tail())

if __name__ == '__main__':
  main()