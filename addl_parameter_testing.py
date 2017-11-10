#testing additional parameters for last part of Q2
#Authors: Janice Love and Melissa Stephens
#Date: November 10, 2017

#Load packages
import numpy
import pandas
from scipy.optimize import minimize
from scipy.stats import norm
from scipy.stats import chi2
from plotnine import* 

#-----------variables---------------------------------------------------
susceptible = [999]
infected = [1]
resistant = [0] 
N = [susceptible, infected, resistant] 
N = [999,1,0]

time = range(0, 500)
betta = [0.05, 0.5, 0.1, 0.005, 0.01, 0.02, 0.01]
gamma = [0.05, 0.5, 0.1, 0.1, 0.05, 0.05, 0.06]

#-----------function-------------------------------------------
def SIR(y, t, betta, gamma ):
  susceptible = y[0]
  infected = y[1]
  resistant = y[2]
  
  dSdt = -betta*infected*susceptible
  dIdt = (betta * infected * susceptible)-(gamma*infected)
  dRdt = (gamma * infected)
  
  return [dSdt, dIdt, dRdt]
  
#--------------------data handling--------------------------------------------
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

#calc % affected over the simulation
perAff = (SIRdf.I[499] + SIRdf.R[499]) / (SIRdf.S[499]+SIRdf.I[499] + SIRdf.R[499])
print ('Percent affected is:', perAff*100)

#calc max daily prevalence 
prev = [0]*500
z = -1 
for row in SIRdf.iterrows():
    z = z + 1
    prev[z] = ((SIRdf.I[z]) / (SIRdf.S[z] + SIRdf.I[z] + SIRdf.R[z]))

print ("The maximum prevalence is", max(prev))

##calc max daily incidence
incid = [0]*499
z = -1 
for row in SIRdf.iterrows(): 
    if z == 498:
        break
    else:
        z = z + 1
        incid[z]=SIRdf.I[z+1]-SIRdf.I[z]
print "The maximum daily incidence is: ", max(incid)

#-----------variables---------------------------------------------------
susceptible = [999]
infected = [1]
resistant = [0] 
N = [susceptible, infected, resistant] 
N = [999,1,0]

time = range(0, 500)
betta = [0.0005, 0.005, 0.001, 0.00005, 0.0001, 0.0002, 0.0001]
gamma = [0.5, 0.5, 1, 1, 0.5, 0.5, 0.6]

#calc max daily prevalence 
prev = [0]*500
z = -1 
for row in SIRdf.iterrows():
    z = z + 1
    prev[z] = ((SIRdf.I[z]) / (SIRdf.S[z] + SIRdf.I[z] + SIRdf.R[z]))

print ("The maximum prevalence is", max(prev))

##calc max daily incidence
incid = [0]*499
z = -1 
for row in SIRdf.iterrows(): 
    if z == 498:
        break
    else:
        z = z + 1
        incid[z]=SIRdf.I[z+1]-SIRdf.I[z]
print "The maximum daily incidence is: ", max(incid)

#testing addtional parameters --------------------------------------------------
