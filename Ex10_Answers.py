#load packages
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

def ddSim(y,t0,r,K):
    #unpack the state vector
    N=y[0]
    
    #running the formula
    dNdt=r*(1-N/K)*N
    
    #return as list
    return [dNdt]

##Q1 A    
# these are the constants    
K=100
N0=[10]
times=range(0,100)
    
#growth rates of each line 
rs=[-0.1,0.1,0.4,0.8,1.0]
#store information in dataframe
store_rs=pandas.DataFrame({"time":times,"r1":0,"r2":0,"r3":0,"r4":0,"r5":0})

#loop through each r value in the list
for i in range(0,len(rs)):
    params=(rs[i],K)
    sim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
    store_rs.iloc[:,i]=sim[:,0]

#plot for population curves
rates=ggplot(store_rs,aes(x="time",y="N"))+theme_classic()

#add each population to the graph
rates=rates+geom_line(store_rs,aes(y="r1"))
rates=rates+geom_line(store_rs,aes(y="r2"))
rates=rates+geom_line(store_rs,aes(y="r3"))
rates=rates+geom_line(store_rs,aes(y="r4"))
rates=rates+geom_line(store_rs,aes(y="r5"))

#show graph
rates

##Q1 B

#Constants
r=0.2 
N0=[1]
times=range(0,100)

#Carrying capacity list
Ks=[10,50,100] 
#Form a dataframe to store population size with columns for each carrying capacity and times modeled 
store_Ks=pandas.DataFrame({"time":times,"K1":0,"K2":0,"K3":0})
                                                               
#Set up loop that runs through each carrying capacity in list and models population growth using other parameters 
for i in range(0,len(Ks)): 
    params=(r,Ks[i])       
    sim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
    #store population values in appropriate column for current carrying capacity 
    store_Ks.iloc[:,i]=sim[:,0] 

#Set up base plot for population curves
capacity=ggplot(store_Ks,aes(x="time",y="N"))+theme_classic()
capacity=capacity+geom_line(store_Ks,aes(y="K1"))
capacity=capacity+geom_line(store_Ks,aes(y="K2"))
capacity=capacity+geom_line(store_Ks,aes(y="K3"))

#show graph
capacity

#Question 2#################################################################################################

#importing necessary packages
import scipy
import scipy.integrate as spint
import numpy
import matplotlib.pyplot as plt

#defining the SIR model
def SIR_model(y, t, beta, gamma):
    S = y[0]
    I = y[1]
    R = y[2]
    
    dSdt=(-beta*I*S)
    dIdt=(beta*I*S-(gamma*I))
    dRdt=(gamma*I)
    
    return (dSdt, dIdt, dRdt)

#Defining constant values
N = [999, 1, 0]
S0=999
I0=1
R0=0

#lists of beta and gamma values
beta=numpy.array([.0005, .005, .0001, .00005, .0001, .0002, .0001])
gamma=numpy.array([.05, .5, .1, .1, .05, .05, .06])

#Creating dataframe for S, I, and R
df_S=pandas.DataFrame({"time":times,"beta1":0,"beta2":0,"beta3":0,"beta4":0,"beta5":0,"beta6":0,"beta7":0})
df_I=pandas.DataFrame({"time":times,"beta1":0,"beta2":0,"beta3":0,"beta4":0,"beta5":0,"beta6":0,"beta7":0})
df_R=pandas.DataFrame({"time":times,"beta1":0,"beta2":0,"beta3":0,"beta4":0,"beta5":0,"beta6":0,"beta7":0})

t=numpy.linspace(0,100)

#loop for beta and gamma table values
for i in range(0,len(beta)):
    params=(beta[i],gamma[i])
    sim=spint.odeint(func=SIR_model,y0=N,t=times,args=params)
    df_S.iloc[:,i]=sim[:,0]
    df_I.iloc[:,i]=sim[:,1]
    df_R.iloc[:,i]=sim[:,2]


plt.figure(figsize=[6,4])
plt.plot(t, solution[:, 0], label="S(t)")
plt.plot(t, solution[:, 1], label="I(t)")
plt.plot(t, solution[:, 2], label="R(t)")
plt.show()

##Max Daily Incidence
MDI=np.diff(df_I.iloc[:,1])
maxI=numpy.max(MDI)
print("MDI")
print(maxI)

##Max Daily Prevelance
MDP=maxI/1000
print("Max Daily Prevalence")
print(MDP)

##Percent Affected Over Simulation
smallS=numpy.min(df_S.iloc[:,0])
pas=(1/smallS)
print("Percent Affected Over Simulation")
print(pas)

##Basic Reproduction Number
S0=999
I0=1
R0=0
beta=numpy.array([.0005, .005, .0001, .00005, .0001, .0002, .0001])
gamma=numpy.array([.05, .5, .1, .1, .05, .05, .06])
basicReproductionNumber=(((beta*(S0+I0+R0))/gamma))
print("BasicReproductionNumber")
print(basicReproductionNumber)


