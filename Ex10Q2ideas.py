#Load packages
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

#Total population, N
N = 1000

#Initial number of susceptible, infected, and recovered individuals (S0, I0, R0)
S0, I0, R0 = 999, 1, 0

#unpack lists containing state variables (y)
Y0 = [S0, I0, R0]

#The SIR model differential equations
def ddSim(y, t, N, beta, gamma):
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

#parameters
beta = [0.0005, 0.005, 0.0001, 0.00005, 0.0001, 0.0002, 0.0001]
gamma = [0.05, 0.5, 0.1, 0.1, 0.05, 0.05, 0.06]


#Define parameters, initial values for state variables, and time steps
params=(,) #not sure what these parameters should be?
N0=[1000]
times=range(0,500)


#Simulate the model using odeint
modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)

#put model output in a dataframe for plotting purposes
modelOutput=pandas.DataFrame({"t":times,"N":modelSim[:,0]})
#plot simulation output
ggplot(modelOutput,aes(x="t",y="N"))+geom_line()+theme_classic()


