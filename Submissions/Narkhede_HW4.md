# Homework # 4 (Week 4)
## Name: Shweta Narkhede
#### Submission date: Sept, 14th, 2020
___
### Grade
3/3 - nice job! next time try including images in your markdown file. Instructions for that will be included in the next assignment.  
___

## **Assignment Questions**

1. **Include discussion of the quantitative analysis that lead to your prediction. This can include any analysis you complete but must include at least two histograms and some quantitative discussion of flow quantiles that helped you make your decision.**

- The percentage change in mean weekly flow was calculated for various year to check if that fits the trend for known data. Since the trend seem to be fitting for year 2015 to 2019, weekly mean percentage change in streamflow was used to predict streamflow in 2020.
- Mean weekly percentage change in flow was calculated for year-to-year change for same days in sepetmeber as well as week-to-week change in same year. Both approcahes gave different values for nect week forecast (aprox 41 cfs and 74 cfs).
- Histograms were plotted to check how many times flow in September for entire record length falls in the bin containing 40 cfs and same is doen for the bin of 75 cfs.
- 75 cfs gave higher count of times when flow in september was around 75 cfs. Thus, the approach of week-to-week percetage change is followed for rest of the predictions.


2. **Describe the variable flow_data:**

- **What is it?**

    Flow_data is an numpy array.

- **What type of values it is composed of?**
    It is composed of the values of "year", "month", "day" and "flow" respectively of the entire data record.

- **What is are its dimensions, and total size?**
The dimension of array flow_data is 2 and its total size is 46340.

3. **How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?**
Number of times daily flow was greater than prediction(48 cfs) = 942 and it was true for 8.13% of the times.

4. **How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)**
Number of times daily flow was greater than prediction(48 cfs) in and before year 2000 = 360 and it was true for 3.11% of the times.
Number of times daily flow was greater than prediction(48 cfs) in and after year 2010 = 312 and it was true for 2.69% of the times.

**Summary Table**
| Record length| Number of times flow exceeds prediction| Percentage of times flow exceeds prediction|
| :-----: | :-----: | :----: |
|  1989-2020 | 942  | 8.16    |
| 1989-2000   | 311| 3.11 |
| 2010-2020   | 311| 2.76 |


5. **How does the daily flow generally change from the first half of September to the second?**
Daily flow for earlier few years seems to have a first peak flow after a first quarter of September and then reduce and again shows second peak in second half of september in 3rd quarter. For few years in records from 1989-2020 this trend is not true. But mostly, we can expect to have higher streamflow in first half of sept than in second half.
___

## **Forecast Summary**
- I tried to figure out the percentage change in mean weekly streamsflows from year to year and from week to week in same year. For the current forecast I preferred to stick to year 2019 and 2020 as trend in earlier years was quite fluctuating.
- The percentage change in mean flow of last week and current week is used to predict flow in next week in year 2020.
- When this same approach is followed for year-year weekly change, the predcition is as low as 41.33 cfs while for same year, week-to-week approach next week's mean flow is predicted as 74.74 cfs.
- Histogram are plotted to check how many times the flows in the septenber falls close to 40 cfs and 74 cfs.
- 74 cfs seems to win the game! But intuitively we should expect low streamflows in the next week. I prefer to stick to predictions by numerical analysis.
