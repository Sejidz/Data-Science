"""Bokeh Visualization Template

This template is a general outline for turning your data into a
visualization using Bokeh.
"""
# Data handling
import pandas as pd  # noqa
import numpy as np  # noqa

# Bokeh libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show
#from bokeh.models import ColumnDataSource  # noqa
#from bokeh.layouts import row, column, gridplot  # noqa
#from bokeh.models import TabPanel  # noqa

# Prepare the datamode/
sales_06 = pd.read_csv(
    'assignment1 data/sales_202106.csv'
)
sales_07 = pd.read_csv(
    'assignment1 data/sales_202107.csv'
)
sales_08 = pd.read_csv(
    'assignment1 data/sales_202108.csv'
)
sales_09 = pd.read_csv(
    'assignment1 data/sales_202109.csv'
)
sales_10 = pd.read_csv(
    'assignment1 data/sales_202110.csv'
)
sales_11 = pd.read_csv(
    'assignment1 data/sales_202111.csv'
)
sales_12 = pd.read_csv(
    'assignment1 data/sales_202112.csv'
)
#print(sales_06.head())


x = [1, 2, 1]
y = [1, 1, 2]

# Determine where the visualization will be rendered
output_file("first_glyphs.html", title="First Glyphs")

# Set up the figure(s)
fig = figure(
    title="My Coordinates",
    height=300,
    width=300,
    x_range=(0, 3),
    y_range=(0, 3),
    toolbar_location=None,
)

# Connect to and draw the data
fig.circle(x=x, y=y, color="green", size=10, alpha=0.5)

# Organize the layout

# Preview and save
show(fig)  # See what I made, and save if I like it

