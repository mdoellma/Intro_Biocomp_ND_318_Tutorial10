#load packages

import pandas
import scipy
import scipy.integrate as spint
from plotnine import *


#growth rates of each line r=(-0.1,0.1,0.4,0.8,1.0)

def ddSim(y,t0,r,K):
    #unpack the state vector
    N=y[0]
    
    # these are the constants    
    K=100
    N0=[10]
    times=range(0,1000)
    
    #running the formula
    dNdt=r*(1-N/K)*N
    
    #return as list
    return [dNdt]
    
# Simulate the model using odeint
modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)

modelOutput=pandas.DataFrame({"t":times,"N":modelSim[:,0]})

ggplot(modelOutput,aes(x="t",y="N"))+geom_line()+theme_classic()

