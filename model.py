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
from bokeh.models import ColumnDataSource, Dropdown, CustomJS
from bokeh.layouts import row, column
df = pd.read_csv("finalcombinedsales.csv")

# Data preprocessing
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
df['Day of Week'] = df['Transaction Date'].dt.day_name()
# Segmentation by SKU ID
# Group by 'Sku Id' and sum 'Amount (Merchant Currency)' for each group
sku_sales = df.groupby('Sku Id')['Amount (Merchant Currency)'].sum()
dayoftheweek_sales = df.groupby('Day of Week')['Amount (Merchant Currency)'].sum()
dayoftheweek_sales = dayoftheweek_sales.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
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

b = figure(x_range=dayoftheweek_sales.index.tolist(), height=350, title="Sales Volume by Day of the Week",
           toolbar_location=None, tools="")
b.vbar(x=dayoftheweek_sales.index.tolist(), top=dayoftheweek_sales.values, width=0.9, line_color="white")
b.xgrid.grid_line_color = None
b.y_range.start = 0
b.xaxis.axis_label = "Day of the Week"
b.yaxis.axis_label = "Sales Volume (In Euro's)"


df['Day'] = df['Transaction Date'].dt.day
df['Month'] = df['Transaction Date'].dt.month

# Aggregate sales volume and count of transactions per day and month
daily_sales = df.groupby('Day')['Amount (Merchant Currency)'].sum()
monthly_sales = df.groupby('Month')['Amount (Merchant Currency)'].sum()
daily_transactions = df.groupby('Day').size()
monthly_transactions = df.groupby('Month').size()

# Create plots
p_daily_sales = figure(title="Daily Sales Volume", x_axis_label="Day", y_axis_label="Sales Volume (Merchant Currency)")
p_daily_sales.line(daily_sales.index, daily_sales.values, line_width=2)

p_monthly_sales = figure(title="Monthly Sales Volume", x_axis_label="Month", y_axis_label="Sales Volume (Merchant Currency)")
p_monthly_sales.line(monthly_sales.index, monthly_sales.values, line_width=2)

p_daily_transactions = figure(title="Daily Transactions", x_axis_label="Day", y_axis_label="Number of Transactions")
p_daily_transactions.line(daily_transactions.index, daily_transactions.values, line_width=2)

p_monthly_transactions = figure(title="Monthly Transactions", x_axis_label="Month", y_axis_label="Number of Transactions")
p_monthly_transactions.line(monthly_transactions.index, monthly_transactions.values, line_width=2)


layout = column(b,p, p_daily_sales, p_monthly_sales, p_daily_transactions, p_monthly_transactions)
show(layout)

