import pandas as pd
from bokeh.io import show, curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, HoverTool, Select
from bokeh.plotting import figure



# maka a dataframe from the csv file
df = pd.read_csv('smartphones.csv')
# print the brands of the phones
#print(df['brand_name'].unique())

"""
axis_map = {
    "Tomato Meter": "Meter",
    "Numeric Rating": "numericRating",
    "Number of Reviews": "Reviews",
    "Box Office (dollars)": "BoxOffice",
    "Length (minutes)": "Runtime",
    "Year": "Year",
}"""

attribute_map = {
    "Brand": "brand_name",
    "Model": "model",
    "Price": "price",
    "Average Rating": "avg_rating",
    "5G Support": "5G_or_not",
    "Processor Brand": "processor_brand",
    "Number of Cores": "num_cores",
    "Processor Speed": "processor_speed",
    "Battery Capacity": "battery_capacity",
    "Fast Charging Available": "fast_charging_available",
    "Fast Charging": "fast_charging",
    "RAM Capacity": "ram_capacity",
    "Internal Memory": "internal_memory",
    "Screen Size": "screen_size",
    "Refresh Rate": "refresh_rate",
    "Number of Rear Cameras": "num_rear_cameras",
    "Operating System": "os",
    "Primary Rear Camera": "primary_camera_rear",
    "Primary Front Camera": "primary_camera_front",
    "Extended Memory Available": "extended_memory_available",
    "Resolution Height": "resolution_height",
    "Resolution Width": "resolution_width",
}


x_axis = Select(title="X Axis", options=sorted(attribute_map.keys()), value="Battery Capacity")
y_axis = Select(title="Y Axis", options=sorted(attribute_map.keys()), value="Price")

# make a graph where the x-axis is the battery_capacity and the y-axis is the price, plot the phone models as circles, when the user hovers over a circle
# more information is shown about the phone model:

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


def update():
    print("updated")

    x_name = attribute_map[x_axis.value]
    y_name = attribute_map[y_axis.value]

    p.xaxis.axis_label = x_axis.value
    p.yaxis.axis_label = y_axis.value
    p.title.text = f"{len(df)} movies selected"
    source.data = dict(
        x=df[x_name],
        y=df[y_name],
        model=df['model']
    )

controls = [ x_axis, y_axis]
for control in controls:
    control.on_change('value', lambda attr, old, new: update())

layout =  row(column(x_axis,y_axis),p)
#show(layout)
curdoc().add_root(layout)