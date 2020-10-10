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
filename = 'streamflow_week7.txt'
filepath = os.path.join('/Users/owner/Documents/GitHub/\
homework-shwetanarkhede/Submissions/Code_Review1', filename)
print(os.getcwd())
print(filepath)


# %%
# Reading data to Panadas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime']
                     )

# Expanding the dates to year, month, day and day of week
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregating flow values to weekly (weekly averaged flow)
flow_weekly = data.resample("W", on='datetime').mean()

# Enabling datetime index to easily check the flow on specific date
# flow_weekly.reset_index(level=None,drop=False, \
# inplace=True, \col_level=0, col_fill='')

# %%
# Building an Autoregressive Model

# Step 1: Setting up the arrays based on lagged time series
flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)
flow_weekly['flow_tm3'] = flow_weekly['flow'].shift(3)
flow_weekly['flow_tm4'] = flow_weekly['flow'].shift(4)
flow_weekly['flow_tm5'] = flow_weekly['flow'].shift(5)
flow_weekly['flow_tm6'] = flow_weekly['flow'].shift(6)
flow_weekly['flow_tm7'] = flow_weekly['flow'].shift(7)
flow_weekly['flow_tm8'] = flow_weekly['flow'].shift(8)

# Step 2: Selecting data to use for prediction
# Using data from 2006 onwards
mydata = flow_weekly[
    (flow_weekly['year'] >= 2018) &
    (flow_weekly['month'] <= 10) &
    (flow_weekly['month'] >= 8)][['flow', 'flow_tm1', 'flow_tm2',
                                  'flow_tm3', 'flow_tm4', 'flow_tm5',
                                  'flow_tm6', 'flow_tm7', 'flow_tm8']]

# Seperating initial 80% data for training and rest 20% for testing
trainset = round(0.8*len(mydata))
train = mydata[0:trainset+1][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3',
                              'flow_tm4', 'flow_tm5', 'flow_tm6', 'flow_tm7',
                              'flow_tm8']]
test = mydata[trainset:][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3',
                          'flow_tm4', 'flow_tm5', 'flow_tm6', 'flow_tm7',
                          'flow_tm8']]

# Step 3: Fitting a linear regression model using sklearn
# For week 1 ahead forecast
model1 = LinearRegression()
x = train[['flow_tm1', 'flow_tm2', 'flow_tm3', 'flow_tm4',
           'flow_tm5', 'flow_tm6', 'flow_tm7', 'flow_tm8']].values
y = train[['flow']].values
model1.fit(x, y)

# Model Results
r_sq1 = model1.score(x, y)
print('Training: Coefficient of Determination = ', np.round(r_sq1, 2))
print('Training: Intercept = ', np.round(model1.intercept_, 2))
print('Training: Slope = ', np.round(model1.coef_[0], 2))

# Step 4: Making a prediction with model
# Predicting the model response for a  given flow value
q_pred_train = model1.predict(train[['flow_tm1', 'flow_tm2', 'flow_tm3',
                                     'flow_tm4', 'flow_tm5', 'flow_tm6',
                                     'flow_tm7', 'flow_tm8']].values)

# Alternatively, instead of using predict function, predictions can be made
# with the following equation
# q_pred = model.intercept_ + model.coef_ * train['flow_tm1']

# Training plot
fig, ax = plt.subplots()
ax.plot(train.index, train['flow'].values, label='Observed')
ax.plot(train.index, q_pred_train, label='Training')
ax.set(title="Model Training for week 1 Forecast", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]", yscale='log')
ax.legend()
fig.set_size_inches(5, 3)
fig.savefig("Model1 Training plot.png")  # Saving plot as .png image

# Testing Plot
q_pred_test = model1.predict(test[['flow_tm1', 'flow_tm2', 'flow_tm3',
                                   'flow_tm4', 'flow_tm5', 'flow_tm6',
                                   'flow_tm7', 'flow_tm8']].values)
fig, ax = plt.subplots()
ax.plot(test.index, test['flow'].values, label='Observed')
ax.plot(test.index, q_pred_test, label='Testing')
ax.set(title="Model Testing for week 1 Forecast", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]", yscale='log')
ax.legend()
fig.set_size_inches(5, 3)
fig.savefig("Model1 Testing plot.png")

# Predicting streamflow for week1
last_week_flow = mydata.tail(1)[['flow_tm1', 'flow_tm2', 'flow_tm3',
                                 'flow_tm4', 'flow_tm5', 'flow_tm6',
                                 'flow_tm7', 'flow_tm8']]
week1_prediction = model1.predict(last_week_flow.values)
print('Week 1 forecast = ', week1_prediction[0], 'cfs')

# Adding predicted flow to selected dataset
# newflowdata = np.append(mydata['flow'], week1_prediction)

# %%
# Model for week 2 forecast

# Need to use upto two time step lagged time series
# Using every second time series instead of making new dataset
model2 = LinearRegression()
x2 = train[['flow_tm2', 'flow_tm4', 'flow_tm6', 'flow_tm8']]
model2.fit(x2, y)
r_sq2 = model2.score(x2, y)
print('coefficient of determination:', np.round(r_sq2, 2))
print('intercept:', np.round(model2.intercept_, 2))
print('slope:', np.round(model2.coef_, 2))

last_week_flow1 = mydata.tail(1)[['flow_tm2', 'flow_tm4',
                                  'flow_tm6', 'flow_tm8']]

week2_prediction = model2.predict(last_week_flow1.values)
print('Week 2 forecast = ', week2_prediction[0], 'cfs')

# %%
# Extra informative plots

# Plotting selected data from entire dataset
# 1. Timeseries of observed flow values
fig, ax = plt.subplots()
ax.plot(flow_weekly['flow'], label='Full data')
ax.plot(mydata['flow'], 'r', label='Selected data')
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]", yscale='log')
ax.legend()
fig.set_size_inches(8, 3)
fig.savefig("Selected data.png")

# 2. Time series of flow values with the x axis range limited
fig, ax = plt.subplots()
ax.plot(mydata['flow'], label='full')
ax.plot(train['flow'], 'r:', label='training')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
       yscale='log', xlim=[datetime.date(2018, 8, 1),
                           datetime.date(2020, 10, 10)])
ax.legend()
fig.set_size_inches(8, 3)
fig.savefig("Zoomed training data.png")

# %% Printing required answers:

print('AR Model Week 1 forecast = ', week1_prediction[0], 'cfs')
print('AR Model Week 2 forecast = ', week2_prediction[0], 'cfs')
# Using AR Model results for competition
print('Week 1 forecast for competition = ', week1_prediction[0], 'cfs')
print('Week 2 forecast for competition = ', week2_prediction[0], 'cfs')
# %%
