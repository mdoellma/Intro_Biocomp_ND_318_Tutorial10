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

time = range(0, 500)
betta = [0.0005, 0.005, 0.001, 0.00005, 0.0001, 0.0002, 0.0001]
gamma = [0.05, 0.5, 0.1, 0.1, 0.05, 0.05, 0.06]

dfvar = pandas.DataFrame({"time": time, "g1":0, "g2":0, "g3":0, "g4":0, "g5":0, "g6":0, "g7":0})

#for loop to read over table of values, needs fixing  
for i in range(0, len(betta)):
  params = (betta[i], gamma[i])
  modelSim = spint.odeint(func=SIR, t = time, args = betta)
  Q2.iloc[:,i]=modelSim[:,0] #need to fix 
  
modelOutput = pandas.DataFrame({"t":time, "N":modelSim[:,0]})

#calc max daily incidence
#calc max daily prevalence 
#calc % affected over the simulation 
#calc basic reproduction number---------------------------- 
R0 = (betta *(S + I + R))/gamma 
R0 = (betta * N)/gamma 

def SIR(y, t, betta, gamma ):
  susceptible = y[0]
  infected = y[1]
  resistant = y[2]
  
  dSdt = -betta*infected*susceptible
  dIdt = (betta * infected * susceptible)-(gamma*infected)
  dRdt = (gamma * infected)
  
  return [dSdt, dIdt, dRdt]

#df for values   
SIRdf = pandas.DataFrame({"time":times, "S":0, "I":0, "R":0})
for i in range(0,len(gamma)):
	params=(beta[i],gamma[i])
	modelSim=spint.odeint(func=SIR,y0=N0,t=times,args=params) ##Because N0 has three values, there will be three columns
	for j in range(0,3):
	    Q2.iloc[:,j]=modelsim[:,j]
	    

Q2plot = ggplot(Q2,aes(x="time", y = "S")) + geom_line #susceptible 
Q2plot = Q2plot + ggplot(Q2, aes(x = "time", y = "I") + geom_line(color = "red")) #infected
Q2plot = Q2plot + ggplot(Q2, aes(x = "time", y = "R")+geom_line(color = "blue")) #resistant 
