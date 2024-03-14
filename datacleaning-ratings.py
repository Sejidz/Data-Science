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


# Prepare the datamode/
ratings_country_06 = pd.read_csv(
    'assignment1 data/stats_ratings_202106_country.csv', encoding='utf-16-le'
)


ratings_country_06['Date'] = pd.to_datetime(ratings_country_06['Date'])
ratings_country_06 = ratings_country_06.groupby('Country').resample('ME', on='Date')['Total Average Rating'].mean().reset_index()


ratings_country_07 = pd.read_csv(
    'assignment1 data/stats_ratings_202107_country.csv', encoding='utf-16-le'
)
ratings_country_07['Date'] = pd.to_datetime(ratings_country_07['Date'])
ratings_country_07 = ratings_country_07.groupby('Country').resample('ME', on='Date')['Total Average Rating'].mean().reset_index()


ratings_country_08 = pd.read_csv(
    'assignment1 data/stats_ratings_202108_country.csv', encoding='utf-16-le'
)
ratings_country_08['Date'] = pd.to_datetime(ratings_country_08['Date'])
ratings_country_08 = ratings_country_08.groupby('Country').resample('ME', on='Date')['Total Average Rating'].mean().reset_index()

ratings_country_09 = pd.read_csv(
    'assignment1 data/stats_ratings_202109_country.csv', encoding='utf-16-le'
)
ratings_country_09['Date'] = pd.to_datetime(ratings_country_09['Date'])
ratings_country_09 = ratings_country_09.groupby('Country').resample('ME', on='Date')['Total Average Rating'].mean().reset_index()

ratings_country_10 = pd.read_csv(
    'assignment1 data/stats_ratings_202110_country.csv', encoding='utf-16-le'
)
ratings_country_10['Date'] = pd.to_datetime(ratings_country_10['Date'])
ratings_country_10 = ratings_country_10.groupby('Country').resample('ME', on='Date')['Total Average Rating'].mean().reset_index()

ratings_country_11 = pd.read_csv(
    'assignment1 data/stats_ratings_202111_country.csv', encoding='utf-16-le'
)
ratings_country_11['Date'] = pd.to_datetime(ratings_country_11['Date'])
ratings_country_11 = ratings_country_11.groupby('Country').resample('ME', on='Date')['Total Average Rating'].mean().reset_index()

ratings_country_12 = pd.read_csv(
    'assignment1 data/stats_ratings_202112_country.csv', encoding='utf-16-le'
)
ratings_country_12['Date'] = pd.to_datetime(ratings_country_12['Date'])
ratings_country_12 = ratings_country_12.groupby('Country').resample('ME', on='Date')['Total Average Rating'].mean().reset_index()

# Combine the data into a single DataFrame
combined_ratings_country = pd.concat([ratings_country_06, ratings_country_07, ratings_country_08, ratings_country_09, ratings_country_10, ratings_country_11, ratings_country_12])

#keep only the columns date and Daily Average Rating
combined_ratings_country = combined_ratings_country[['Date','Country', 'Total Average Rating']]

combined_ratings_country['Date'] = combined_ratings_country['Date'].dt.strftime('%m')

#Multiple the ratings by a number to make the plot more readable
combined_ratings_country['Total Average Rating'] = combined_ratings_country['Total Average Rating']



#If the values in the beginning and at the end for a country is same then remove
#the country from the dataframe
for country in combined_ratings_country['Country'].unique():
    country_data = combined_ratings_country[combined_ratings_country['Country'] == country]
    if country_data['Total Average Rating'].iloc[0] == country_data['Total Average Rating'].iloc[-1]:
        combined_ratings_country = combined_ratings_country[combined_ratings_country['Country'] != country]

combined_ratings_country.to_csv('ratings_per_country.csv', index=False)









