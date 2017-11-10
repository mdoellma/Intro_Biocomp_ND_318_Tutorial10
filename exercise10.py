import pandas
import numpy
import scipy
import scipy.integrate as spint
from plotnine import *

### --- Begin challenge 1 ------------------------------------
def DDSim (y, t, r, K):
    #unpack the parameter variables
    N = y[0]
    return r * (1 - N/K) * N
    
def modelDDSim (N_arr, times, r_arr, K_arr):
    #Initialize variables
    
    #Determine which array has highest length
    max_len = max(len(N_arr), len(r_arr), len(K_arr))
    
    #Dataframe where columns will be added
    output = pandas.DataFrame({"time": times})
    
    #Plot where geom_line() will be added
    plot = ggplot(output, aes(x="time")) + theme_classic()
    #Array for colors
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]
    
    #Loop
    for i in range(max_len):
        #Just initializing some variables whose values will change
        N0 = -1
        r = -1
        K = -1
        
        #Checking if we have only one value or values in an array
        if len(N_arr) == 1:
            N0 = N_arr[0]
        else:
            N0 = N_arr[i]
        if len(r_arr) == 1:
            r = r_arr[0]
        else:
            r = r_arr[i]
        if len(K_arr) == 1:
            K = K_arr[0]
        else:
            K = K_arr[i]
            
        #params variable
        params = (r, K)
        
        #Will return a list of simulated values for the combination of N0, r, K
        sim = spint.odeint(func=DDSim, y0=N0, t=times, args=params)
        
        #String for column name
        col_name = "Pop " + str(i + 1)
        
        #Add column to dataframe
        output[col_name] = sim[:,0]
        
        #Add geom_line to plot
        plot = plot + geom_line(aes(x="time", y=col_name), color=colors[i])
    return plot

#Results:
#Make plot for separate R values
modelDDSim([10], range(0,100), [-0.1, 0.1, 0.4, 0.8, 1], [100])
#Make plot for separate K values
modelDDSim([10], range(0,100), [0.2], [1, 50, 100])
#Make plot for separate N0 values
modelDDSim([1, 5, 100], range(0,100), [0.2], [1, 50, 100])


### --- End Challenge 1---------------------------------------

### --- Begin challenge 2-------------------------------------

#state=I/S=state params=r/B
#basic reproduction only initial values

#create ode for each equation

#equations = dS/dt=-BIS dI/dt=BIS-RI dR/dt=RI
def epiSim(y,t,B,r):
    S=y[0]
    I=y[1]
    R=y[2]
    
    dSdt=(-B*I*S)
    dIdt=(B*I*S)-(r*I)
    dRdt=(r*I)
    
    return[dSdt,dIdt,dRdt]

#put list of B and R parameters into dataframe
paramB=[0.0005,0.005,0.0001,0.00005,0.0001,0.0002,0.0001]
paramr=[0.05,0.5,0.1,0.1,0.05,0.05,0.06]
param_array=numpy.column_stack([paramB,paramr])
param_df=pandas.DataFrame(param_array,columns=['B','r'])

#extract params from dataframe
#dictionary variable
d={}
for i in range(0,7):
    I0=1
    S0=999
    R0=0
    y0=[S0,I0,R0]
    params=(param_df.B[i],param_df.r[i])
    t=range(0,501)
    
    #simulate model using odeint and store in dictionary
    modelSimISR=spint.odeint(epiSim,y0,t,params)
    d["Sim{0}".format(i)]=pandas.DataFrame({'t':t,'S':modelSimISR[:,0],'I':modelSimISR[:,1],'R':modelSimISR[:,2]})

#calculate maximum incidence, maximum prevalence, percent affected and basic reproduction number
inclist=[]
prevlist=[]
percafflist=[]
brnlist=[]
A=list(d.keys())
for i in range(0,7):
    B=A[i]
    df=d[B]
    
    C=[]
    for x in range(0,501):
        if x!=0:
            N=x-1
            Ip=df.iloc[N,0]
            If=df.iloc[x,0]
            incidence=If-Ip
            C.append(incidence)
    M=round(max(C),3)
    inclist.append(M)
    
    D=[]
    for y in range(0,501):
        I=df.iloc[y,0]
        S=df.iloc[y,2]
        R=df.iloc[y,1]
        prev=(I/(S+I+R))
        D.append(prev)
    M=round(max(D),3)
    prevlist.append(M)
    
    I=df.iloc[500,0]
    R=df.iloc[500,1]
    S=df.iloc[500,2]
    percaff=round(((I+R)/(S+I+R)),3)
    percafflist.append(percaff)
    
    I=df.iloc[0,0]
    R=df.iloc[0,1]
    S=df.iloc[0,2]
    B=param_df.B[i]
    r=param_df.r[i]
    brn=round(((B*(S+I+R))/r),3)
    brnlist.append(brn)
    
F=list(range(0,7,1))
Results=pandas.DataFrame(numpy.column_stack([F,paramB,paramr,inclist,prevlist,percafflist,brnlist]),columns=['Simulation','B','r','Max Incidence','Max Prevalence','Percent Affected','Basic Reproduction #'])
print(Results)
### --- End Challenge 2---------------------------------------






