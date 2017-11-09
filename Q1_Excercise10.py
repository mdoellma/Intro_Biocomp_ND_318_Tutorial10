#Excercise 10- SImulation modeling with ODEs
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
N0=[10]     ##state variable
times=range(0,600)        ##creates a vector of numbers (list) from 0-600
rval=[-0.1,0.1,0.4,0.8,1.0]        ##access these by rval[0],rval[1],etc

#Make a dataframe to store results
Q1A=pandas.DataFrame({"time":times,"r1":0,"r2":0,"r3":0,"r4":0,"r5":0})

#Write a For loop to loop over list of r-vals. Want 'i' to be as long as the length of the rvals (r changes with everypass)
#Run the simulation using the odeint() function

for i in range(0,len(rval)):
	params=(rval[i],K)     ##at first iteration rval[i]=0, second iter rval[i]=1, etc
	modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
	Q1A.iloc[:,i]=modelSim[:,0]       ##we want all the rows replaced for columns

ggplot(Q1A,aes(x="time",y="r1"))+geom_line()+geom_line(aes(x="time",y="r2"),color='red')+geom_line(aes(x="time",y="r3"),color='blue')+geom_line(aes(x="time",y="r4"),color='green')+geom_line(aes(x="time",y="r5"),color='orange')+theme_classic()

##-----------------------------Plots 2-----------------------------------------
K=[10,50,100]
N0=1
times=range(0,600)
rval=0.2

Q1B=pandas.DataFrame({"time":times,"K1":0,"K2":0,"K3":0})

for i in range(0,len(K)):
        params=(rval,K[i])    
        modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
        Q1B.iloc[:,i]=modelSim[:,0]

ggplot(Q1B,aes(x="time",y="K1"))+geom_line()+geom_line(aes(x="time",y="K2"),color='red')+geom_line(aes(x="time",y="K3"),color='blue')+theme_classic()


##--------------------------------------Plot 3----------------------------------------
K=50
N0=[1,50,100]
times=range(0,600)
rval=0.1

Q1C=pandas.DataFrame({"time":times,"N1":0,"N2":0,"N3":0})

for i in range(0,len(N0)):
        params=(rval,K)                                                               
        modelSim=spint.odeint(func=ddSim,y0=N0[i],t=times,args=rval)
        Q1C.iloc[:,i]=modelSim[:,0]

ggplot(Q1C,aes(x="time",y="N1"))+geom_line()+geom_line(aes(x="time",y="N2"),color='red')+geom_line(aes(x="time",y="N3"),color='green')+theme_classic()
