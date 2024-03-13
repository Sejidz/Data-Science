# Data handling
import pandas as pd  # noqa
import numpy as np  # noqa

# Bokeh libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.palettes import Category10
from bokeh.models import ColumnDataSource, Dropdown, CustomJS
from bokeh.layouts import row, column
from bokeh.models import DatetimeTickFormatter

output_file('crashes-ratings.html', 
            title='Crashes and Ratings per Month')

fig = figure(x_axis_type='datetime',
             height=300, width=600,
             title='Crashes and Ratings per Month',
             x_axis_label='Date', y_axis_label='Number of Crashes and Ratings', 
             toolbar_location=None)





# Load the data
crashes_per_month = pd.read_csv('crashes_per_month.csv')
ratings_per_month = pd.read_csv('ratings_per_month.csv')

crashes_per_month['Date'] = pd.to_datetime(crashes_per_month['Date'])
ratings_per_month['Date'] = pd.to_datetime(ratings_per_month['Date'])


# Add data to the figure
#fig.line(crashes_per_month['Date'], crashes_per_month['Daily Crashes'], 
         #legend_label='Crashes',
         #line_width=2,
         #color ='#CE1141')

fig.line(ratings_per_month['Date'], ratings_per_month['Daily Average Rating'],
         legend_label='Ratings' ,
         line_width=2, 
         color='#007A33')

# Customize the x-axis
fig.xaxis.formatter = DatetimeTickFormatter(months=["%b"])


# Move the legend to the upper left corner
fig.legend.location = 'top_left'

show(fig)
