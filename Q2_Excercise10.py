#Excercise10
#Authors Melissa Stephens and Janice Love

#import packages
import numpy
import pandas
from scipy.optimize import minimize
from scipy.stats import norm
from scipy.stats import chi2
from plotnine import*

#beta and gamma are my params, ds/dt, dI/dt, and dR/dt is my [dNdt]

beta=(.0005,.005,.0001,.00005,.0001,.0002,.0001)
gamma=(.05,0.5,0.1,0.1,0.05,0.06)
In=1
Res=0
Sus=999
N0=[Sus,In,Res]
times=range(0,500)
    #state variables. y is a list of state variables.(I,R,S) need to unpack these one at a time in the custom function
R0=(B0*N)/gamma

#Write a custom function that defines the model. Unpack state variables one at a time. Then one differential equation for each state variable
def SIR (y,t,beta,gamma):
	Sus=y[0]
	In=y[1]
	Res=y[2]
	dSdt=-beta*In*Sus
	dIdt=(beta*In*Sus)-(gamma*In)
	dRdt=gamma*In
	return [dSdt,dIdt,dRdt]

#Make a dataframe with beta, gamma, max daily incidence, max daily prevalence, percent affected, reproduction number
Q2=pandas.DataFrame({"beta":beta,"gamma":gamma,"Incidence":0,"prevalence":0,"percent_affected":0,"R0":beta*1000/gamma)

for i in range(0,len(gamma)):
	params=(beta[i],gamma[i])
	modelSim=spint.odeint(func=SIR,y0=N0,t=times,args=params) ##Because N0 has three values, there will be three columns
	Q2.percent_affected[i]= ##always going to be on row i. Because our dataframe has a different combination of columns

ggplot(Q2,aes(x=
