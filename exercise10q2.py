"""
Exercise 10, Q2
Authors: Grant Keller and Kathleen Nicholson

## Module description
"""
from scipy.integrate import odeint as oi
import pandas
from time import sleep

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
    q2df = pandas.DataFrame({"times" : times, "S1" : 0, "I1" : 0, "R1": 0,
                             "S2" : 0, "I2" : 0, "R2": 0,"S3" : 0, "I3" : 0, "R3": 0,
                             "S4" : 0, "I4" : 0, "R4": 0,"S5" : 0, "I5" : 0, "R5": 0,
                             "S6" : 0, "I6" : 0, "R6": 0,"S7" : 0, "I7" : 0, "R7": 0})

    
    for i, b in enumerate(betas):
        params = (b, gammas[i])
        sim = oi(func=simSIR, y0 = (S0, I0, R0), t=times, args=params)
        q2df.iloc[:, i+14] = sim[:, 0] # assigns S values to S#i
        q2df.iloc[:, i] = sim[:, 1] # assigns I values to I#i
        q2df.iloc[:, i+7] = sim[:, 2] # assigns R values to R#i
    
    max_incidence = [] # It - It-1
    max_prevalence = [] # I / (S + I + R)
    percent_affected = [(q2df["I%s"%i][499] + q2df["R%s"%i][499]) / 
                        (q2df["S%s"%i][499] + q2df["I%s"%i][499] + q2df["R%s"%i][499])
                        for i in range(1,8)] # (I + R) / (S + I + R)
    # beta * (S + I + R) / gamma
    basic_reproduction = [betas[i] * (S0 + I0 + R0) / gammas[i] for i in range(7)]
    
    for i in range(1, 8):
        daily_incidence = [q2df["I%s"%i][j] - q2df["I%s"%i][j-1] for j in range(1, 500)]
        daily_prevalence = [q2df["I%s"%i][j] / ( q2df["S%s"%i][j] + q2df["I%s"%i][j] + 
                            q2df["R%s"%i][j]) for j in range(500)]
        max_incidence.append(max(daily_incidence))
        max_prevalence.append(max(daily_prevalence))
    
    for i in range(7):
        print "Case {0}, beta = {1}, gamma = {2}:".format(i+1, betas[i], gammas[i])
        print "Basic reproduction rate: %s"%basic_reproduction[i]
        print "Percent affected by end of simulation: %s"%percent_affected[i]
        print "Maximum incidence, highest # of subsequent infections per case: %s"%max_incidence[i]
        print "Maximum prevalence, max % population affected at any time: %s"%max_prevalence[i]
        sleep(10)
        print "\n\n"

"""
2.

What patterns do you see in these results? Try additional parameter combinations
to identify key values of or trends with β, γ, or R0 (the basic reproduction
number). Add text (a paragraph or two) to the readme file in your GitHub
repository summarizing what you’ve learned. Include the code you generated to
learn about the patterns you summarize as a file in your Github repository as well.
"""
