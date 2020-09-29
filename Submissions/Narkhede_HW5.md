# Homework # 5 (Week 5)
## Name: Shweta Narkhede
#### Submission date: Sept, 27th, 2020
___
## Grade
3/3 - Great work!  I like your forecasting approach.  One note is that your image didn't render in your md within  atom. Next  time try the plugin I recommended and that should fix it. 
___

## **Assignment Questions**
___
1. **Provide a summary of the data frames properties**
- **What are the column names?**

  Column names are:  *agency_cd*, *site_no*, *datetime*, *flow*, *code*, *year*,*month*, *day*

- **What is its index?**

    Dataframe has row indices from 0 to 11592 with step 1.

- **What data types do each of the columns have?**



| Columns  | Data Type|
|:----:|:----:|
|agency_cd |    object|
|site_no   |     int64|
|datetime|      object|
|flow| float64|
|code|object|
|year|  int64|
|month|   int64|
|day   |  int64|



2. **Provide a summary of the flow column including the min, mean, max, standard deviation and quartiles.**



|Parameter| Flow (cfs)|
|:------:|:---------:|
| max | 63400    |
| mean  |   345.63 |
| std   |  1410.83 |
| min   |    19    |
| 25%   |    93.7  |
| 50%   |   158    |
| 75%   |   216    |



3. **Provide the same information but on a monthly basis. (Note: you should be able to do this with one or two lines of code)**



|   month |   ('flow', 'count') |   ('flow', 'mean') |   ('flow', 'std') |   ('flow', 'min') |   ('flow', '25%') |   ('flow', '50%') |   ('flow', '75%') |   ('flow', 'max') |
|:--------:|:--------------------:|:-------------------:|:------------------:|:------------------:|:------------------:|------------------:|------------------:|------------------:|
|       1 |                 992 |           706.321  |         2749.15   |             158   |           202     |            219.5  |            292    |             63400 |
|       2 |                 904 |           925.252  |         3348.82   |             136   |           201     |            244    |            631    |             61000 |
|       3 |                 992 |           941.732  |         1645.8    |              97   |           179     |            387.5  |           1060    |             30500 |
|       4 |                 960 |           301.24   |          548.141  |              64.9 |           112     |            142    |            214.5  |              4690 |
|       5 |                 992 |           105.442  |           50.7747 |              46   |            77.975 |             92.95 |            118    |               546 |
|       6 |                 960 |            65.999  |           28.9665 |              22.1 |            49.225 |             60.5  |             77    |               481 |
|       7 |                 992 |            95.5715 |           83.5123 |              19   |            53     |             70.9  |            110    |              1040 |
|       8 |                 992 |           164.354  |          274.464  |              29.6 |            76.075 |            114    |            170.25 |              5360 |
|       9 |                 956 |           172.689  |          286.776  |              36.6 |            88.075 |            120    |            171.25 |              5590 |
|      10 |                 961 |           146.169  |          111.779  |              69.9 |           107     |            125    |            153    |              1910 |
|      11 |                 930 |           205.105  |          235.674  |             117   |           156     |            175    |            199    |              4600 |
|      12 |                 961 |           337.098  |         1097.28   |             155   |           191     |            204    |            228    |             28700 |

___

4. **Provide a table with the 5 highest and 5 lowest flow values for the period of record. Include the date, month and flow values in your summary.**

Five highest flow values:

| Date   |   Month |   Flow (cfs) |
|:-----------:|:--------:|:-------:|
| 1993-01-08 |       1 |  63400 |
| 1993-02-20 |       2 |  61000 |
| 1995-02-15 |       2 |  45500 |
| 2005-02-12 |       2 |  35600 |
| 1995-03-06 |       3 |  30500 |

Five lowest flow values:
| Date   |   Month |   Flow (cfs)|
|:-----:|:-----------:|:--------:|
| 2012-07-03 |       7 |   23.4 |
| 2012-06-29 |       6 |   22.5 |
| 2012-06-30 |       6 |   22.1 |
| 2012-07-02 |       7 |   20.1 |
| 2012-07-01 |       7 |   19   |


5. **Find the highest and lowest flow values for every month of the year (i.e. you will find 12 maxes and 12 mins) and report back what year these occurred in.**

