import pandas as pd
from bokeh.io import show, curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, HoverTool, Select, MultiSelect, Slider, RangeSlider, RadioGroup, Legend, Div
from bokeh.models.ui.dialogs import Button
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

from preprocessing import smartphonesDF, getMaxValue, numerical_columns
from legend import legendDiv

attribute_map = {
    "Brand": "brand_name",
    "Price": "price",
    "Average Rating": "avg_rating",
    "5G Support": "5G_or_not",
    "Processor Brand": "processor_brand",
    "Number of Cores": "num_cores",
    "Processor Speed": "processor_speed",
    "Battery Capacity": "battery_capacity",
    "Fast Charging Available": "fast_charging_available",
    "RAM Capacity": "ram_capacity",
    "Internal Memory": "internal_memory",
    "Screen Size": "screen_size",
    "Refresh Rate": "refresh_rate",
    "Number of Rear Cameras": "num_rear_cameras",
    "Primary Rear Camera Quality": "primary_camera_rear",
    "Primary Front Camera Quality": "primary_camera_front",
    "Extended Memory Available": "extended_memory_available",
    "Resolution Height": "resolution_height",
    "Resolution Width": "resolution_width",
}
#filter only numerical values
attribute_map =  dict(filter(lambda item: item[1] in numerical_columns, attribute_map.items()))

#INTERACTION WIDGETS
x_axis_choose = Select(title="X Axis", options=sorted(attribute_map.keys()), value="Battery Capacity")
y_axis_choose = Select(title="Y Axis", options=sorted(attribute_map.keys()), value="Price")
price_slider_filter = Slider(title="maximum price", start=100, end=5000, value=5000, step=1)
screen_size_bounds = RangeSlider(start=0, end=15, value=(0, 15), step=0.1, title="screen size bounds (inclusive)")
brand_select = MultiSelect(title="Brands", options= ['ALL'] + smartphonesDF['brand_name'].unique().tolist(), value= ["ALL"], height = 100, width = 300)
choose_fast_charging = RadioGroup(labels=["No", "Yes", "Any"], active=2)
choose_extended_memory_available = RadioGroup(labels=["No", "Yes", "Any"], active=2)
choose_5G_or_not = RadioGroup(labels=["No", "Yes", "Any"], active=2)

ui_choice_fast_charging = column(Div(text= " <b>Fast charging</b>"), choose_fast_charging)
ui_choice_extended_memory = column(Div(text= " <b>Extended memory</b>"), choose_extended_memory_available)
ui_choice_5G_or_not = column(Div(text= " <b>5G support</b>"), choose_5G_or_not)


ratingThreshold = 8.0
#make 2 dataframes the first dataframe for all rows where the rating is less than 8 and another where the rating is greater than 8
smartphonesDFExcellentRating = smartphonesDF[smartphonesDF['avg_rating'] >= ratingThreshold]
smartphonesDFNormalRating = smartphonesDF[smartphonesDF['avg_rating'] < ratingThreshold]

sourceStars = ColumnDataSource(data=dict(
    x=smartphonesDFExcellentRating['battery_capacity'],
    y=smartphonesDFExcellentRating['price'],
    model=smartphonesDFExcellentRating['model'],
    brand=smartphonesDFExcellentRating['brand_name'],
    rating=smartphonesDFExcellentRating['avg_rating']
))

sourceCircles = ColumnDataSource(data=dict(
    x=smartphonesDFNormalRating['battery_capacity'],
    y=smartphonesDFNormalRating['price'],
    model=smartphonesDFNormalRating['model'],
    brand=smartphonesDFNormalRating['brand_name'],
    rating=smartphonesDFNormalRating['avg_rating']
))


# Define the colors for each brand
brand_colors = {'samsung': 'cyan', 'apple': 'orange', 'huawei': 'green', 'oppo': 'purple', 'xiaomi': 'pink', 'vivo': 'red', 'realme': 'blue', 'oneplus': 'yellow', 'nokia': 'brown'}
brand_mapper = factor_cmap(field_name='brand', factors=list(brand_colors.keys()), palette=list(brand_colors.values()))
Figure2D = figure(x_axis_label="Battery capacity", y_axis_label="Price")

