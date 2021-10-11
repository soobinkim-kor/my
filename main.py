import numpy as np
import scipy.special
import scipy.stats

S0 = 1
mu = 0.05
sigma = 0.2
K = 1.2
r = 0.05
T = 5
N = 100
dt=T/N
Pi=2
Spath = np.zeros(shape=N+1)
Spath[0] = S0


def BSM_call(S, K, tau, r, sigma):
    import numpy as np
    import scipy.stats
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    
    return S * scipy.stats.norm.cdf(d1, 0, 1) - K * np.exp(-r * tau) * scipy.stats.norm.cdf(d2, 0, 1)

def BSM_call_prc(S, K, tau, r, sigma):

    
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    
    return S * scipy.stats.norm.cdf(d1, 0, 1) - K * np.exp(-r * tau) * scipy.stats.norm.cdf(d2, 0, 1)



def discrete_asset_path(S0,mu,sigma,T,N):
    dt=T/N
    Spath = np.zeros(shape=N+1)
    Spath[0] = S0

    for i in range(1, N+1):
        z = np.random.standard_normal()  #z는 정규분포를 따름
        Spath[i] = Spath[i-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)  #discrete asset model공식

    return(Spath)

def BSM_prc_path(Spath,K,T,mu,r,sigma):
    if T>0:
      d1 = (np.log(Spath / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
      d2 = d1 - sigma * np.sqrt(T)
      N1 = 0.5*(1+scipy.special.erf(d1/np.sqrt(2)))
      N2 = 0.5*(1+scipy.special.erf(d2/np.sqrt(2)))
      Cpath = Spath*N1-K*np.exp(-r*(T))*N2 # 유럽형 콜옵션 가격에 대한 유일한 해 공식
    
    else:
      Cpath = max(Spath-K,0)

    return Cpath





def BSM_call_delta(S, K, T, r, sigma):
    import numpy as np
    import scipy.stats
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    return scipy.stats.norm.cdf(d1[0], 0, 1) #cumaltive distribution함수(리턴값은 확률)
    
    

def del_path(Spath,K,T,mu,r,sigma,Pi):
    bsm_call_prc0 = BSM_call_prc(Spath, K, T, r, sigma)
    N=Spath.size-1
    dt=T/N
    Spath = np.zeros(shape=N+1) 
    cash = np.zeros(shape=N+1)
    Pi = np.zeros(shape=N+1)
    asset = np.zeros(shape=N+1)
    error = np.zeros(shape=N+1)
    Cpath = np.zeros(shape=N+1)
 


    #Spath[0] = S0
    Spath[0] = 1
    cash[0] = 1
    
    asset[0] = BSM_call_delta(Spath, K, T, r, sigma)
    Pi[0] = asset[0] * Spath[0] + cash[0]
    error[0] = 0

    Cpath[0] = bsm_call_prc0[0]


    for i in range(1, N+1):
        z = np.random.standard_normal()
        Spath[i] = Spath[i-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
        Pi[i] = asset[i-1] * Spath[i] + (1 + r * dt) * cash[i-1]
        asset[i] = BSM_call_delta(Spath[i], K, T - i * dt, r, sigma)
        cash[i] = (1 + r * dt) * cash[i-1] + (asset[i-1] - asset[i]) * Spath[i]
        Cpath[i]=BSM_call_prc(Spath[i], K, T - i * dt, r, sigma) 
        error[i] = abs(Cpath[i] - Pi[i] - (bsm_call_prc0[0] - Pi[0]) * np.exp(r * i * dt))
    return Pi

a=discrete_asset_path(1,0.05,0.1,3,1000)
BSM_prc_path(a,200,20,0.05,0.0168,0.0099)
del_path(a,200,5,0.02,0.03,0.35,10)