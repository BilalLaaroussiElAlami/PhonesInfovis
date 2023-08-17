# Allow user to select multiple models they wish to compare
import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import MultiSelect, ColumnDataSource, Div
from bokeh.plotting import figure


df = pd.read_csv('smartphones.csv')

initial_attribute = 'price'
initial_models = ['Apple iPhone 11', 'Apple iPhone 14', 'Google Pixel 2 XL', 'Samsung Galaxy S23 Plus']

def get_value_attribute(model, attribute):
    print("🤔  model: ", model, " attribute: ", attribute)
    return df.loc[df['model'] == model, attribute].values[0]

def get_values_multiple_models_one_attribute(models, attribute):
    return list(map(lambda model: get_value_attribute(model, attribute), models))

def create_barchart(models,attribute):
    source = ColumnDataSource(
        data=dict(models=models,
                  values=get_values_multiple_models_one_attribute(models, attribute)))
    barchart = figure(x_range=models, height=350, title=f"comparing {attribute}",
                      toolbar_location=None, tools="")
    barchart.vbar(x='models', top='values', source=source, width=0.4)
    barchart.xgrid.grid_line_color = None
    barchart.y_range.start = 0
    return barchart

def create_data_table(models, attributes):
    data = pd.read_csv('smartphones.csv')
    filtered_data = data[data['model'].isin(models)]
    html = '<table>'
    for index, row in filtered_data.iterrows():
        html += '<tr>'
        for attr in ['model'] + attributes:
            html += f'<td> {row[attr]}</td>'
        html += '</tr>'
    html += '</table>'
    return Div(text = html)

data_table = create_data_table(initial_models, [initial_attribute])

barchart = create_barchart(initial_models, initial_attribute)
# will be called when selectinf models or attributes to see/compare
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
    compareViewModels.children[1] = nnewbarchart
    llayout.children[1].children[1] = compareViewModels


def update_barcharts(llayout, barcharts):
    compareViewModels.children[1]  = column(barcharts)
    llayout.children[1].children[1] = compareViewModels

def update_data_table(llayout, data_table):
    compareViewModels.children[0].children[1] = data_table
    llayout.children[1].children[1] = compareViewModels

#INTERACTION WIDGETS
optionsModels = df['model'].unique().tolist()
multi_select_models = MultiSelect(title="select model(s)::", value=["Apple iPhone 11"], options=optionsModels,
                                  height=200)
multi_select_models.on_change('value', multi_select_callback)

# Allow user to select multiple attributes to be compared
optionsAttributes = df.columns.tolist()
multi_select_attributes = MultiSelect(title="Select attributes:", value=["price"], options=optionsAttributes,
                                      height=200)
multi_select_attributes.on_change('value', multi_select_callback)




compareViewModels = column(column(row(multi_select_models, multi_select_attributes), data_table), barchart, width = 1200)

layout = None

#This module would needs to have acces to the layout because it will modify it!
def getLayoutForCompare(llayout):
    global layout
    layout = llayout


