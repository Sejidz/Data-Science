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
from bokeh.io import output_notebook
from bokeh.models.layouts import TabPanel, Tabs
from bokeh.models import ColumnDataSource, Dropdown, CustomJS
from bokeh.layouts import row, column
from bokeh.models import DatetimeTickFormatter
import geopandas as gpd
from shapely.geometry import Point
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar
from bokeh.palettes import Viridis256
import geopandas as gpd
import json
import matplotlib as mpl
import pylab as plt
from bokeh.io import output_file, show, output_notebook, export_png
from bokeh.models import ColumnDataSource, GeoJSONDataSource, LinearColorMapper, ColorBar, Dropdown, CustomJS, DatetimeTickFormatter, Legend
from bokeh.plotting import figure, show
from bokeh.palettes import Category10, brewer
import panel as pn
import panel.widgets as pnw

# Read the provided data into a DataFrame
df = pd.read_csv("finalcombinedsales.csv")
crashes_per_month = pd.read_csv('crashes_per_month.csv')
ratings_per_month = pd.read_csv('ratings_per_month.csv')



# Data preprocessing
crashes_per_month['Date'] = pd.to_datetime(crashes_per_month['Date'])
ratings_per_month['Date'] = pd.to_datetime(ratings_per_month['Date'])
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
df['Day of Week'] = df['Transaction Date'].dt.day_name()
# Segmentation by SKU ID
# Group by 'Sku Id' and sum 'Amount (Merchant Currency)' for each group
sku_sales = df.groupby('Sku Id')['Amount (Merchant Currency)'].sum()
dayoftheweek_sales = df.groupby('Day of Week')['Amount (Merchant Currency)'].sum()
dayoftheweek_sales = dayoftheweek_sales.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
# Visualization
output_file("visualisation.html")

# Aggregate sales volume by country
country_mapping = {
    'US': 'United States of America',
    'GB': 'United Kingdom',
    'CA': 'Canada',
    'DE': 'Germany',
    'NL': 'Netherlands',
    'AU': 'Australia',
    'IT': 'Italy',
    'SE': 'Sweden',
    'MX': 'Mexico',
    'GR': 'Greece',
    'BR': 'Brazil',
    'RU': 'Russia',
    'CZ': 'Czech Republic',
    'PL': 'Poland',
    'BE': 'Belgium',
    'DK': 'Denmark',
    'UA': 'Ukraine',
    'FR': 'France',
    'CH': 'Switzerland',
    'PH': 'Philippines',
    'ES': 'Spain',
    'AT': 'Austria',
    'ID': 'Indonesia',
    'ZA': 'South Africa',
    'IE': 'Ireland',
    'PR': 'Puerto Rico',
    'LT': 'Lithuania',
    'TR': 'Turkey',
    'MY': 'Malaysia',
    'PT': 'Portugal',
    'IL': 'Israel',
    'NO': 'Norway',
    'BG': 'Bulgaria',
    'FI': 'Finland',
    'AR': 'Argentina'
    # Add more mappings as needed
}

# Convert country codes to full names in sales volume data
df['Buyer Country'] = df['Buyer Country'].map(country_mapping)
sales_volume_by_country = df.groupby('Buyer Country')['Amount (Merchant Currency)'].sum().reset_index()
print(sales_volume_by_country)
# Read the GeoDataFrame containing country geometries
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge sales volume data with country geometries
world = world.merge(sales_volume_by_country, how='left', left_on='name', right_on='Buyer Country')

# Convert GeoDataFrame to GeoJSONDataSource
geo_source = GeoJSONDataSource(geojson=world.to_json())

# Create color mapper
color_mapper = LinearColorMapper(palette=Viridis256, low=world['Amount (Merchant Currency)'].min(), high=world['Amount (Merchant Currency)'].max())

# Create Bokeh plot
r = figure(title="Sales Volume Heatmap by Country", height=600, width=1000)
r.toolbar_location = None
r.xgrid.grid_line_color = None
r.ygrid.grid_line_color = None

# Add country polygons
r.patches('xs', 'ys', source=geo_source, fill_color={'field': 'Amount (Merchant Currency)', 'transform': color_mapper},
          line_color='black', line_width=0.5, fill_alpha=0.7)

# Add color bar
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=12, location=(0, 0))
r.add_layout(color_bar, 'right')


fig = figure(x_axis_type='datetime',
             height=300, width=600,
             title='Crashes and Ratings per Month',
             x_axis_label='Date', y_axis_label='Number of Crashes and Ratings', 
             toolbar_location=None)

# Add data to the figure
fig.line(crashes_per_month['Date'], crashes_per_month['Daily Crashes'], 
         legend_label='Crashes',
         line_width=2,
         color ='#CE1141')

