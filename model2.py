import pandas as pd
import geopandas as gpd
from bokeh.plotting import figure, show
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar
from bokeh.palettes import Viridis256
from bokeh.layouts import column
from bokeh.models import Slider

# Read the provided data into a DataFrame
df = pd.read_csv("finalcombinedsales.csv")

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

# Define callback function for slider
def update_plot(attr, old, new):
    selected_month = months[new]
    updated_data = df[df['Month'] == selected_month]
    sales_volume_by_country = updated_data.groupby('Buyer Country')['Amount (Merchant Currency)'].sum().reset_index()
    updated_world = world.merge(sales_volume_by_country, how='left', left_on='name', right_on='Buyer Country')
    updated_world['Amount (Merchant Currency)'] = updated_world['Amount (Merchant Currency)'].fillna(0)  # Fill missing values with 0
    geo_source.geojson = updated_world.to_json()
    color_mapper.low = updated_world['Amount (Merchant Currency)'].min()
    color_mapper.high = updated_world['Amount (Merchant Currency)'].max()

# Convert 'Transaction Date' column to datetime
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

# Extract month from 'Transaction Date'
df['Month'] = df['Transaction Date'].dt.month

months = sorted(df['Month'].unique())
slider = Slider(start=0, end=len(months) - 1, value=0, step=1, title="Month")
slider.on_change('value', update_plot)

layout = column(r, slider)
show(layout)
