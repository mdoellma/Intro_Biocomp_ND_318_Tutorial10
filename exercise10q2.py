"""
Exercise 10, Q2
Authors: Grant Keller and Kathleen Nicholson

## Module description
"""
def simSIR(y,t,I,S):
    """
    Function descriptor.
    
    State: S, I, R
    Param: B
    """
    beta=y[0]
    gamma=y[1]
    dSdt = -beta*I*S
    dIdt = beta*I*S - gamma*I
    dRdt = gamma*I
    return [dSdt,dIdt,dRdt]
S=999
I=1
R=0
time=range(0,500)

if __name__ == '__main__':
    pass

"""
2. Often simulation models are used to develop an intuition about how a system
works. We describe the system using some simple differential equations and then
we try a variety of parameter values to explore how the system responds. All
the while we are making the strong assumption that the real system we care about
behaves somewhat like our simple model.

Let’s use a simple model of disease transmission to learn about this process!
One simple model used for simulating disease transimission is called an SIR
model because it considers three sub-groups of a population - susceptible (S),
infected (I), and resistant (R). This model doesn’t actually model the disease
causing agent at all, but rather focuses on the host of the disease. The model
does, however, include parameters that describe the transmission of the disease
causing agent and the rate a host recovers from the disease. The simplest SIR
model assumes a constant population size and looks like this:

    dSdt = -β*I*S
    dIdt = β*I*S - γ*I
    dRdt = γ*I
    
When considering dynamics of a disease epidemic we can quantify:
• incidence - the number of new infections occurring over a defined time
interval (It − It−1) 

• prevalence - the fraction of the population that is infected at a given
time ( I/(S+I+R) )

• percent affected - the fraction of the population that was sick at any time
during an epidemic ( (I+R)/(S+I+R) )

• basic reproduction number ( R0 = β(S+I+R)/γ ) - the number of cases one case
generates on average over its infectious period in an otherwise uninfected population

Write a custom function describing the SIR model above, and for each row in the
table below, use the pair of parameter values (β and γ) to simulate the model
for 500 days. 

Start each simulation with 999 susceptible, 1 infected, and 0 resistant
individuals. For each simulation, calculate the maximum daily incidence and
maximum daily prevalence. Also calculate the percent affected over the
simulation (use the last time step of the simulation for this) and the basic
reproduction number (you can actually do this without simulating, since we
give you β, γ, and the initial S + I + R.

    β    γ
0.0005 0.05
0.005 0.5
0.0001 0.1
0.00005 0.1
0.0001 0.05
0.0002 0.05
0.0001 0.06

What patterns do you see in these results? Try additional parameter combinations
to identify key values of or trends with β, γ, or R0 (the basic reproduction
number). Add text (a paragraph or two) to the readme file in your GitHub
repository summarizing what you’ve learned. Include the code you generated to
learn about the patterns you summarize as a file in your Github repository as well.
"""
