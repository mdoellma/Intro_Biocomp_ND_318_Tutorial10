#import packages
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

#Define basic model of density-dependent growth
def ddSim (y,t0,r,K):
    N=y[0]
    dNdt=r*(1-N/K)*N
    return [dNdt]
    
#Define a constant carrying capacity and initial population size
K=100 
N0=[10]
times=range(0,500)
  
#Define a list of growth rates for each separate population
rs=[-0.1,0.1,0.4,0.8,1.0]
#Form a dataframe to store population size, with columns labeled for times and each growth rate
store_rs=pandas.DataFrame({"time":times,"r1":0,"r2":0,"r3":0,"r4":0,"r5":0}) 
                                                                             

#Loop that runs through each growth rate in list and models population growth using previously established parameters
for i in range(0,len(rs)): 
    params=(rs[i],K)       
    sim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
    store_rs.iloc[:,i]=sim[:,0] #Store population values in the column appropriate for the growth rate being modeled

#Set up base plot for population curves
rates=ggplot(store_rs,aes(x="time",y="N"))+theme_classic() 
#Add each population curve to graph
rates=rates+geom_line(store_rs,aes(y="r1")) 
rates=rates+geom_line(store_rs,aes(y="r2"))
rates=rates+geom_line(store_rs,aes(y="r3"))
rates=rates+geom_line(store_rs,aes(y="r4"))
rates=rates+geom_line(store_rs,aes(y="r5"))

#Display graphs
rates 

#Define a set growth rate and initial population size
r=0.2 
N0=[1]
times=range(0,500)

#Define list of carrying capacities for each population
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

#Show graph
capacity 