# Autoregressive Model for forecasting weekly streamflow
# Modified by: Shweta Narkhede
# Last edited: Oct 5th, 2020

# %%
# Importing the modules
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime

# %%
# Accessing data
filename = 'streamflow_week6.txt'
filepath = os.path.join('/Users/owner/Documents/GitHub/homework-shwetanarkhede/data/', filename)
print(os.getcwd())
print(filepath)


# %%
# Reading data to Panadas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime']
        )

# Expanding the dates to year month day and day of week
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregating flow values to weekly (weekly averaged flow)
flow_weekly = data.resample("W", on='datetime').mean()

# Enabling datetime index to easily check date of flow
#flow_weekly.reset_index(level=None,drop=False, inplace=True, col_level=0, col_fill='')

# %% 
# Building an Autoregressive Model 

# Step 1: Setting up the arrays based on lagged time series

# For first two weeks forecast
flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)

# For later weeks' forecast (upto 8 weeks)
flow_weekly['flow_tm3'] = flow_weekly['flow'].shift(3)
flow_weekly['flow_tm4'] = flow_weekly['flow'].shift(4)
flow_weekly['flow_tm5'] = flow_weekly['flow'].shift(5)
flow_weekly['flow_tm6'] = flow_weekly['flow'].shift(6)
flow_weekly['flow_tm7'] = flow_weekly['flow'].shift(7)
flow_weekly['flow_tm8'] = flow_weekly['flow'].shift(8)

