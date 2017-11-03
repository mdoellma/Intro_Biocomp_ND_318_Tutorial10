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


# Code for the second plot with varying carrying capacities 

# Code for thirst plot with varying initial population size




##### Question 2

# Write custom function for SIR model
def SIRmodel(y, t0, beta, gamma):
    S=y[0]
    I=y[1]
    R=y[2]
    
    dSdt=-beta*I*S
    dIdt=beta*I*S-gamma*I
    dRdt=gamma*I
    
    return [dSdt, dIdt, dRdt]

### Simulate output with different betas and gammas, create plots, and calculate disease metrics 
times=range(0,500) #run simulation for 500 days
N0=[999, 1, 0] #initial values = 999 susceptible, 1 infected, and 0 resistent
# Create lists to loop over 
betas=[0.0005, 0.005, 0.0001, 0.00005, 0.0001, 0.0002, 0.0001]
gammas=[0.05, 0.5, 0.1, 0.1, 0.05, 0.05, 0.06]
plotnames=["Parameters 1", "Parameters 2","Parameters 3","Parameters 4","Parameters 5","Parameters 6", "Parameters 7"] 
# Create a list to store plots 
plots=["Plot1", "Plot2","Plot3","Plot4","Plot5","Plot6","Plot7"] 
# Create a dataframe to store disease metric calculations
out_SIR=pandas.DataFrame({"ParameterSet": plotnames, "maxIncidence": 0, "maxPrevalence": 0,"percAffected": 0,"r0": 0})

# Do the stuff!
for i in range(0, len(betas)):
    # Set parameters for iteration
    params=(betas[i], gammas[i])
    # Simulate model dynamics
    sim=spint.odeint(func=SIRmodel, y0=N0, t=times, args=params)
    # Put output into a dataframe
    sim_df=pandas.DataFrame({"t": times, "dSdt": sim[:,0], "dIdt": sim[:,1], "dRdt": sim[:,2]})
    # Plot S, I, and R versus time
    plots[i]=ggplot(sim_df, aes(x="t"))+geom_line(aes(y="dSdt"))+theme_classic()+xlab("Time")+ylab("N")+geom_line(aes(y="dIdt"), color = "red")+geom_line(aes(y="dRdt"), color = "blue")+ggtitle(plotnames[i])
    # Calculate max incidence
    incidence=range(500) #create list to store incidence values
    for j in range(0, 500): #calculate incidence for every time step
        incidence[j]=sim_df.iloc[j,0]-sim_df.iloc[j-1,0]
    out_SIR.iloc[i, 1]=max(incidence) #get the max
    # Calculate max prevalence
    prevalence=sim_df.iloc[:,0]/1000 #calculate prevalence at every time ste
    out_SIR.iloc[i, 2]=max(prevalence) #get the max
    # Calculate percent affected
    out_SIR.iloc[i, 3]=(sim_df.iloc[499,0]+sim_df.iloc[499,1])/100
    # Calculate R0
    out_SIR.iloc[i,4]=(betas[i]*1000)/gammas[i]

### Look at the results!
print(plots)
print(out_SIR)



