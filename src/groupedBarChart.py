from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.transform import dodge
from bokeh.models import ColumnDataSource
import pandas as pd

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Group1': [10, 15, 7, 12],
    'Group2': [8, 10, 5, 9]
}

# Convert data to a Pandas DataFrame
df = pd.DataFrame(data)

# Create a Bokeh ColumnDataSource
source = ColumnDataSource(df)

# Create the figure
p = figure(x_range=df['Category'], height=250, title="Grouped Bar Chart")

# Define width and offsets for bars in each group
bar_width = 0.3
offset = bar_width / 2

# Create grouped bars
p.vbar(x=dodge('Category', -offset, range=p.x_range), top='Group1', width=bar_width, source=source,
       color="blue", legend_label="Group 1")

p.vbar(x=dodge('Category', offset, range=p.x_range), top='Group2', width=bar_width, source=source,
       color="orange", legend_label="Group 2")

# Customize the plot
p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

# Show the plot
output_file("grouped_bar_chart.html")
show(p)
