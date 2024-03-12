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

combined_crashes['Date'] = pd.to_datetime(combined_crashes['Date'])

combined_crashes.to_csv('combined_crashes.csv', index=False)


