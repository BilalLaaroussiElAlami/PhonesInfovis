import pandas as pd
from bokeh.io import show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure

# p = figure(title="Multiple glyphs example", x_axis_label="x", y_axis_label="y")
# x = [1, 2, 3]
# y = [3,2,1]
# p.circle(x, y, legend_label="Objects", color="blue", size=12)
# show(p)


# maka a dataframe from the csv file
df = pd.read_csv('project/smartphones.csv')
# print the brands of the phones
print(df['brand_name'].unique())


# make a graph where the x-axis is the battery_capacity and the y-axis is the price, plot the phone models as circles, when the user hovers over a circle
# more information is shown about the phone model:
#p = figure(title="Battery capacity vs price", x_axis_label="Battery capacity", y_axis_label="Price")
#p.circle(df['battery_capacity'], df['price'], size=10)
#show(p)

# Create a ColumnDataSource for the data
source = ColumnDataSource(data=dict(
    x=df['battery_capacity'],
    y=df['price'],
    model=df['model']
))

# Create the figure
p = figure(title="Battery capacity vs price", x_axis_label="Battery capacity", y_axis_label="Price")

# Add circles with data from the ColumnDataSource
circle = p.circle(x='x', y='y', size=10, source=source, color = 'blue', line_color = 'black')

# Customize the HoverTool to display the model information
hover = HoverTool()
hover.tooltips = [("Model", "@model")]
p.add_tools(hover)

# Show the plot
show(p)