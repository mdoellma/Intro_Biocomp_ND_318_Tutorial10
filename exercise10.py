import pandas
import numpy
import scipy
import scipy.integrate as spint
from plotnine import *

### --- Begin challenge 1 ------------------------------------




### --- End Challenge 1---------------------------------------
### --- Begin challenge 2-------------------------------------
#state=I/S=state params=r/B
#basic reproduction only initial values

#create ode for each equation

#equations = dS/dt=-BIS dI/dt=BIS-RI dR/dt=RI
def epiSim(y,t,B,r):
    I=y[0]
    S=y[1]
    
    dSdt= (-B*I*S)
    dIdt= (B*I*S)-(r*I)
    dRdt= (r*I)
    
    return[dSdt,dIdt,dRdt]

#put list of B and R parameters into dataframe
paramB=[0.0005,0.005,0.0001,0.00005,0.0001,0.0002,0.0001]
paramr=[0.05,0.5,0.1,0.1,0.05,0.05,0.06]
param_array=numpy.column_stack([paramB,paramR])
param_df=pandas.DataFrame(param_array,columns=['B','r'])

#extract params from dataframe
for i in range(0,6):
    I0=[1]
    S0=[999]
    params=(param_df.B[i],param_df.r[i])
    times=range(0,500)
    #simulate model using odeint
    modelSim=spint.odeint(func=epiSim,y0=(I0,S0),t=times,args=params)
    
### --- End Challenge 2---------------------------------------