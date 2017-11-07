import pandas
import numpy
import scipy
import scipy.integrate as spint
from plotnine import *

def epiSim(y,t,B,r):
    S=y[0]
    I=y[1]
    R=y[2]
    
    dSdt=(-B*I*S)
    dIdt=(B*I*S)-(r*I)
    dRdt=(r*I)
    
    return[dSdt,dIdt,dRdt]

#put list of B and R parameters into dataframe
paramB=[0.05,0.1,0.05,0.1]
paramr=[0.05,0.05,0.1,0.1]
param_array=numpy.column_stack([paramB,paramr])
param_df=pandas.DataFrame(param_array,columns=['B','r'])

#extract params from dataframe
#dictionary variable
d={}
for i in range(0,4):
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
for i in range(0,4):
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
    
F=list(range(0,4,1))
Results=pandas.DataFrame(numpy.column_stack([F,paramB,paramr,inclist,prevlist,percafflist,brnlist]),columns=['Simulation','B','r','Max Incidence','Max Prevalence','Percent Affected','Basic Reproduction #'])
print(Results)