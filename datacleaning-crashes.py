import pandas as pd  # noqa
import numpy as np  # noqa



# Prepare the datamode/
crashes_06 = pd.read_csv(
    'assignment1 data/stats_crashes_202106_overview.csv', encoding='utf-16-le'
)
crashes_07 = pd.read_csv(
    'assignment1 data/stats_crashes_202107_overview.csv', encoding='utf-16-le'
)
crashes_08 = pd.read_csv(
    'assignment1 data/stats_crashes_202108_overview.csv', encoding='utf-16-le'
)
crashes_09 = pd.read_csv(
    'assignment1 data/stats_crashes_202109_overview.csv', encoding='utf-16-le'
)
crashes_10 = pd.read_csv(
    'assignment1 data/stats_crashes_202110_overview.csv', encoding='utf-16-le'
)
crashes_11 = pd.read_csv(
    'assignment1 data/stats_crashes_202111_overview.csv', encoding='utf-16-le'
)
crashes_12 = pd.read_csv(
    'assignment1 data/stats_crashes_202112_overview.csv', encoding='utf-16-le'
)
# Combine the data into a single DataFrame
combined_crashes = pd.concat([crashes_06, crashes_07, crashes_08, crashes_09, crashes_10, crashes_11, crashes_12])


#keep only the columns date and Daily Crashes
combined_crashes = combined_crashes[['Date', 'Daily Crashes']]

# Sum um the crashed per month
crashes_per_month = combined_crashes.groupby(combined_crashes['Date'].str[:7]).sum()

# Prepare the datamode
ratings_per_month = pd.read_csv(
    'ratings_per_month.csv'
)

crashes_per_month['Daily Crashes Divided'] = 0
#Divide the values by the corresponding values in ratings_per_month by a for loop iloc
for i in range(0, len(ratings_per_month)):
    crashes_per_month['Daily Crashes Divided'].iloc[i] = crashes_per_month['Daily Crashes'].iloc[i] / ratings_per_month['Daily Average Rating'].iloc[i]

#Change the date column to only show the month
crashes_per_month['Date'] = crashes_per_month.index

crashes_per_month.to_csv('crashes_per_month.csv', index=False)


