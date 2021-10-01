import numpy as np
import math
############
############
#np.power(x,y) = x^y
#np.sqrt(x,y)=x^(1/y)
#math.erf(x) = error function for x
#np.log(x) = log x
#max(x,y) = x,y 중 큰 값
#min(x,y) = x,y 중 작은 값
#np.sign(x) = 부호
#np.pi = 파이 값 \
#np.exp(x) = e의 x제곱
############
############

def ch10(S,E,r,sigma,tau):
  if tau>0:
    d1=(np.log(S/E) + (r+0.5*np.power(sigma,2))*(tau))/(sigma*np.sqrt(tau))
    d2= d1-sigma*np.sqrt(tau)
    N1=0.5*(1+math.erf(d1/np.sqrt(2)))
    N2=0.5*(1+math.erf(d2/np.sqrt(2)))
    C=S*N1-E*np.exp(-r*tau)*N2
    Cdelta=N1
    Cvega=S*np.sqrt(tau)*np.exp(-0.5*np.power(d1,2))/np.sqrt(2*np.pi)
    P=C+E*np.exp(-r*(tau))-S
    Pdelta=Cdelta-1
    Pvega=Cvega
  else:
    C=max(S-E,0)
    Cdelta=0.5*(np.sign(S-E)+1)
    Cvega=0
    P=max(E-S,0)
    Pdelta=Cdelta-1
    Pvega=0
  
  return C,Cdelta,Cvega,P,Pdelta,Pvega

def ch08(S,E,r,sigma,tau):
  if tau>0:
    d1=(np.log(S/E)+(r+0.5*np.power(sigma,2))*(tau))/(sigma*np.sqrt(tau))
    d2=d1-sigma*np.sqrt(tau)
    N1=0.5*(1+math.erf(d1/np.sqrt(2)))
    N2=0.5*(1+math.erf(d2/np.sqrt(2)))
    C=S*N1-E*np.exp(-r*(tau))*N2
    Cdelta=N1
    P=C+E*np.exp(-r*tau)-S
    Pdelta=Cdelta-1
  else:
    C=max(S-E,0)
    Cdelta=0.5*(np.sign(S-E)+1)
    P=max(E-S,0)
    Pdelta=Cdelta-1
  return C, Cdelta,P,Pdelta

#Program for Chapter14

#parameters
r=0.03
S=2
E=2
T=3
tau=T
sigma_true=0.3


C_true,Cdelta,P,Pdelta=ch08(S,E,r,sigma_true,tau)

#starting value

sigmahat=np.sqrt(2*abs((np.log(S/E)+r*T)/T))

#Newtons method

tol=1e-8
sigma=sigmahat
sigmadiff=1
k=1
kmax=100
while(sigmadiff>=tol and k<kmax):
  C,Cdelta,Cvega,P,Pdelta,Pvega=ch10(S,E,r,sigma,tau)
  increment=(C-C_true)/Cvega
  sigma=sigma-increment
  k=k+1
  sigmadiff=abs(increment)

print(sigma)
