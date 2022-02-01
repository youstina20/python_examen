## 3. Question Bonus : Implémentation de la formule Pricer d’option avec Python

from math import log, exp,sqrt
import numpy as np
def d1(S,K,X,T,r,sigma):
    return(log(S/K)+(r+sigma**2/2)*T)/(sigma*sqrt(T))

def d2(S,K,T,r,sigma):
    return d1(S,K,T,r,sigma)-sigma*sqrt(T)

def c(S,N,X,r,T):
  return (S*N(d1)-X*exp(-r*T)*N(d2))

def p(S,N,X,r,T):
  return((X*exp(-r*T)*N(-d2)-(S*N(-d1))))