# Homework 4
# Shweta Narkhede
# Last edited on 09/19/2020

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week4.txt'
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

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Starter Code
## Answers to assignment questions
print("Dimension of flow_data = ",flow_data.ndim) # Gives dimension of array
print("Total size of flow_data = ",flow_data.size) # Gives size of array

# Count the number of values with flow > 48 and month ==9
flow_count = np.sum((flow_data[:,3] > 48) & (flow_data[:,1]==9))
print("Number of times daily flow was greater than prediction = ",flow_count)
flow_count_perc = np.round(flow_count/len(flow_data[:,1]==9)*100,2) # gives percentage value rounded to 2 decimal points
print(flow_count_perc,"% times daily flow was greater than prediction")

# Count the number of values with flow > 48 and month ==9 and year <= 2000
flow_count_b2000 = np.sum((flow_data[:,3] > 48) & (flow_data[:,1]==9) & (flow_data[:,0]<= 2000))
print("Number of times daily flow was greater than prediction in and before year 2000 = ",flow_count_b2000)
flow_count_perc_b2000 = np.round(flow_count_b2000/len(flow_data[:,1]==9)*100,2) # gives percentage value rounded to 2 decimal points
print(flow_count_perc_b2000,"% times daily flow was greater than prediction in and before year 2000 ")

# Count the number of values with flow > 48 and month ==9 and year >= 2010
flow_count_a2010 = np.sum((flow_data[:,3] > 48) & (flow_data[:,1]==9) & (flow_data[:,0]>= 2010))
print("Number of times daily flow was greater than prediction in and after year 2010 = ",flow_count_a2010)
flow_count_perc_a2010 = np.round(flow_count_a2010/len(flow_data[:,1]==9)*100,2) # gives percentage value rounded to 2 decimal points
print(flow_count_perc_a2010,"% times daily flow was greater than prediction in and after year 2010 ")

# %%

## Quantitative analysis

# Grabbing flow data in september for entire length of record
sept_flows = flow_data[(flow_data[:,1]==9),3]

# Piecing out mean flows for specific weeks in september
flow_sept_w = flow_data[(flow_data[:,1] ==9)  & (flow_data[:,2]>= 20) & \
(flow_data[:,2]<= 26),  3] 
#print('weekly mean =', np.mean(flow_sept_w))

# creating array for storing weekly means 
#allmeans = np.ones((1,len(flow_data[:,0])))

#creating bins for flow data between min an dmax of sept data spaced in 10 bins
#mybins = np.linspace(min(sept_flows),max(sept_flows),num=20)
#plt.hist(flow_sept_w, bins = mybins)

# by what percentage streamflow has been changed since past few years
# Year to year % flow change in this week

weeklymean1 = np.mean(flow_data[(flow_data[:,1] ==9)  & (flow_data[:,2]>= 20) & \
(flow_data[:,2]<= 26) & (flow_data[:,0] ==2018), 3])

weeklymean2 = np.mean(flow_data[(flow_data[:,1] ==9)  & (flow_data[:,2]>= 20) & \
(flow_data[:,2]<= 26) & (flow_data[:,0] ==2019), 3])
perc_change = (weeklymean2-weeklymean1)/weeklymean1*100
print('Mean changed by',round(perc_change,2),'% during 2018-2019')
print('Mean flow of next week (week1) = ',(weeklymean2*(1+perc_change/100)))

# %% Week 1 forecast
# but  trend in 2020 points towards value close to 70 cfs
weeklymean3 = np.mean(flow_data[(flow_data[:,1] ==9)  & (flow_data[:,2]>=6) & \
(flow_data[:,2]<= 12) & (flow_data[:,0] ==2020), 3])

weeklymean4 = np.mean(flow_data[(flow_data[:,1] ==9)  & (flow_data[:,2]>=13) & \
(flow_data[:,2]<= 19) & (flow_data[:,0] ==2020), 3])

print('Previous week mean flow =',round(weeklymean3,2),'cfs')
print('Current week mean flow =',round(weeklymean4,2),'cfs')

perc1 =((weeklymean4-weeklymean3)/weeklymean3)*100
print('Percentage change is',round(perc1,2),'%')
next_flow = weeklymean4*(1+perc1/100)
print('Week1 mean flow = ',round(next_flow,2),'cfs')

# %% Week 2 forecast
#Similar approach can be followed for forecasting flow after 2 weeks

print('Previous week mean flow =',round(weeklymean4,2),'cfs')
print('Current week mean flow =',round(next_flow,2),'cfs')

perc2 =(next_flow-weeklymean4)/weeklymean4*100
print('Percentage change is',round(perc2,2),'%')

print('Week2 mean flow = ',next_flow*(1+perc2/100),'cfs') 

#%%

# Visual analysis
# plotting histogram to see which value of forecatsed flow weights more
# creating 10 linearly spaced bins of flows from 40 cfs to 75 cfs
mybins1 = np.linspace(40, 75, num=10)

#Plotting the histogram
Hist_1 = plt.hist(sept_flows[(len(sept_flows)-149):len(sept_flows)], bins = mybins1)
plt.title('Count check for flows close to 40 cfs')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
# %%
mybins2 = np.linspace(70, 200, num=10)

#Plotting the histogram for last 5 years flows in sept
Hist_2 = plt.hist(sept_flows[(len(sept_flows)-149):len(sept_flows)], bins = mybins2)
plt.title('Count check for flows close to 70 cfs')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')


# Get the quantiles of flow

flow_quants1 = np.quantile(sept_flows, q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)

# %%

