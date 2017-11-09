#Excercise10
#Authors Melissa Stephens and Janice Love

#import packages

#beta and gamma are my params, ds/dt, dI/dt, and dR/dt is my [dNdt]
beta=(.0005,.005,.0001,.00005,.0001,.0002,.0001)
gamma=(.05,0.5,0.1,0.1,0.05,0.06)
In=1
Res=0
Sus=999
times=range(0,600)
N=1000    #state variable
R0=(B0*N)/gamma

#Write a custom function that defines the model
def SIR (y,t,beta,gamma):
	N=y[0]
	dS/dt=-beta*In*Sus
	dI/dt=(beta*In*Sus)-(gamma*In)
	dR/dt=gamma*In

#Make a dataframe to store results
Q2=pandas.DataFrame({"time":time, "

for i in range(0,len(gamma)):
	params=(beta[i],gamma[i])
	modelSim=spint.odeint(func=SIR,y0=N0,t=times,args=params)
	Q2.iloc[:,i]=modelSim[:,0]

ggplot(Q2,aes(x=
