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
from bokeh.palettes import Category10
from bokeh.models import ColumnDataSource
df = pd.read_csv("combined_sales_last.csv")

# Data preprocessing
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
df['Day of Week'] = df['Transaction Date'].dt.day_name()

# Segmentation by SKU ID
# Remove non-numeric characters and convert 'Amount (Buyer Currency)' to numeric

# Group by 'Sku Id' and sum 'Amount (Buyer Currency)' for each group
sku_sales = df.groupby('Sku Id')['Amount (Merchant Currency)'].sum()

print(sku_sales)
# Visualization
output_file("sales_volume_by_sku_id.html")

p = figure(x_range=sku_sales.index.tolist(), height=350, title="Sales Volume by SKU ID",
           toolbar_location=None, tools="")

p.vbar(x=sku_sales.index.tolist(), top=sku_sales.values, width=0.9, line_color="white")

p.xgrid.grid_line_color = None
p.y_range.start = 0
p.xaxis.major_label_orientation = "vertical"
p.xaxis.axis_label = "SKU ID"
p.yaxis.axis_label = "Sales Volume (In Euro's)"

show(p)

