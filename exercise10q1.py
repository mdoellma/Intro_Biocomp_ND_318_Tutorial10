"""
Exercise 10, Q1
Authors: Grant Keller and Kathleen Nicholson

## Module description
"""

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
    pass

def part3():
    """
    • A plot of population size as a function of time with three
    populations (one line per population) that shows the effect of
    initial population size (N0 = 1, 50, and 100). Use a r = 0.1
    and K = 50 for these simulations.
    """
    pass

if __name__ == '__main__':
    pass