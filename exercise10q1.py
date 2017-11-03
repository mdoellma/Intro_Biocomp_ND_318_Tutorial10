"""
Exercise 10, Q1
Authors: Grant Keller and Kathleen Nicholson

## Module description
"""
# list of r-values
rs=[-0.1,0.1,0.4,0.8,1.0]
# make Df to store results. Needs column for time and each r. 
storage=pandas.DataFrame({"time":times,"r1":0,"r2":0,"r3":0,"r4":0,"r5":0})
# Write a for loop to evaluate model at each r. 
for i in range(0,len(rs)):
    params=(rs[i],K)
    sim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
    Q1A.iloc[:,i]=sim[:,0]


if __name__ == '__main__':
    pass

"""
1. Imagine you’ve been tasked with giving a lecture to teach 
high school students about density-dependent population growth.

You’ve been told to generate the three figures described below
to demonstrate the influence of growth rate (r), carrying capacity 
(K), and initial population size (N0) on temporal dynamics of
a population. 

Write a script with all code necessary to generate the three figures
below.

• A plot of population size as a function of time with five 
populations (one line per population) possessing different
maximum growth rates (r = -0.1, 0.1, 0.4, 0.8, and 1.0). 
Use K = 100 and N0 = 10 (these were somewhat arbitrarily chosen 
to make an informative figure).

• A plot of population size as a function of time with three 
populations (one line per population) possessing different 
carrying capacities (K = 10, 50, and 100). Use r = 0.2 and
N0 = 1 (these were somewhat arbitrarily chosen to make an 
informative figure).

• A plot of population size as a function of time with three
populations (one line per population) that shows the effect of
initial population size (N0 = 1, 50, and 100). Use a r = 0.1
and K = 50 for these simulations.

Think about how for-loops might help make your code more efficient!
"""