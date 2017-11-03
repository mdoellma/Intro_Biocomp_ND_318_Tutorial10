"""
Exercise 10, Q1
Authors: Grant Keller and Kathleen Nicholson

## Module description
"""
<<<<<<< HEAD

import pandas
from scipy.integrate import odeint as oi
from plotnine import *

def ddSim(y, t0, r, K):
    """
    Function descriptor.
    """
    return [r*y[0]*(1-y[0]/K)]

# storage = pandas.DataFrame()
# store_rs.iloc[:,i]=sim[:,0]
# sim=si.odeint(func=ddSim,y0=N0[i],t=times,args=pars)
# numpy.max(sim[:,1]/)
    
def part1():
    """
    """
    times = range(600)
    N0, K = 10, 100
    QIA = pandas.DataFrame({"times":times,
                            "r1":0, "r2":0,
                            "r3":0, "r4":0, "r5":0})
    rs = [-0.1, 0.1, 0.4, 0.8, 1.0]
    for i, r in enumerate(rs):
        params = (r, K)
        sim = oi(func=ddSim, y0=N0, t=times,args=params)
        QIA.iloc[:, i] = sim[:, 0]

    
    # plot data
    
def part2():
    """
    • A plot of population size as a function of time with three 
    populations (one line per population) possessing different 
    carrying capacities (K = 10, 50, and 100). Use r = 0.2 and
    N0 = 1 (these were somewhat arbitrarily chosen to make an 
    informative figure).
    """
def ddSim (y,t,r,K):
    N=y[0]
    dNdt=r*(1-N/K)*N
    return [dNdt]
# define initial values (these don't change), state variables, time steps, params (that aren't changing)
# ex. define initial val (N), time steps, param(k)
r=0.2
N0=[1]
times=range(0,2)
# list of r-values
Ks=[10,50,100]
# make Df to store results. Needs column for time and each r. 
Q1B=pandas.DataFrame({"times":times,"K1":0,"K2":0,"K3":0})
# Write a for loop to evaluate model at each r. 
for i in range(0,len(Ks)):
    params=(Ks[i],r)
    sim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
    Q1B.iloc[:,i]=sim[:,0]
print ggplot(aes(x='times'), data=Q1B)+\
    xlab("time")+ylab("capacity") +\
    geom_line(aes(y='K1'), color='blue') +\
    geom_line(aes(y='K2'), color='red') +\
    geom_line(aes(y='K3'), color='green') 





def part3():
    """
    • A plot of population size as a function of time with three
    populations (one line per population) that shows the effect of
    initial population size (N0 = 1, 50, and 100). Use a r = 0.1
    and K = 50 for these simulations.
    """
def ddSim (y,t,r,K):
    N=y[0]
    dNdt=r*(1-N/K)*N
    return [dNdt]
# define initial values (these don't change), state variables, time steps, params (that aren't changing)
# ex. define initial val (N), time steps, param(k)
r=0.1
K=[50]
times=range(0,3)
# list of r-values
Ns=[1,50,100]
# make Df to store results. Needs column for time and each r. 
Q1C=pandas.DataFrame({"times":times,"N1":0,"N2":0,"N3":0})
# Write a for loop to evaluate model at each r. 
for i in range(0,len(Ns)):
    params=(Ns[i],r)
    sim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
    Q1C.iloc[:,i]=sim[:,0]
print ggplot(aes(x='times'), data=Q1C)+\
    xlab("time")+ylab("population size") +\
    geom_line(aes(y='N1'), color='blue') +\
    geom_line(aes(y='N2'), color='yellow') +\
    geom_line(aes(y='N3'), color='green') 


if __name__ == '__main__':
    pass
