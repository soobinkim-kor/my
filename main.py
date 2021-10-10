import numpy as np
import math
import scipy.special
import scipy.stats



def discrete_asset_path(S0,mu,sigma,T,N):
    dt=T/N
    Spath = np.zeros(shape=N+1)
    Spath[0] = S0

    for i in range(1, N+1):
        z = np.random.standard_normal()
        Spath[i] = Spath[i-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)  

    return(Spath)

def BSM_prc_path(Spath,K,T,mu,r,sigma):
    if T>0:
      d1 = (np.log(Spath / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
      d2 = d1 - sigma * np.sqrt(T)
      N1 = 0.5*(1+scipy.special.erf(d1/np.sqrt(2)))
      N2 = 0.5*(1+scipy.special.erf(d2/np.sqrt(2)))
      Cpath = Spath*N1-K*np.exp(-r*(T))*N2
    else:
      Cpath = max(Spath-K,0)

    return Cpath


def del_path(Spath,K,T,mu,r,sigma,Pi):
  BSM_prc_path0 = BSM_prc_path(Spath, K, T, mu, r, sigma)
  N=Spath.size-1
  dt=T/N
  Spath = np.zeros(shape=N+1)
  cash = np.zeros(shape=N+1)
  Pi = np.zeros(shape=N+1)
  asset = np.zeros(shape=N+1)
  error = np.zeros(shape=N+1)
  Cpath = np.zeros(shape=N+1)


  Spath[0] = S0
  cash[0] = 1
  asset[0] = BSM_call_delta(Spath, K, T, r, sigma)
  Pi[0] = asset[0] * Spath[0] + cash[0]
  error[0] = 0
  Cpath[0] = BSM_prc_path0


  for i in range(1, N+1):
      z = np.random.standard_normal()
      Spath[i] = Spath[i-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
      Pi[i] = asset[i-1] * Spath[i] + (1 + r * dt) * cash[i-1]
      asset[i] = BSM_call_delta(Spath[i], K, T - i * dt, r, sigma)
      cash[i] = (1 + r * dt) * cash[i-1] + (asset[i-1] - asset[i]) * Spath[i]
      Cpath[i]=BSM_prc_path(Spath[i], K, T - i * dt, r, sigma) 
      error[i] = abs(Cpath[i] - Pi[i] - (BSM_prc_path0 - Pi[0]) * np.exp(r * i * dt))
  
  return Pi
print(BSM_prc_path(discrete_asset_path(1,0.05,0.1,3,1000),200,20,0.05,0.0168,0.0099))
