"""
Exercise 10, Q2
Authors: Grant Keller and Kathleen Nicholson

Simulates SIR disease model for identical populations with
    varying disease parameters to compare what effect these parameters
    have on disease outcomes.
"""
from time import sleep
from scipy.integrate import odeint as oi
import pandas

def simSIR(y, t0, beta, gamma):
    """
    Calculates the change in disease Susceptible, Infected, and Resistance
    individuals over the course of a disease simulation.
    State: S, I
    Param: B
    """
    S, I = y
    dsdt = -beta * I * S
    didt = beta * I * S - gamma * I
    drdt = gamma * I
    return [dsdt, didt, drdt]

if __name__ == '__main__':
    S0, I0, R0 = 999, 1, 0
    TIMES = range(500)
    BETAS = [0.0005, 0.005, 0.0001, 0.00005, 0.0001, 0.0002, 0.0001]
    GAMMAS = [0.05, 0.5, 0.1, 0.1, 0.05, 0.05, 0.06]
    Q2DF = pandas.DataFrame({"times" : TIMES, "S1" : 0, "I1" : 0, "R1": 0,
                             "S2" : 0, "I2" : 0, "R2": 0,"S3" : 0, "I3" : 0, "R3": 0,
                             "S4" : 0, "I4" : 0, "R4": 0,"S5" : 0, "I5" : 0, "R5": 0,
                             "S6" : 0, "I6" : 0, "R6": 0,"S7" : 0, "I7" : 0, "R7": 0})

    for i, b in enumerate(BETAS):
        params = (b, GAMMAS[i])
        sim = oi(func=simSIR, y0=(S0, I0), t=TIMES, args=params)
        Q2DF.iloc[:, i+14] = sim[:, 0] # assigns S values to S#i
        Q2DF.iloc[:, i] = sim[:, 1] # assigns I values to I#i
        Q2DF.iloc[:, i+7] = sim[:, 2] # assigns R values to R#i

    MAX_INC = [] # It - It-1
    MAX_PREV = [] # I / (S + I + R)
    PERCENT_AFFECT = [(Q2DF["I%s"%i][499] + Q2DF["R%s"%i][499]) /
                      (Q2DF["S%s"%i][499] + Q2DF["I%s"%i][499] + Q2DF["R%s"%i][499])
                      for i in range(1, 8)] # (I + R) / (S + I + R)
    # beta * (S + I + R) / gamma
    BASIC_REPRO = [BETAS[i] * (S0 + I0 + R0) / GAMMAS[i] for i in range(7)]

    for i in range(1, 8):
        daily_incidence = [Q2DF["I%s"%i][j] - Q2DF["I%s"%i][j-1] for j in range(1, 500)]
        daily_prevalence = [Q2DF["I%s"%i][j] / ( Q2DF["S%s"%i][j] + Q2DF["I%s"%i][j] +
                                                 Q2DF["R%s"%i][j]) for j in range(500)]
        MAX_INC.append(max(daily_incidence))
        MAX_PREV.append(max(daily_prevalence))

    for i in range(7):
        print "Case {0}, beta = {1}, gamma = {2}:".format(i+1, BETAS[i], GAMMAS[i])
        print "Basic reproduction rate: %s"%BASIC_REPRO[i]
        print "Percent affected by end of simulation: %s"%PERCENT_AFFECT[i]
        print "Maximum incidence, highest # of subsequent infections per case: %s"%MAX_INC[i]
        print "Maximum prevalence, max percent population affected: %s"%MAX_PREV[i]
        sleep(10)
        print "\n\n"

"""
2.

What patterns do you see in these results? Try additional parameter combinations
to identify key values of or trends with B, y, or R0 (the basic reproduction
number). Add text (a paragraph or two) to the readme file in your GitHub
repository summarizing what you’ve learned. Include the code you generated to
learn about the patterns you summarize as a file in your Github repository as well.
"""
