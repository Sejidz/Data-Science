import pandas as pd  # noqa
import numpy as np  # noqa

# Prepare the datamode/
ratings_06 = pd.read_csv(
    'assignment1 data/stats_ratings_202106_overview.csv', encoding='utf-16-le'
)
average_06 = 0
for index, value in ratings_06['Daily Average Rating'].items():
    if not pd.isna(value):
        average_06 +=1


ratings_07 = pd.read_csv(
    'assignment1 data/stats_ratings_202107_overview.csv', encoding='utf-16-le'
)
average_07 = 0
for index, value in ratings_07['Daily Average Rating'].items():
    if not pd.isna(value):
        average_07 +=1


ratings_08 = pd.read_csv(
    'assignment1 data/stats_ratings_202108_overview.csv', encoding='utf-16-le'
)
average_08 = 0
for index, value in ratings_08['Daily Average Rating'].items():
    if not pd.isna(value):
        average_08 +=1


ratings_09 = pd.read_csv(
    'assignment1 data/stats_ratings_202109_overview.csv', encoding='utf-16-le'
)
average_09 = 0
for index, value in ratings_09['Daily Average Rating'].items():
    if not pd.isna(value):
        average_09 +=1


ratings_10 = pd.read_csv(
    'assignment1 data/stats_ratings_202110_overview.csv', encoding='utf-16-le'
)
average_10 = 0
for index, value in ratings_10['Daily Average Rating'].items():
    if not pd.isna(value):
        average_10 +=1


ratings_11 = pd.read_csv(
    'assignment1 data/stats_ratings_202111_overview.csv', encoding='utf-16-le'
)
average_11 = 0
for index, value in ratings_11['Daily Average Rating'].items():
    if not pd.isna(value):
        average_11 +=1


ratings_12 = pd.read_csv(
    'assignment1 data/stats_ratings_202112_overview.csv', encoding='utf-16-le'
)
average_12 = 0
for index, value in ratings_12['Daily Average Rating'].items():
    if not pd.isna(value):
        average_12 +=1

# Combine the data into a single DataFrame
combined_ratings = pd.concat([ratings_06, ratings_07, ratings_08, ratings_09, ratings_10, ratings_11, ratings_12])

#keep only the columns date and Daily Average Rating
combined_ratings = combined_ratings[['Date', 'Daily Average Rating']]

# Sum um the ratings per month
ratings_per_month = combined_ratings.groupby(combined_ratings['Date'].str[:7]).sum()

#Take the mean of the values per month
ratings_per_month['Daily Average Rating'] = ratings_per_month['Daily Average Rating'] / [average_06, average_07, average_08, average_09, average_10, average_11, average_12]

#Change the date column to only show the month
ratings_per_month['Date'] = ratings_per_month.index

ratings_per_month.to_csv('ratings_per_month.csv', index=False)




