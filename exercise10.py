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

# Code for the first plot, using a for loop to vary growth rate
### Define parameters and initial conditions
# params=(r, K)
r=[-0.1, 0.1, 0.4, 0.8, 1] #make list of r's to loop over
N0=[10]
times=range(0,175)

### Create dataframe to store model outputs 
out_df=pandas.DataFrame({"t": times, "N1": 0, "N2": 0, "N3": 0, "N4": 0, "N5": 0})

### Simulate the model using odeint and different values for r in a for loop
for i in range(0, len(r)):
    params=(r[i], 100)
    out=spint.odeint(func=logGrowth, y0=N0, t=times, args=params)
    out_df.iloc[:,i]=out[:,0]
### Put model outputs in output table
### Plot simulation output
plot1=ggplot(out_df, aes(x="t", y="N1"))+geom_line()+theme_classic()+ylab("Population Size (N)")+xlab("Time")
plot1+geom_line(aes(x="t", y="N2"), color="red")+geom_line(aes(x="t", y="N3"), color="green")+geom_line(aes(x="t", y="N4"), color="blue")+geom_line(aes(x="t", y="N5"), color="orange")

# Code for the second plot with varying carrying capacities 
#define parameters

N02=[1]
K2=[10,50,100]
times=range(0,100)

#create dataframe to store outputs
outdata=pandas.DataFrame({"t":times, "N1": 0, "N2": 0, "N3": 0})

#simulate model with loop
for i in range(0,len(K2)):
    params2=(0.2,K2[i])
    out2=spint.odeint(func=logGrowth, y0=N02, t=times, args=params2)
    outdata.iloc[:,i]=out2[:,0]

#plot output
plot2=ggplot(outdata, aes(x="t", y="N1"))+geom_line()+theme_classic()+ylab("Population Size (N)")+xlab("Time")
plot1+geom_line(aes(x="t", y="N2"), color="red")+geom_line(aes(x="t", y="N3"), color="green")


# Code for the third plot with varying intial population sizes
# Define parameters
# params=(r, K)
params_prob3=(.1,50)
#define intial population sizes
N0_pop1=[10]
N0_pop2=[50]
N0_pop3=[100]
#define time interval
times=range(0,175)
##### Simulate the model using odeint and different values for N0
N0_pop1_sim=spint.odeint(func=logGrowth, y0=N0_pop1, t=times, args=params_prob3)
N0_pop2_sim=spint.odeint(func=logGrowth, y0=N0_pop2, t=times, args=params_prob3)
N0_pop3_sim=spint.odeint(func=logGrowth, y0=N0_pop3, t=times, args=params_prob3)
#### Put model outputs in output table
N0_df=pandas.DataFrame({"t": times, "P1": N0_pop1_sim[:,0], "P2": N0_pop2_sim[:,0], "P3": N0_pop3_sim[:,0]})
### Plot simulation output
plot3=ggplot(N0_df, aes(x="t", y="P1"))+geom_line(color='mediumblue')+theme_classic()+ylab("Population Size (N)")+xlab("Time")
plot3+geom_line(aes(x="t",y="P2"),color='deeppink')+geom_line(aes(x="t",y="P3"),color='darkorchid')

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



