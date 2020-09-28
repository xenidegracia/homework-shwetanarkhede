# Example solution for HW 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('/Users/owner/Documents/GitHub/homework-shwetanarkhede/data/', filename)
print(os.getcwd())
print(filepath)

#filepath = '/Users/owner/Documents/GitHub/homework-shwetanarkhede/data/

# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %% Answers
df = pd.DataFrame(data)
Columns = df.columns
print('Names of columns = ',Columns.values)
print('Dataframe indices = ',df.index)
print('Type of data in each column = ',df.dtypes)
summary_flow = df[['flow']].describe()
print('Summary of flow properties = ', summary_flow)
print(summary_flow.to_markdown())

# Grouping data by month (Monthly flow)

monthly_flow_stats = df.groupby(['month'])[["flow"]].describe()
print('Monthly flow statistics = ',monthly_flow_stats)
print(monthly_flow_stats.to_markdown(tablefmt='grid'))

# 5 Highest and 5 lowest flow values for record
sorted_flow = df.sort_values(by="flow",ascending = False)

five_highest = sorted_flow.head()
five_highest_ans = five_highest[['datetime','month','flow']]
print('High Five = ',five_highest_ans)
print(five_highest_ans.to_markdown())

five_lowest = sorted_flow.tail()
five_lowest_ans = five_lowest[['datetime','month','flow']]
print('Low Five = ',five_lowest_ans)
print(five_lowest_ans.to_markdown())

# Highest and lowest for every month of the year


Monthly_flow_maxes = df.groupby(['month'])[['flow']].max()
Monthly_flow_mins = df.groupby(['month'])[["flow"]].min()

print(Monthly_flow_maxes.to_markdown())
print(Monthly_flow_mins.to_markdown())

# %% Flows within 10% of week 1 forecast in sept 
flows_within_windows = df[(df['flow']>=54.27 ) & (df['flow']<=66.3)& (df['month']==9)]
flow_win_sept = flows_within_windows[['datetime','flow']]
flow_win_sept.set_index('datetime', inplace=True)
print(flow_win_sept.to_markdown())

# %%
flow_win_sept.plot( y = 'flow')