# Step 2 - Selecting data to use for prediction
# Using data from 2016 onwards
mydata = flow_weekly[(flow_weekly['year']>=2016 )][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3', 'flow_tm4', 'flow_tm5', 'flow_tm6', 'flow_tm7', 'flow_tm8']] #(flow_weekly['month']==9) & (flow_weekly['month']==10)]

# Seperating initial 80% data for training and rest 20% for testing
trainset = round(0.8*len(mydata))
train = mydata[0:trainset][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3', 'flow_tm4', 'flow_tm5', 'flow_tm6', 'flow_tm7', 'flow_tm8']]
test = mydata[trainset:][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3', 'flow_tm4', 'flow_tm5', 'flow_tm6', 'flow_tm7', 'flow_tm8']]

# Step 3: Fitting a linear regression model using sklearn 
# For week 1 forecast
model1 = LinearRegression()
x=train['flow_tm1'].values.reshape(-1,1)
y=train['flow'].values
model1.fit(x,y)

# Model1 Results 
# Model training r^2 values, intercept and the slope (rounded to two decimal places)
r_sq1 = model1.score(x, y)
print('Training: Coefficient of Determination:', np.round(r_sq1,2))
print('Training:Intercept:', np.round(model1.intercept_, 2))
print('Training:Slope:', np.round(model1.coef_[0], 2)) # indexing coef_ to print slope as a value instead of array

# Step 4: Making a prediction with model1 
# Predicting the model response for a  given flow value
q_pred_train = model1.predict(train['flow_tm1'].values.reshape(-1,1))

# Training plot
fig, ax = plt.subplots()
ax.plot(train.index,train['flow'].values, label='Observed')
ax.plot(train.index,q_pred_train,label='Training')
ax.set(title= "Model Training for week 1 Forecast", xlabel="Date", 
        ylabel="Weekly Avg Flow [cfs]",yscale = 'log')
ax.legend()
fig.set_size_inches(5,3)
fig.savefig("Model1 Training plot.png")
# Testing Plot
q_pred_test = model1.predict(test['flow_tm1'].values.reshape(-1,1))
fig, ax = plt.subplots()
ax.plot(test.index,test['flow'].values, label='Observed')
ax.plot(test.index,q_pred_test, label='Testing')
ax.set(title="Model Testing for week 1 Forecast", xlabel="Date", 
        ylabel="Weekly Avg Flow [cfs]",yscale = 'log')
ax.legend()
fig.set_size_inches(5,3)
fig.savefig("Model1 Testing plot.png")

#altrenatievely you can calcualte this yourself like this: 
#q_pred = model.intercept_ + model.coef_ * train['flow_tm1']

# Predicting streamflow for week1 
last_week_flow = mydata.flow[len(mydata)-1]
week1_prediction = model1.intercept_ + model1.coef_ * last_week_flow
print('Week 1 forecast = ',round((week1_prediction[0]),3),'cfs')

# %%
# Model for week 2 forecast

# Need to use upto two time step lagged time series (flow_tm2)
model2 = LinearRegression()
x2=train[['flow_tm1','flow_tm2']]
model2.fit(x2,y)
r_sq2 = model2.score(x2, y)
print('coefficient of determination:', np.round(r_sq2,2))
print('intercept:', np.round(model2.intercept_, 2))
print('slope:', np.round(model2.coef_, 2))

# Generating predictions
q_pred2_train = model2.predict(train[['flow_tm1', 'flow_tm2']])

# or by hand
#%q_pred2 = model2.intercept_   \
 #        + model2.coef_[0]* train['flow_tm1'] \
  #       +  model2.coef_[1]* train['flow_tm2'] 

# Training plot : Model 2
fig, ax = plt.subplots()
ax.plot(train.index,train['flow'].values, label='Observed')
ax.plot(train.index,q_pred2_train,label='Training')
ax.set(title= "Model Training for week 2 Forecast", xlabel="Date", 
        ylabel="Weekly Avg Flow [cfs]",yscale = 'log')
ax.legend()
fig.set_size_inches(5,3)
fig.savefig("Model2 Training plot.png")
# Testing Plot : Model 2
q_pred2_test = model2.predict(test[['flow_tm1', 'flow_tm2']])
fig, ax = plt.subplots()
ax.plot(test.index,test['flow'].values, label='Observed')
ax.plot(test.index,q_pred2_test, label='Testing')
ax.set(title="Model Testing for week 2 Forecast", xlabel="Date", 
        ylabel="Weekly Avg Flow [cfs]")
ax.legend()
fig.set_size_inches(5,3)
fig.savefig("Model2 Testing plot.png")
#%%
# Predicting streamflow for week2 
flow_before_2_weeks = mydata.flow[len(mydata)-1]
week2_prediction = model2.intercept_ + model2.coef_ * flow_before_2_weeks
print('Week 2 forecast = ',round((week2_prediction[0]),3),'cfs')

# %% 

fig, ax = plt.subplots()
ax.scatter(test['flow'].values,q_pred_test, marker='o',
              color='m',label = 'Model 1')

ax.scatter(test['flow'].values,q_pred2_test,marker='x',
              color='c',label = 'Model 2')

ax.set(title="Prediction for testing dataset", xlabel="Observed flow (cfs)", 
        ylabel="Predicted flow (cfs)" )
ax.set_xlim(0,np.max(test.flow))
ax.set_ylim(0,np.max(test.flow))
ax.legend()
fig.set_size_inches(5,5) 
fig.savefig("Testing Scatters.png")

# %%


# %%

# Extra informative plots

# Plotting selected data from entire dataset
# 1. Timeseries of observed flow values
fig, ax = plt.subplots()
ax.plot(flow_weekly['flow'], label='Full data')
ax.plot(mydata['flow'], 'r:', label='Selected data')
ax.set(title="Observed Flow", xlabel="Date", 
        ylabel="Weekly Avg Flow [cfs]")
ax.legend()
fig.set_size_inches(5,3)
fig.savefig("Selected data.png")

#2. Time series of flow values with the x axis range limited
# Just plotted in different scale on axis
fig, ax = plt.subplots()
ax.plot(mydata['flow'], label='full')
ax.plot(train['flow'], 'r:', label='training')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log', xlim=[datetime.date(2016, 1, 1), datetime.date(2020, 10, 1)])
ax.legend()
fig.set_size_inches(10,6)
fig.savefig("Zoomed training data.png")

#%% Week 3 Forecast model
model3 = LinearRegression()
x3=train[['flow_tm1','flow_tm2','flow_tm3']]
model3.fit(x3,y)
r_sq3 = model3.score(x3, y)
# Generating predictions
q_pred3_train = model3.predict(train[['flow_tm1', 'flow_tm2','flow_tm3']])
q_pred3_test = model3.predict(test[['flow_tm1', 'flow_tm2','flow_tm3']])
# Predicting streamflow for week3 
flow_before_3_weeks = mydata.flow[len(mydata)-1]
week3_prediction = model3.intercept_ + model3.coef_ * flow_before_3_weeks
print('Week 3 forecast = ',round((week3_prediction[0]),3),'cfs')

# %%
fig, ax = plt.subplots()
ax.plot(train.index,train['flow'].values,'r',label='Training data')
ax.plot(test.index,test['flow'].values,'g',label='Testing data')
ax.set(title= " Data used for Models", xlabel="Date", 
        ylabel="Weekly Avg Flow [cfs]",yscale = 'log')
ax.legend()
fig.set_size_inches(5,3)
fig.savefig("Training-testing data.png")