fig.line(crashes_per_month['Date'], crashes_per_month['Daily Crashes Divided'],
         legend_label='Daily Crashes Divided by Daily Average Rating' ,
         line_width=2, 
         color='#007A33')

fig.line(ratings_per_month['Date'], ratings_per_month['Daily Average Rating'] * 100,
         legend_label='Daily Average Rating per Month times 100',
         line_width=2, 
         color='#0057e7')

# Customize the x-axis
fig.xaxis.formatter = DatetimeTickFormatter(months=["%b"])

# Move the legend to the upper left corner
fig.legend.location = 'top_left'


p = figure(x_range=sku_sales.index.tolist(), height=350, title="Sales Volume by SKU ID",
           toolbar_location=None, tools="")
p.vbar(x=sku_sales.index.tolist(), top=sku_sales.values, width=0.9, line_color="white")
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.xaxis.major_label_orientation = "vertical"
p.xaxis.axis_label = "Storage Keeping Index ID"
p.yaxis.axis_label = "Sales Volume (In Euro's)"

b = figure(x_range=dayoftheweek_sales.index.tolist(), height=350, title="Sales Volume by Day of the Week",
           toolbar_location=None, tools="")
b.vbar(x=dayoftheweek_sales.index.tolist(), top=dayoftheweek_sales.values, width=0.9, line_color="white")
b.xgrid.grid_line_color = None
b.y_range.start = 0
b.xaxis.axis_label = "Day of the Week"
b.yaxis.axis_label = "Sales Volume (In Euro's)"



# Output to file

# Increase the plot widths

# Create two panels, one for each conference
skupanel = TabPanel(child=p, title='Sales Volume by SKU ID')
daypanel = TabPanel(child=b, title='Sales Volume by day of the week')

# Assign the panels to Tabs
tabs = Tabs(tabs=[skupanel, daypanel])

# Show the tabbed layout

df['Day'] = df['Transaction Date'].dt.day
df['Month'] = df['Transaction Date'].dt.month

# Aggregate sales volume and count of transactions per day and month
daily_sales = df.groupby('Day')['Amount (Merchant Currency)'].sum()
monthly_sales = df.groupby('Month')['Amount (Merchant Currency)'].sum()
daily_transactions = df.groupby('Day').size()
monthly_transactions = df.groupby('Month').size()

# Create plots
p_daily_sales = figure(title="Daily Sales Volume", x_axis_label="Day", y_axis_label="Sales Volume (In Euro's)")
p_daily_sales.line(daily_sales.index, daily_sales.values, line_width=2)

p_monthly_sales = figure(title="Monthly Sales Volume", x_axis_label="Month", y_axis_label="Sales Volume (In Euro's)")
p_monthly_sales.line(monthly_sales.index, monthly_sales.values, line_width=2)

p_daily_transactions = figure(title="Transactions per day", x_axis_label="Day", y_axis_label="Number of Transactions on that day of each month")
p_daily_transactions.line(daily_transactions.index, daily_transactions.values, line_width=2)

p_monthly_transactions = figure(title="Transactions per month", x_axis_label="Month", y_axis_label="Number of Transactions in that month")
p_monthly_transactions.line(monthly_transactions.index, monthly_transactions.values, line_width=2)

panel1 = TabPanel(child=p_daily_transactions, title='Transactions per day')
panel2 = TabPanel(child=p_monthly_transactions, title='Transactions per month')
panel3 = TabPanel(child=p_daily_sales, title='Sales Volume per day')  
panel4 = TabPanel(child=p_monthly_sales, title='Sales Volume per month')
# Assign the panels to Tabs
tabs2 = Tabs(tabs=[panel1, panel2, panel3, panel4])



ratings_per_country = pd.read_csv('ratings_per_country.csv')

colors = Category10[10] * (len(ratings_per_country['Country'].unique()) // len(Category10[10]) + 1)
fig2 = figure(
    title='Ratings per country over time',
    height=300,
    width=600,
    toolbar_location='below',
    tools='pan, wheel_zoom, box_zoom, reset',
    x_axis_label='Date', y_axis_label='Average Rating per month'
)

teller = 0
items = []
# Add the data to the figure where every country has its own line in the plot
#The x-axis is the date and the y-axis is the daily average rating
for country in ratings_per_country['Country'].unique():
    teller += 1
    country_data = ratings_per_country[ratings_per_country['Country'] == country]

    line = fig2.line(country_data['Date'], country_data['Total Average Rating'], 
             line_width=2,
             color=colors[teller])
    items.append((country, [line]))

legend = Legend(items=items,
location=(0, -30))
fig2.add_layout(legend, 'right')

fig2.legend.click_policy="hide"
fig2.legend.label_text_font_size = '10pt'

layout = column(tabs2, tabs)
#add a row to the layout as fig
layout2 = column(fig, r)
layout = row(layout, layout2, fig2)

show(layout)

# Data handling


    
    

