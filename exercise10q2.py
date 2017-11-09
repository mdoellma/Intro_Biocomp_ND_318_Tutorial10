"""
Exercise 10, Q2
Authors: Grant Keller and Kathleen Nicholson

## Module description
"""
from scipy.integrate import odeint as oi


def simSIR(y, t0, beta, gamma):
    """
    Function descriptor.
    
    State: S, I, R
    Param: B
    """
    S, I, R = y
    dSdt = -beta * I * S
    dIdt = beta * I * S - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

if __name__ == '__main__':
    S0, I0, R0 = 999, 1, 0
    times = range(500)
    betas = [0.0005, 0.005, 0.0001, 0.00005, 0.0001, 0.0002, 0.0001]
    gammas = [0.05, 0.5, 0.1, 0.1, 0.05, 0.05, 0.06]
    
    for i, b in enumerate(betas):
        params = (b, gammas[i])
        sim = oi(func=simSIR, y0 = (S0, I0, R0), t=times, args=params)
        q2a.iloc[:, i] = sim[:, 0]
    

"""
2. Susceptible (S), infected (I), and resistant (R). 

The model does, include parameters that describe the transmission of the disease
causing agent and the rate a host recovers from the disease.

The simplest SIR model assumes a constant population size and looks like this:
    
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
