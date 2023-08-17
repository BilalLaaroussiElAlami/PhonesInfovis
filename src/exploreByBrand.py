import pandas as pd
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, HoverTool, Select, MultiSelect, Slider, RangeSlider, RadioGroup
from bokeh.plotting import figure
from bokeh.transform import factor_cmap


# maka a dataframe from the csv file
smartPhonesDF = pd.read_csv('smartphones.csv')
smartPhonesDF['price'] = smartPhonesDF['price']/100

numerical_columns = smartPhonesDF.select_dtypes(include=['number'])
# Group by 'brand' and calculate the averages for numerical columns
smartphones_brand_averages_df = numerical_columns.groupby(smartPhonesDF['brand_name']).mean().reset_index()

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
    "Fast Charging": "fast_charging",
    "RAM Capacity": "ram_capacity",
    "Internal Memory": "internal_memory",
    "Screen Size": "screen_size",
    "Refresh Rate": "refresh_rate",
    "Number of Rear Cameras": "num_rear_cameras",
    "Primary Rear Camera": "primary_camera_rear",
    "Primary Front Camera": "primary_camera_front",
    "Extended Memory Available": "extended_memory_available",
    "Resolution Height": "resolution_height",
    "Resolution Width": "resolution_width",
}


#INTERACTION WIDGETS
x_axis_choose = Select(title="X Axis", options=sorted(attribute_map.keys()), value="Battery Capacity")
y_axis_choose = Select(title="Y Axis", options=sorted(attribute_map.keys()), value="Price")
price_slider_filter = Slider(title="maximum price", start=100, end=5000, value=500, step=1)
screen_size_bounds = RangeSlider(start=0, end=15, value=(0, 15), step=1, title="screen size bounds (inclusive)")
brand_select = MultiSelect(title="Brands", options= ['ALL'] + smartphones_brand_averages_df['brand_name'].unique().tolist(), value= ["ALL"], height = 100, width = 300)
choose_fast_charging = RadioGroup(labels=["No", "Yes", "Any"], active=2)

ratingThreshold = 8.0
#make 2 dataframes the first dataframe for all rows where the rating is less than 8 and another where the rating is greater than 8
smartphones_brand_averages_dfExcellentRating = smartphones_brand_averages_df[smartphones_brand_averages_df['avg_rating'] >= ratingThreshold]
smartphones_brand_averages_dfNormalRating = smartphones_brand_averages_df[smartphones_brand_averages_df['avg_rating'] < ratingThreshold]

sourceStars = ColumnDataSource(data=dict(
    x=smartphones_brand_averages_dfExcellentRating['battery_capacity'],
    y=smartphones_brand_averages_dfExcellentRating['price'],
    brand=smartphones_brand_averages_dfExcellentRating['brand_name'],
    rating=smartphones_brand_averages_dfExcellentRating['avg_rating']
))

sourceCircles = ColumnDataSource(data=dict(
    x=smartphones_brand_averages_dfNormalRating['battery_capacity'],
    y=smartphones_brand_averages_dfNormalRating['price'],
    brand=smartphones_brand_averages_dfNormalRating['brand_name'],
    rating=smartphones_brand_averages_dfNormalRating['avg_rating']
))


# Define the colors for each brand
brand_colors = {'samsung': 'cyan', 'apple': 'orange', 'huawei': 'green', 'oppo': 'purple', 'xiaomi': 'pink', 'vivo': 'red', 'realme': 'blue', 'oneplus': 'yellow', 'nokia': 'brown', 'sony': 'grey', 'google': 'black'}
brand_mapper = factor_cmap(field_name='brand', factors=list(brand_colors.keys()), palette=list(brand_colors.values()))
Figure2D = figure(x_axis_label="Battery capacity", y_axis_label="Price")

# Add circles with data from the ColumnDataSource
Figure2D.circle(x='x', y='y', size=10, source=sourceCircles, color=brand_mapper, line_color ='black')#, legend_field='brand')
Figure2D.square_pin(x='x', y='y', size=13, source=sourceStars,   color=brand_mapper, line_color ='black')#, legend_field='brand')


#TODO add legend
"""
# Show the legend
Figure2D.legend.title = 'Brand'
Figure2D.legend.label_text_font_size = '10pt'

# Customize the legend items' appearance
Figure2D.legend.background_fill_alpha = 0.7
Figure2D.legend.label_standoff = 8
"""

def select_smartphones():
    max_price = price_slider_filter.value
    minimum_screen_size = screen_size_bounds.value[0]
    maximum_screen_size = screen_size_bounds.value[1]
    want_fast_charging = choose_fast_charging.active #0 is no, 1 is yes, 3 doesnt matter
    selected = smartphones_brand_averages_df[
        (smartphones_brand_averages_df['price'] <= max_price)
        & (smartphones_brand_averages_df['screen_size'] >= minimum_screen_size)
        & (smartphones_brand_averages_df['screen_size'] <= maximum_screen_size)
    ]
    if(want_fast_charging != 2):
        selected = selected[selected['fast_charging_available'] == want_fast_charging]
    if('ALL' not in brand_select.value):
        selected = selected[selected['brand_name'].isin(brand_select.value)]
    #print("☢️ selected: ", selected.head(10))
    return selected

def updateFigure2D():
    print("updated")
    x_name = attribute_map[x_axis_choose.value]
    y_name = attribute_map[y_axis_choose.value]

    Figure2D.xaxis.axis_label = x_axis_choose.value
    Figure2D.yaxis.axis_label = y_axis_choose.value
    selected_smartphones = select_smartphones()
    Figure2D.title.text = f"{len(selected_smartphones)} smartphones"
    """sourceFigure2D.data = dict(
        x=selected_smartphones[x_name],
        y=selected_smartphones[y_name],
        model=selected_smartphones['model'],
        brand=selected_smartphones['brand_name']
    )"""
    updateSource(selected_smartphones, x_name, y_name)

def updateSource(selection, x_name, y_name):
    selectionGoodRating = selection[selection['avg_rating'] >= ratingThreshold]
    sourceStars.data = dict(
        x=selectionGoodRating[x_name],
        y=selectionGoodRating[y_name],
        brand=selectionGoodRating['brand_name'],
        rating = selectionGoodRating['avg_rating']
    )
    selectionNormalRating = selection[selection['avg_rating'] < ratingThreshold]
    sourceCircles.data = dict(
        x=selectionNormalRating[x_name],
        y=selectionNormalRating[y_name],
        brand=selectionNormalRating['brand_name'],
        rating = selectionNormalRating['avg_rating']
    )

controls = [x_axis_choose, y_axis_choose, price_slider_filter, screen_size_bounds, brand_select]
for control in controls:
    control.on_change('value', lambda attr, old, new: updateFigure2D())

selectboxes = [choose_fast_charging]
for selectbox in selectboxes:
    selectbox.on_change('active', lambda attr, old, new: updateFigure2D())

controlsExport = controls + selectboxes

# Customize the HoverTool to display the model information
hover = HoverTool()
hover.tooltips = [("Brand","@brand"), ("Rating", "@rating")]
Figure2D.add_tools(hover)

exploreViewBrand = column(column(controlsExport), Figure2D, width = 1200)



