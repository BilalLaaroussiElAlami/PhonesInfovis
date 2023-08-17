# Allow user to select multiple models they wish to compare
import pandas as pd
from bokeh.io import curdoc, show
from bokeh.layouts import column, row
from bokeh.models import MultiSelect, ColumnDataSource, Div
from bokeh.plotting import figure


smartPhonesDF = pd.read_csv('smartphones.csv')
numerical_columns = smartPhonesDF.select_dtypes(include=['number'])
# Group by 'brand' and calculate the averages for numerical columns
smartphones_brand_averages_df = numerical_columns.groupby(smartPhonesDF['brand_name']).mean().reset_index()


initial_attribute = 'price'
initial_brands = ['apple', 'samsung', 'huawei']


def get_value_attribute(brand, attribute):
    print("🤔  brand:", brand ," attribute:",attribute)
    return smartphones_brand_averages_df.loc[smartphones_brand_averages_df['brand_name'] == brand, attribute].values[0]

def get_values_multiple_brands_one_attribute(brands, attribute):
    return list(map(lambda model: get_value_attribute(model, attribute), brands))

def create_barchart(brands, attribute):
    source = ColumnDataSource(
        data=dict(models=brands,
                  values=get_values_multiple_brands_one_attribute(brands, attribute)))
    barchart = figure(x_range=brands, height=350, title=f"comparing {attribute}",
                      toolbar_location=None, tools="")
    barchart.vbar(x='models', top='values', source=source, width=0.4)
    barchart.xgrid.grid_line_color = None
    barchart.y_range.start = 0
    return barchart

barchart = create_barchart(initial_brands, initial_attribute)
# will be called when selecting brands or attributes to see/compare
def create_data_table(brands, attributes):
    filtered_data = smartphones_brand_averages_df[smartphones_brand_averages_df['brand_name'].isin(brands)]
    html = '<table>'
    # Create the header row
    html += '<tr>'
    for attr in ['Model'] + attributes:
        html += f'<th>{attr}</th>'
    html += '</tr>'

    for index, row in filtered_data.iterrows():
        html += '<tr>'
        for attr in ['brand_name'] + attributes:
            html += f'<td> {row[attr]}</td>'
        html += '</tr>'
    html += '</table>'
    print("html brandddddd 😝: ")
    print(html)
    return Div(text = html)

data_table = create_data_table(initial_brands, [initial_attribute])



def multi_select_callback(attr, old, new):
    user_selected_models = multi_select_models.value
    print("🙏  user_selected_models", user_selected_models)
    user_selected_attributes = multi_select_attributes.value
    user_selected_attribute = multi_select_attributes.value[0]
    new_barchart = create_barchart(user_selected_models, user_selected_attribute)
    update_barchart(layout, new_barchart)
    if(len(user_selected_attributes) > 1):
        new_barcharts = list(map(lambda attribute: create_barchart(user_selected_models, attribute), user_selected_attributes))
        update_barcharts(layout, new_barcharts)
    update_data_table(layout, create_data_table(user_selected_models, user_selected_attributes))

def update_barchart(llayout, nnewbarchart):
    compareViewBrand.children[1] = nnewbarchart
    llayout.children[1].children[1] = compareViewBrand


def update_barcharts(llayout, barcharts):
    compareViewBrand.children[1]  = column(barcharts)
    llayout.children[1].children[1] = compareViewBrand

def update_data_table(llayout, data_table):
    compareViewBrand.children[0].children[1] = data_table
    llayout.children[1].children[1] = compareViewBrand


#INTERACTION WIDGETS
optionsBrands = smartphones_brand_averages_df['brand_name'].unique().tolist()
multi_select_models = MultiSelect(title="select brand(s)::", value=["apple"], options=optionsBrands,
                                         height=200)
multi_select_models.on_change('value', multi_select_callback)


# Allow user to select multiple attributes to be compared
optionsAttributes = smartphones_brand_averages_df.columns.tolist()
multi_select_attributes = MultiSelect(title="Select attributes:", value=["price"], options=optionsAttributes,
                                      height=200)
multi_select_attributes.on_change('value', multi_select_callback)
layout = None
#This module would needs to have acces to the layout because it will modify it!
def getLayoutForCompareByBrand(llayout):
    global layout
    layout = llayout

compareViewBrand = column(column(row(multi_select_models, multi_select_attributes), data_table, barchart, width = 1200))



