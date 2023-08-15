import pandas as pd
from bokeh.io import show, curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, HoverTool, Select, MultiSelect
from bokeh.plotting import figure

from compare import multi_select_models, multi_select_attributes

# maka a dataframe from the csv file
df = pd.read_csv('smartphones.csv')
# print the brands of the phones
#print(df['brand_name'].unique())


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


x_axis_choose = Select(title="X Axis", options=sorted(attribute_map.keys()), value="Battery Capacity")
y_axis_choose = Select(title="Y Axis", options=sorted(attribute_map.keys()), value="Price")

# make a graph where the x-axis is the battery_capacity and the y-axis is the price, plot the phone models as circles, when the user hovers over a circle
# more information is shown about the phone model:

# Create a ColumnDataSource for the data
sourceFigure2D = ColumnDataSource(data=dict(
    x=df['battery_capacity'],
    y=df['price'],
    model=df['model'],
    brand = df['brand_name']
))

# Create the figure
Figure2D = figure(title="Battery capacity vs price", x_axis_label="Battery capacity", y_axis_label="Price")

# Add circles with data from the ColumnDataSource
circle = Figure2D.circle(x='x', y='y', size=10, source=sourceFigure2D, color ='blue', line_color ='black')

# Customize the HoverTool to display the model information
hover = HoverTool()
hover.tooltips = [("Model", "@model")]
Figure2D.add_tools(hover)


def updateFigure2D():
    print("updated")

    x_name = attribute_map[x_axis_choose.value]
    y_name = attribute_map[y_axis_choose.value]

    Figure2D.xaxis.axis_label = x_axis_choose.value
    Figure2D.yaxis.axis_label = y_axis_choose.value
    Figure2D.title.text = f"{len(df)} movies selected"
    sourceFigure2D.data = dict(
        x=df[x_name],
        y=df[y_name],
        brand=df['brand_name']
    )

controls = [x_axis_choose, y_axis_choose]
for control in controls:
    control.on_change('value', lambda attr, old, new: updateFigure2D())




