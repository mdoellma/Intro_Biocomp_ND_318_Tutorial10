#Exercise 10, question 2 
#Authors: Melissa Stephens and Janice Love 

#Load packages
import numpy
import pandas
from scipy.optimize import minimize
from scipy.stats import norm
from scipy.stats import chi2
from plotnine import* 

susceptible = [999]
infected = [1]
resistant = [0] 
N = [susceptible, infected, resistant] 
N = [999,1,0]

time = range(0, 500)
betta = [0.0005, 0.005, 0.001, 0.00005, 0.0001, 0.0002, 0.0001]
gamma = [0.05, 0.5, 0.1, 0.1, 0.05, 0.05, 0.06]


#calc max daily incidence
#calc max daily prevalence 
#calc % affected over the simulation 


def SIR(y, t, betta, gamma ):
  susceptible = y[0]
  infected = y[1]
  resistant = y[2]
  
  dSdt = -betta*infected*susceptible
  dIdt = (betta * infected * susceptible)-(gamma*infected)
  dRdt = (gamma * infected)
  
  return [dSdt, dIdt, dRdt]

#df for values   
SIRdf = pandas.DataFrame({"time":time, "S":0, "I":0, "R":0})
cols = ["S", "I", "R", "time"]
SIRdf = SIRdf[cols]

for i in range(0,7):
	params=(betta[i],gamma[i])
	modelSim=spint.odeint(func=SIR,y0=N,t=time,args=params) ##Because N has three values, there will be three columns
	for j in range(0,3):
	    SIRdf.iloc[:,j]=modelSim[:,j]
	    

Q2plot = ggplot(SIRdf,aes(x="time", y = "S")) + geom_line() #susceptible 
Q2plot = Q2plot + geom_line(aes(x = "time", y = "I"),  color = "red") #infected
Q2plot = Q2plot +geom_line(aes(x="time", y = "R" ), color = "blue") #resistant 
print Q2plot

#percent affected 
perAff = (SIRdf.I[499] + SIRdf.R[499]) / (SIRdf.S[499]+SIRdf.I[499] + SIRdf.R[499])
print ('Percent affected is:', perAff*100)

#prevalence 
prev = [0]*500
z = -1 
for row in SIRdf.iterrows():
    z = z + 1
    prev[z] = ((SIRdf.I[z]) / (SIRdf.S[z] + SIRdf.I[z] + SIRdf.R[z]))

print ("The maximum prevalence is", max(prev))
#incidence
incid = [0]*500
z = -1 
for row in SIRdf.iterrows(): #needs to be fixed 
    z = z + 1
    incid[z] = ((SIRdf.I[z] - SIRdf.I[z-1]


#calc basic reproduction number---------------------------- 
R0 = (betta *(S + I + R))/gamma 
R0 = (betta * N)/gamma 

Q2=pandas.DataFrame({"betta":betta,"gamma":gamma,"Incidence":0,"prevalence":0,"percent_affected":0,"R0":0})


Q2.R0 = (Q2.betta * 1000)/ Q2.gamma
print Q2.R0 

