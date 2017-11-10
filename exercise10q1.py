"""
Exercise 10, Q1
Authors: Grant Keller and Kathleen Nicholson

## Module description
"""

from time import sleep
import pandas
from scipy.integrate import odeint as oi
from plotnine import ggplot, geom_line, labs, aes

def ddsim(y, t0, r, K):
    """
    Population (N) over time function. Returns dN/dt.
    """
    return [r*y[0]*(1-y[0]/K)]

def part1():
    """
    Plots population size vs. time of 5 populations.
    N0 = 10, K = 100.
    r varies.
    """
    times = range(500)
    N0, K = 10, 100
    q1a = pandas.DataFrame({"times":times,
                            "r1":0, "r2":0,
                            "r3":0, "r4":0, "r5":0})
    rs = [-0.1, 0.1, 0.4, 0.8, 1.0]
    for i, r in enumerate(rs):
        params = (r, K)
        sim = oi(func=ddsim, y0=N0, t=times, args=params)
        q1a.iloc[:, i] = sim[:, 0]

    print ggplot(aes(x='times'), data=q1a) +\
        labs(title="population size over time", x="time", y="population size") +\
        geom_line(aes(y='r1'), color='blue') +\
        geom_line(aes(y='r2'), color='red') +\
        geom_line(aes(y='r3'), color='green') +\
        geom_line(aes(y='r4'), color='yellow') +\
        geom_line(aes(y='r5'), color='orange')

def part2():
    """
    Plots population size vs. time of 5 populations.
    N0 = 1, r = 0.2.
    K varies.
    """
    N0, r = 1, 0.2
    times = range(500)
    # list of K-values
    Ks = [10, 50, 100]
    # make Df to store results. Needs column for time and each K.
    q1b = pandas.DataFrame({"times":times, "K1":0,
                            "K2":0, "K3":0})
    # Write a for loop to evaluate model at each K.
    for i, K in enumerate(Ks):
        params = (r, K)
        sim = oi(func=ddsim, y0=N0, t=times, args=params)
        q1b.iloc[:, i] = sim[:, 0]
    print ggplot(aes(x='times', color='K'), data=q1b) +\
        labs(title="population size over time", x="time", y="population size") +\
        geom_line(aes(y='K1'), color='blue') +\
        geom_line(aes(y='K2'), color='red') +\
        geom_line(aes(y='K3'), color='green')

def part3():
    """
    Plots population size vs. time of 5 populations.
    K = 50, r = 0.1.
    N0 varies.
    """
    # define initial values, state variables, time steps, params
    # ex. define initial val (N), time steps, param(k)
    K, r = 50, 0.1
    times = range(500)
    # list of N-values
    N0s = [1, 50, 100]
    # make Df to store results. Needs column for time and each N.
    q1c = pandas.DataFrame({"times":times, "N1":0,
                            "N2":0, "N3":0})
    # Write a for loop to evaluate model at each N.
    for i, N0 in enumerate(N0s):
        params = (r, K)
        sim = oi(func=ddsim, y0=N0, t=times, args=params)
        q1c.iloc[:, i] = sim[:, 0]

    print ggplot(aes(x='times'), data=q1c) +\
        labs(title="population size over time", x="time", y="population size") +\
        geom_line(aes(y='N1'), color='blue') +\
        geom_line(aes(y='N2'), color='yellow') +\
        geom_line(aes(y='N3'), color='green')

if __name__ == '__main__':
    print "Part 1 - N0 = 10; K = 50; r = -0.1, 0.1, 0.4, 0.8, 1.0: "
    part1()
    sleep(5)
    print "Part 2 - N0 = 1; K = 10, 50, 100; r = 0.2: "
    part2()
    sleep(5)
    print "Part 3 - N0 = 1, 50, 100; K = 50; r = 0.1: "
    part3()
