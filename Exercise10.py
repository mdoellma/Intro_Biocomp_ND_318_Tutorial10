#import packages
import os
import numpy as np
import pandas as pd
import scipy
import sklearn
import scipy.integrate as spint
from plotnine import *
from ggplot import *
import matplotlib.pyplot as plt

#set working directory
#os.chdir('/Users/omneelay/Desktop/Exercise10/Intro_Biocomp_ND_318_Tutorial10/')
os.chdir('C:\\Users\\jsh\\OneDrive\\github\\BioComp\\Intro_Biocomp_ND_318_Tutorial10\\')
#PART 1.1

def ddSim(y,t0,r,K):#c
    # "unpack" lists containing state variables (y)
    N=y[0]
    # calculate change in state variables with time, give parameter values # and current value of state variables
    dNdt=r*(1-N/K)*N
    # return list containing change in state variables with time
    return [dNdt]
    
### Define parameters, initial values for state variables, and time steps
rvalues=[-0.1, 0.1, 0.4, 0.8,1.0, 100]
z=0
times=range(0,100)
N0=[10]
columns=["t", "N1", "N2", "N3", "N4", "N5", "N6"]
modelOutput=pd.DataFrame(columns=columns)
modelOutput.t=times

for i in rvalues:
    params=(i,100)
    z=z+1

    ### Simulate the model using odeint
    modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)

    ### put model output in a dataframe for plotting purposes
    Output=pd.DataFrame({"t":times,"N":modelSim[:,0]})
    modelOutput[modelOutput.columns[z]]=(Output.N)

### plot simulation output
plot1=ggplot(modelOutput,aes(x="t"))+geom_line(aes(y="N1"), color='blue')+geom_line(aes(y="N2"), color='red')+geom_line(aes(y='N3'), color='yellow')+geom_line(aes(y='N4'), color='purple')+geom_line(aes(y='N5'), color='green')+geom_line(aes(y='N6'), color='orange')+ggtitle("Different R's")

#Part 1.2
Kvalues=[10,50,100]
z=0
times=range(0,100)
N0=[1] #initial value
columns=["t", "N1", "N2", "N3"]
modelOutput=pd.DataFrame(columns=columns)
modelOutput.t=times

for i in Kvalues:
    params=(0.2,i) #parameter/k value
    z=z+1

    ### Simulate the model using odeint
    modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)

    ### put model output in a dataframe for plotting purposes
    Output=pd.DataFrame({"t":times,"N":modelSim[:,0]})
    modelOutput[modelOutput.columns[z]]=(Output.N)

### plot simulation output
plot2=ggplot(modelOutput,aes(x="t"))+geom_line(aes(y="N1"), color='blue')+geom_line(aes(y="N2"), color='red')+geom_line(aes(y='N3'), color='green')+ggtitle("Different K's")
#Part 1.3

Nvalues=[1,50,100]
z=0
times=range(0,100)
columns=["t", "N1", "N2", "N3"]
modelOutput=pd.DataFrame(columns=columns)
modelOutput.t=times

for i in Nvalues:
    params=(0.1,50)
    z=z+1
    N0=i

    ### Simulate the model using odeint
    modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)

    ### put model output in a dataframe for plotting purposes
    Output=pd.DataFrame({"t":times,"N":modelSim[:,0]})
    modelOutput[modelOutput.columns[z]]=(Output.N)

### plot simulation output
plot3=ggplot(modelOutput,aes(x="t"))+geom_line(aes(y="N1"), color='blue')+geom_line(aes(y="N2"), color='red')+geom_line(aes(y='N3'), color='green')+ggtitle("Different N's")
plot1.show()
plot2.show()
plot3.show()


#PART 2
    
#define function
def Sim2(y,t0,g,B):
    #unpack state variables from list y
    S=y[0]
    I=y[1]
    R=y[2]
    #calculate changes in state variables
    dSdt=-1*B*I*S
    dIdt=(B*I*S)-(g*I)
    dRdt=g*I
    #return lists containing changes in state variables with time
    return [dSdt,dIdt,dRdt]
    
#define parameters, initial values for state variables, and time steps
gvalues=[.05,.5,.1,.1,.05,.05,.06] #original g values
#gvalues=[.05,.5,2,.1,.05,37,.06] #testing different parameters
Bvalues=[.0005,.005,.0001,.00005,.0001,.0002,.0001] #original values
#Bvalues=[.0005,.005,1,5,.0001,.0002,.0001] #testing different parameters
parameters=pd.DataFrame({"B":Bvalues,"g":gvalues})
N0=[999,1,0]
times=range(0,500)
m=-1

#for loop for each set of parameters and to print out results and calculate values
for row in parameters.iterrows():
    m=m+1
    params=(gvalues[m],Bvalues[m])
    

    #simulate model
    modelSim=spint.odeint(func=Sim2,y0=N0,t=times,args=params)
    modelOutput=pd.DataFrame({"t":times,"S":modelSim[:,0],"I":modelSim[:,1],"R":modelSim[:,2]})

    #calculate max incedence and prevalence
    incidence=[0]*499
    o=-1
    for row in modelOutput.iterrows():
        if o==498:
            break
        else:    
            o=o+1
            incidence[o]=modelOutput.I[o+1]-modelOutput.I[o]
                
    prevalence=[0]*500
    o=-1
    for row in modelOutput.iterrows():
        o=o+1
        prevalence[o]=(modelOutput.I[o])/(modelOutput.S[o]+modelOutput.I[o]+modelOutput.R[o])
    
    #calculate percent affected and basic reproduction number
    percentaffected=100*(modelOutput.I[499]+modelOutput.R[499])/(modelOutput.S[499]+modelOutput.I[499]+modelOutput.R[499])
    brr=Bvalues[m]*(modelOutput.S[499]+modelOutput.I[499]+modelOutput.R[499])/gvalues[m]
    
    #print results
    print("for gamma value:",gvalues[m]," and beta value:",Bvalues[m])
    print("    the max incidence is:",max(incidence))
    print("    the max prevalence is:",max(prevalence))
    print("    the percent affected is:",percentaffected,"%")
    print("    the basic reproduction number is:",brr)
    print("")
    



#What we learned:
#-increases  the gamma value appears to have a inverse-corelation with the 4 calculated values
#-increase the beta values appears to have a direct correlation with the 4 calculated values. Increase beta directly increase the spread of the disease. 
#This seems logical, as the beta parameter represents the number contacts per unit of time, making new infections. While gamma actually represents the mean infectious period. The basic reproduction value is beta/gamma. 
#Thus, based on this equation, the most important factor in a disease spread may be these two values. A disease that spreads frequently/quick and is present in the individual for a long period of time, would increase the max incidence, prevalaence, and total percent affected. 
#-The above code used to determine this, is # out below the original gamma and beta values. 