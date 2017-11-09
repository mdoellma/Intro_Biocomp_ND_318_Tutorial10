#Exercise 10, question 2 

#import necessary packages 

susceptible = 999
infected = 1
resistant = 0 
N = 1000 

time = range(0, 500)
betta = [0.0005, 0.005, 0.001, 0.00005, 0.0001, 0.0002, 0.0001]
gamma = [0.05, 0.5, 0.1, 0.1, 0.05, 0.05, 0.06]

dfvar = pandas.DataFrame({"time": time, "g1":0, "g2":0, "g3":0, "g4":0, "g5":0, "g6":0, "g7":0})

#for loop to read over table of values, needs fixing  
for i in range(0, len(betta)):
  params = (betta[i], gamma[i])
  modelSim = spint.odeint(func=SIR, t = time, args = betta)
  Q2.iloc[:,i]=modelSim[:,0] #need to fix 
  
modelOutput = pandas.DataFrame({"t":time, "N":modelSim[:,0]})

#calc max daily incidence
#calc max daily prevalence 
#calc % affected over the simulation 
#calc basic reproduction number---------------------------- 
R0 = (betta *(S + I + R))/gamma 
R0 = (betta * N)/gamma 

def SIR( ):
  
