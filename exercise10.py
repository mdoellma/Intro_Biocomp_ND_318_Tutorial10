##### Script for Tutorial #10

### Load packages
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *



##### Question 1
# Write custom function for logistic growth
def logGrowth(y, t0, r, K):
    N=y[0]
    dNdt=r*(1-N/K)*N
    return [dNdt]

# Code for the first plot with varying growth rate
### Define parameters and initial conditions
# params=(r, K)
N0=[10]
times=range(0,175)

### Simulate the model using odeint and different values for r
params1=(-0.1, 100)
out1=spint.odeint(func=logGrowth, y0=N0, t=times, args=params1)
params2=(0.1, 100)
out2=spint.odeint(func=logGrowth, y0=N0, t=times, args=params2)
params3=(0.4, 100)
out3=spint.odeint(func=logGrowth, y0=N0, t=times, args=params3)
params4=(0.8, 100)
out4=spint.odeint(func=logGrowth, y0=N0, t=times, args=params4)
params5=(1, 100)
out5=spint.odeint(func=logGrowth, y0=N0, t=times, args=params5)

### Put model outputs in output table
out_df=pandas.DataFrame({"t": times, "N1": out1[:,0], "N2": out2[:,0], "N3": out3[:,0], "N4": out4[:,0], "N5": out5[:,0]})
### Plot simulation output
plot1=ggplot(out_df, aes(x="t", y="N1"))+geom_line()+theme_classic()+ylab("Population Size (N)")+xlab("Time")
plot1+geom_line(aes(x="t", y="N2"), color="red")+geom_line(aes(x="t", y="N3"), color="green")+geom_line(aes(x="t", y="N4"), color="blue")+geom_line(aes(x="t", y="N5"), color="orange")



