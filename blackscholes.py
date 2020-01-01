import numpy as np
import pandas as pd
from scipy import log, exp, sqrt, stats

def bscall(S, E, T, rf, sig):
    d1 = (log(S/E)+(rf+sig*sig/2.0*T)/sig*sqrt(T))
    d2 = d1-sig*sqrt(T)
    
    return S*stats.norm.cdf(d1)-E*exp(-rf*T)*stats.norm.cdf(d2)
    
def bsput(S, E, T, rf, sig):
    d1 = (log(S/E)+(rf+sig*sig/2.0)*T)/(sig*sqrt(T))
    d2 = d1-sig*sqrt(T)
    
    return -S*stats.norm.cdf(-d1)+E*exp(-rf*T)*stats.norm.cdf(-d2)


if __name__ == "__main__":

    print("Black Scholes Program")
    
    S = float(input("Enter the Stock Price:  "))          #stock price
    E = float(input("Enter the Strike Price:  "))            #strike price
    T = float(input("Enter the Expiry Date:  "))          #expiry date
    rf = float(input("Enter the Risk Free Interest Rate (Decimal Form):  ")) #risk-free interest rate
    sig = float(input("Enter the Sigma Value (Volatility):  "))#volatility of the stock
    
    print("call option price = ", bscall(S, E, T, rf, sig))
    print("put option price = ", bsput(S, E, T, rf, sig))