# Add circles with data from the ColumnDataSource
Figure2D.circle(x='x', y='y', size=10, source=sourceCircles, color=brand_mapper, line_color ='black')
Figure2D.square_pin(x='x', y='y', size=13, source=sourceStars,   color=brand_mapper, line_color ='black')




def select_smartphones():
    max_price = price_slider_filter.value
    minimum_screen_size = screen_size_bounds.value[0]
    maximum_screen_size = screen_size_bounds.value[1]
    want_fast_charging = choose_fast_charging.active #0 is no, 1 is yes, 3 doesnt matter
    want_extended_memory_available = choose_extended_memory_available.active #0 is no, 1 is yes, 3 doesnt matter
    want_5G_or_not = choose_5G_or_not.active #0 is no, 1 is yes, 3 doesnt matter
    selected = smartphonesDF[
        (smartphonesDF['price'] <= max_price)
        & (smartphonesDF['screen_size'] >= minimum_screen_size)
        & (smartphonesDF['screen_size'] <= maximum_screen_size)
    ]
    if(want_fast_charging != 2):
        selected = selected[selected['fast_charging_available'] == want_fast_charging]
    if(want_extended_memory_available != 2):
        selected = selected[selected['extended_memory_available'] == want_extended_memory_available]
    if(want_5G_or_not != 2):
        selected = selected[selected['5G_or_not'] == want_5G_or_not]
    if('ALL' not in brand_select.value):
        selected = selected[selected['brand_name'].isin(brand_select.value)]
    return selected

def updateSource(selection, x_name, y_name):
    selectionGoodRating = selection[selection['avg_rating'] >= ratingThreshold]
    sourceStars.data = dict(
        x=selectionGoodRating[x_name],
        y=selectionGoodRating[y_name],
        model=selectionGoodRating['model'],
        brand=selectionGoodRating['brand_name'],
        rating = selectionGoodRating['avg_rating']
    )
    selectionNormalRating = selection[selection['avg_rating'] < ratingThreshold]
    sourceCircles.data = dict(
        x=selectionNormalRating[x_name],
        y=selectionNormalRating[y_name],
        model=selectionNormalRating['model'],
        brand=selectionNormalRating['brand_name'],
        rating=selectionNormalRating['avg_rating']
    )

def updateFigure2D():
    x_name = attribute_map[x_axis_choose.value]
    y_name = attribute_map[y_axis_choose.value]

    Figure2D.xaxis.axis_label = x_axis_choose.value
    Figure2D.yaxis.axis_label = y_axis_choose.value
    Figure2D.y_range.start = 0
    Figure2D.y_range.end = getMaxValue(y_name)*1.1
    Figure2D.x_range.start = 0
    Figure2D.x_range.end = getMaxValue(x_name)*1.1

    selected_smartphones = select_smartphones()
    Figure2D.title.text = f"{len(selected_smartphones)} smartphones"
    updateSource(selected_smartphones, x_name, y_name)

controls = [x_axis_choose, y_axis_choose, price_slider_filter, screen_size_bounds, brand_select]
for control in controls:
    control.on_change('value', lambda attr, old, new: updateFigure2D())

choose_fast_charging.on_change('active', lambda attr, old, new: updateFigure2D())
choose_extended_memory_available.on_change('active', lambda attr, old, new: updateFigure2D())
choose_5G_or_not.on_change('active', lambda attr, old, new: updateFigure2D())

controlsExport = controls + [row(ui_choice_fast_charging, ui_choice_extended_memory, ui_choice_5G_or_not)]
exploreViewModels = row(column(controlsExport), Figure2D, legendDiv, width = 1010)

hover = HoverTool()
hover.tooltips = [("Model", "@model"), ("Rating", "@rating")]
Figure2D.add_tools(hover)



