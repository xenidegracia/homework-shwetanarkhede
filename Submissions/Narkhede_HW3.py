# Forecasting Assignment 3
# Name: Shweta Narkhede
# Last Edited: Sept 14th, 2020

# %%
# Importing the modules
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week3.txt'
filepath = os.path.join('/Users/owner/Documents/GitHub/homework-shwetanarkhede/data/', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Calculating some basic properites
print(min(flow))
print(max(flow))
print(np.mean(flow))
print(np.std(flow))


#%% September Flows in 2020

ilist = [] # Making and empty list to store index values of interest

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets the specified crieteria
for i in range(len(flow)):
        if month[i] == 9 and year[i]== 2020 : # by changing year, data for specific year can be pieced out
                ilist.append(i)

# Shows how many times crieteria was met
#print(len(ilist))
# Grabs the data of interest
sept_flows_20 = [flow[j] for j in ilist]
sept_day_20 = [day[j] for j in ilist]
# Plotting data for visual analysis
plt.plot(sept_flows_20)
plt.title('September 2020')
#plt.xlabel('Days')
plt.ylabel('Daily streamflow (cfs)')
#%% Pulling out data that had values greater than prediction in 2020
ilist2 =[]
for i in range(len(flow)):
        if flow [i] > 62 and month[i] == 9 and year[i]==2020:
                ilist2.append(i)
# Shows how many times crieteria was met

print("Number of times flow was greater than prediction in Sept 2020 =",len(ilist2))
sept_20_flows_g = [flow[j] for j in ilist2]
# Exceedence 
print( "Percent times daily streamflow exceeded than prediction in 2020 =",len(sept_20_flows_g)/len(sept_flows_20)*100)

# Calcualting mean percentage exceedence in flow
percent_incr = []
for i in range(0,len(sept_20_flows_g)):
        perc = (sept_20_flows_g[i]-62)/62*100
        percent_incr.append(perc)
print("Mean percent exceedence (2020) = ",np.mean(percent_incr)) 



#%% September flows from 1989 - 2020

ilist3 = [] # Making and empty list to store index values of interest

for i in range(len(flow)):
        if month[i] == 9 and year[i]<= 2000:  # for the data before 2000 add year[i]< 2000
                ilist3.append(i)

# Grabs the data of interest
sept_flows = [flow[j] for j in ilist3]
sept_day = [day[j] for j in ilist3]
# Plotting data for visual analysis
#plt.plot(sept_day,sept_flows)

#%% Pulling out data that had values greater than prediction from 1989 - 2020

ilist4 =[]
for i in range(len(flow)):
        if flow [i] > 62 and month[i] == 9 and year[i]<= 2000: # for the data before 2000 add year[i]<=2000
                ilist4.append(i)
# Shows how many times crieteria was met

print("Number of times flow was greater than prediction =",len(ilist4))
sept_flows_g = [flow[j] for j in ilist4]
# Exceedence 
print( "Percent times daily streamflow exceeded than prediction =",len(sept_flows_g)/len(sept_flows)*100)

# Calcualting mean percentage exceedence in flow
percent_incr = []
for i in range(0,len(sept_flows_g)):
        perc = (sept_flows_g[i]-62)/62*100
        percent_incr.append(perc)
print("Mean percent exceedence  = ",np.mean(percent_incr)) 
