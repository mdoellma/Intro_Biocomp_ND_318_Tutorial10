#Tutorial 10 exercise: Simulation modeling with ordinary differential equations (ODEs)
#Authors: Janice Love, Melissa Stephens 

#Date: November 9, 2017 

#Load packages
import pandas
import scipy
import scipy.integrate as spint 
from plotnine import * 

def ddSim (y,t,r,K):
  N = y[0]
  dNdt = r*(1-N/K)* N
  return [dNdt]

params = (0.3, 10)
N0 = [0.01]
times = range (0, 600)

modelSim = spint.odeint (func = ddSim, y0 = N0, t = times, args = params)

#model output into dataframe for plotting 
modelOutput = pandas.DataFrame({"t": times, "N":modelSim[:,0]})

#plot simulation output
ggplot (modelOutput, aes(x = "t", y = "N")) + geom_line() + theme_classic()

#---------------------------------------------------------------------------------------------
#Question 1:

#plot 1: 
r = [-0.1, 0.1, 0.4, 0.8, 1.0]
K = 100
N0 = [10] 

Q1A=pandas.DataFrame({"time":times,"r1":0,"r2":0,"r3":0,"r4":0,"r5":0})

for i in range(0,len(r)):
	params=(r[i],K)  ##at first iteration r[i]=0, second iter r[i]=1, etc
	modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
	Q1A.iloc[:,i]=modelSim[:,0] ##we want all the rows replaced for column 0
print Q1A

#put model into a dataframe for plotting purposes
modelOutput=pandas.DataFrame({"t":times,"N":modelSim[:,0]})

#plot simulation output
ggplot (modelOutput,aes((x="t",y="N"))+geom_line()+theme_classic()


#plot 2: 
K = [10, 50, 100]
r = 0.2
N0 = 1 

plot2df = pandas.DataFrame({"time":times, "K1":0, "K2":0, "K3":0})
for i in range(0,len(K)):
  params = (K[i],r)
  modelSim2 = spint.odeint(func=ddSim, y0=N0, t = times, args = params)
  plot2df.iloc[:,i]=modelSim[:,0]
print plot2df

#Plot 2 output into dataframe
plot2_output = pandas.DataFrame({"t":times, "N":modelSim2[:,0]})
#plot output 
ggplot (plot2_output,aes((x = "t", y = "N"))+geom_line() + theme_classic()


def ddsim2 (y, t0, r, K):
  -
  -
  return [answer]

#plot 3 
K = 50
r = 0.1
N0 = [1, 50, 100]

for i in range(0,len(N0)):
  params = (N0[i],)
#---------------------------------------------------------------------------------------------