|   Month | Year|   Max flow (cfs) |
|:--------:|:---:|:-------:|
|       1 |1993|  63400 |
|       2 | 1993| 61000 |
|       3 | 1995 |30500 |
|       4 | 1991 | 4690 |
|       5 | 1992  | 546 |
|       6 | 1992   |481 |
|       7 | 2006  |1040 |
|       8 |  1992 |5360 |
|       9 |  2004 |5590 |
|      10 |  2010 |1910 |
|      11 | 2004  |4600 |
|      12 |  2004|28700 |


|   Month | Year |  Min flow (cfs)|
|:--------:|:----:|:-------:|
|       1 |2003 | 158   |
|       2 | 1991| 136   |
|       3 | 1989 | 97   |
|       4 | 2018  |64.9 |
|       5 | 2004  |46   |
|       6 | 2012  |22.1 |
|       7 |   2012|19   |
|       8 | 2019  |29.6 |
|       9 | 2020  |36.6 |
|      10 | 2012  |69.9 |
|      11 | 2016 |117   |
|      12 | 2012 |155   |


6. **Provide a list of historical dates with flows that are within 10% of your week 1 forecast value. If there are none than increase the %10 window until you have at least one other value and report the date and the new window you used.**

My week 1 forecast value is 60.3 cfs. The list of flows within 10% of 60.3 cfs for entire lebgth of records counts 603 times.Its a very long list to tabulate. Hence, I chose to seperate flows within 10% of 60.3 cfs occured only in the month of Sepetember historically.


| Date   |   Flow (cfs) |
|:-----------:|:-------:|
| 1989-09-08 |   66   |
| 2000-09-23 |   66   |
| 2000-09-24 |   64   |
| 2001-09-01 |   61   |
| 2002-09-06 |   58   |
| 2004-09-01 |   56.5 |
| 2004-09-02 |   56.2 |
| 2004-09-03 |   55.6 |
| 2004-09-04 |   59.6 |
| 2004-09-05 |   59.2 |
| 2004-09-06 |   61.6 |
| 2004-09-07 |   59.5 |
| 2004-09-08 |   64.7 |
| 2004-09-10 |   64   |
| 2004-09-11 |   56.3 |
| 2004-09-18 |   55.1 |
| 2009-09-01 |   62.8 |
| 2009-09-02 |   60.6 |
| 2009-09-03 |   60.5 |
| 2009-09-04 |   54.3 |
| 2009-09-05 |   56.6 |
| 2011-09-01 |   59.6 |
| 2011-09-02 |   59   |
| 2011-09-03 |   58.9 |
| 2011-09-04 |   58.9 |
| 2011-09-05 |   59.6 |
| 2011-09-06 |   62.6 |
| 2019-09-05 |   65.4 |
| 2019-09-06 |   61.5 |
| 2019-09-07 |   59   |
| 2019-09-08 |   61.7 |
| 2019-09-09 |   57.3 |
| 2019-09-10 |   59.1 |
| 2019-09-11 |   55.3 |
| 2019-09-12 |   56   |
| 2019-09-17 |   61.6 |
| 2019-09-18 |   62.9 |
| 2019-09-19 |   60.6 |
| 2019-09-20 |   57.1 |
| 2019-09-23 |   60.9 |
| 2020-09-01 |   65.3 |
| 2020-09-02 |   63.3 |
| 2020-09-03 |   60.6 |
| 2020-09-14 |   57.5 |
| 2020-09-15 |   58.2 |
| 2020-09-16 |   57.4 |
| 2020-09-17 |   57.3 |
| 2020-09-18 |   55.6 |
| 2020-09-21 |   55.9 |
| 2020-09-22 |   60   |
| 2020-09-23 |   64.5 |
| 2020-09-24 |   62.2 |
| 2020-09-25 |   58.1 |
| 2020-09-26 |   55.7 |

![image.png](/Users/owner/Documents/GitHub/homework-shwetanarkhede/Submissions/Plot1.png)




___
## **Forecast Summary**
___
- I tried to figure out the percentage change in mean weekly streamsflows from year to year and from week to week in same year. For the current forecast I preferred to stick to year 2019 and 2020 as trend in earlier years was quite fluctuating.
- I plotted the mean weekly flow in Sept and Oct for past 3 years to visualize the trend.
- The mean percenatge change in weekly flow was calculated for record of 2018 to 2020. The forecast for next few weeks was calculated based on mean percentage change in flow in 2018 and 2019.
