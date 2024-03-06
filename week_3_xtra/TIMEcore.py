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

        StoL = S * labda * (1 - alpha)
        StoI = S * labda * alpha * sigma
        StoN = S * labda * alpha * (1 - sigma)

        Sin  = A * omega 
        Sout = S * mu

        LtoI = L * (nu + labda * alpha * (1 - x)) * sigma
        LtoN = L * (nu + labda * alpha * (1 - x)) * (1 - sigma)
        Lout = L * mu

        ItoL = I * (gamma * Sei * eta * tau + r)
        Iout = I * (mu + muI)

        NtoL = N * (gamma * Sen * eta * tau * d + r)
        NtoI = N * theta
        Nout = N * (mu + muN)

        dS = -StoL - StoN - StoI - Sout + Sin
        dL = StoL + ItoL + NtoL - LtoI - LtoN - Lout
        dI = StoI + LtoI - ItoL - Iout + NtoI
        dN = StoN + LtoN - NtoL - Nout - NtoI

        return [dS, dL, dI, dN]

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
  df = pd.DataFrame(np.insert(out,0, times, axis=1), columns=['time', 'S', 'L', 'I', 'N']).set_index('time')

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