#Excercise 10
#Janice Love and Melissa Stephens

#load necessary packages
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

#open files
#custom function that defines the model differential equations
def ddSim(y,t,r,K):
	N=y[0]
	dNdt=r*(1-N/K)*N
	return [dNdt]

#define parameters, state variables, and time steps for storing the model simulation
K=100
N0=[10] ##state variable
times=range(0,600) ##creates a vector of numbers (list) from 0-600
rval=[-0.1,0.1,0.4,0.8,1.0]  ##access these by rval[0],rval[1],etc

#Make a dataframe to store results
Q1A=pandas.DataFrame({"time":times,"r1":0,"r2":0,"r3":0,"r4":0,"r5":0})

#Write a For loop to loop over list of r-vals. Want 'i' to be as long as the length of the rvals (r changes with everypass)
#Run the simulation using the odeint() function
For i in range(0,len(rval)):
	params=(rval[i],K)  ##at first iteration rval[i]=0, second iter rval[i]=1, etc
	modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
	Q1A.iloc[:,i]=modelSim[:,0] ##we want all the rows replaced for column 0
print Q1A

#put model into a dataframe for plotting purposes
modelOutput=pandas.DataFrame({"t":times,"N":modelSim[:,0]})

#plot simulation output
ggplot (modelOutput,aes((x="t",y="N"))+geom_line()+theme_classic()
