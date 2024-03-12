import pandas as pd  # noqa
import numpy as np  # noqa

# Prepare the datamode/
ratings_06 = pd.read_csv(
    'assignment1 data/stats_ratings_202106_overview.csv', encoding='utf-16-le'
)
ratings_07 = pd.read_csv(
    'assignment1 data/stats_ratings_202107_overview.csv', encoding='utf-16-le'
)
ratings_08 = pd.read_csv(
    'assignment1 data/stats_ratings_202108_overview.csv', encoding='utf-16-le'
)
ratings_09 = pd.read_csv(
    'assignment1 data/stats_ratings_202109_overview.csv', encoding='utf-16-le'
)
ratings_10 = pd.read_csv(
    'assignment1 data/stats_ratings_202110_overview.csv', encoding='utf-16-le'
)
ratings_11 = pd.read_csv(
    'assignment1 data/stats_ratings_202111_overview.csv', encoding='utf-16-le'
)
ratings_12 = pd.read_csv(
    'assignment1 data/stats_ratings_202112_overview.csv', encoding='utf-16-le'
)

# Combine the data into a single DataFrame
combined_ratings = pd.concat([ratings_06, ratings_07, ratings_08, ratings_09, ratings_10, ratings_11, ratings_12])

combined_ratings['Date'] = pd.to_datetime(combined_ratings['Date'])

#combined_ratings = combined_ratings.dropna(subset=['Daily Average Rating'])

combined_ratings.to_csv('combined_ratings.csv', index=False)



