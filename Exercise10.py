#import packages
import os
import numpy as np
import pandas as pd
import scipy
import sklearn
import scipy.integrate as spint
from plotnine import *
from ggplot import *
import matplotlib.pyplot as plt

#set working directory
os.chdir('/Users/omneelay/Desktop/Exercise10/Intro_Biocomp_ND_318_Tutorial10/')

#PART 1.1

def ddSim(y,t0,r,K):
    # "unpack" lists containing state variables (y)
    N=y[0]
    # calculate change in state variables with time, give parameter values # and current value of state variables
    dNdt=r*(1-N/K)*N
    # return list containing change in state variables with time
    return [dNdt]
    
### Define parameters, initial values for state variables, and time steps
rvalues=[-0.1, 0.1, 0.4, 0.8,1.0, 100]
z=0
times=range(0,100)
N0=[10]
columns=["t", "N1", "N2", "N3", "N4", "N5", "N6"]
modelOutput=pd.DataFrame(columns=columns)
modelOutput.t=times

for i in rvalues:
    params=(i,100)
    z=z+1

    ### Simulate the model using odeint
    modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)

    ### put model output in a dataframe for plotting purposes
    Output=pd.DataFrame({"t":times,"N":modelSim[:,0]})
    modelOutput[modelOutput.columns[z]]=(Output.N)

### plot simulation output
plot1=ggplot(modelOutput,aes(x="t"))+geom_line(aes(y="N1"), color='blue')+geom_line(aes(y="N2"), color='red')+geom_line(aes(y='N3'), color='yellow')+geom_line(aes(y='N4'), color='purple')+geom_line(aes(y='N5'), color='green')+geom_line(aes(y='N6'), color='orange')+ggtitle("Different R's")

#Part 1.2
Kvalues=[10,50,100]
z=0
times=range(0,100)
N0=[1]
columns=["t", "N1", "N2", "N3"]
modelOutput=pd.DataFrame(columns=columns)
modelOutput.t=times

for i in Kvalues:
    params=(0.2,i)
    z=z+1

    ### Simulate the model using odeint
    modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)

    ### put model output in a dataframe for plotting purposes
    Output=pd.DataFrame({"t":times,"N":modelSim[:,0]})
    modelOutput[modelOutput.columns[z]]=(Output.N)

### plot simulation output
plot2=ggplot(modelOutput,aes(x="t"))+geom_line(aes(y="N1"), color='blue')+geom_line(aes(y="N2"), color='red')+geom_line(aes(y='N3'), color='green')+ggtitle("Different K's")
#Part 1.3

Nvalues=[1,50,100]
z=0
times=range(0,100)
columns=["t", "N1", "N2", "N3"]
modelOutput=pd.DataFrame(columns=columns)
modelOutput.t=times

for i in Nvalues:
    params=(0.1,50)
    z=z+1
    N0=i

    ### Simulate the model using odeint
    modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)

    ### put model output in a dataframe for plotting purposes
    Output=pd.DataFrame({"t":times,"N":modelSim[:,0]})
    modelOutput[modelOutput.columns[z]]=(Output.N)

### plot simulation output
plot3=ggplot(modelOutput,aes(x="t"))+geom_line(aes(y="N1"), color='blue')+geom_line(aes(y="N2"), color='red')+geom_line(aes(y='N3'), color='green')+ggtitle("Different N's")
plot1.show()
plot2.show()
plot3.show()


##PART 2


