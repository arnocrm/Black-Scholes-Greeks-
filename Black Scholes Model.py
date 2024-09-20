#Black Scholes Model
import numpy as np
from scipy.stats import norm

r=0.01  # Interet Rate 
S=30    #Spot
K= 40   # Strike
T=240/365 # Maturity
sigma= 0.3 #Vol

def blackScholes(r,S,K,T,sigma,type="C"):
    "Calculate BS Price for a Call (C) or Put (P)"
    d1=(np.log(S/K)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2=d1-sigma*np.sqrt(T)
    try:
        if type=="C":
            price=S*norm.cdf(d1,0,1)-K*np.exp(-r*T)*norm.cdf(d2,0,1)
        elif type=="P":
            price=K*np.exp(-r*T)*norm.cdf(-d2,0,1)-S*norm.cdf(-d1,0,1)
        return price
    except:
        print("Please confirm all option parameter")

print(round(blackScholes (r,S,K,T,sigma,type="P"),2))




