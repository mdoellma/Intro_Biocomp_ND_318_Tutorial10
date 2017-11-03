import pandas
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



### --- End Challenge 2---------------------------------------