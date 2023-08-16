# Allow user to select multiple models they wish to compare
import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import MultiSelect, ColumnDataSource
from bokeh.plotting import figure

df = pd.read_csv('smartphones.csv')

selected_attribute = 'price'
selected_models = ['Apple iPhone 11', 'Apple iPhone 14', 'Google Pixel 2 XL', 'Samsung Galaxy S23 Plus']


def get_value_attribute(model, attribute):
    print("🤔  model: ", model, " attribute: ", attribute)
    return df.loc[df['model'] == model, attribute].values[0]


def get_values_multiple_models_one_attribute(models, attribute):
    return list(map(lambda model: get_value_attribute(model, attribute), models))


def create_barchart(models):
    source = ColumnDataSource(
        data=dict(models=models,
                  values=get_values_multiple_models_one_attribute(models, selected_attribute)))
    barchart = figure(x_range=models, height=350, title="comparing $attribute",
                      toolbar_location=None, tools="")
    barchart.vbar(x='models', top='values', source=source, width=0.4)
    barchart.xgrid.grid_line_color = None
    barchart.y_range.start = 0
    return barchart

barchart = create_barchart(selected_models)

# will be called when selectinf models or attributes to see/compare
def multi_select_callback(attr, old, new):
    print("‼️  multi_select_callback")
    user_selected_models = multi_select_models.value
    print("🙏  user_selected_models", user_selected_models)
    new_barchart = create_barchart(user_selected_models)
    layout.children[1].children[1] = new_barchart


optionsModels = df['model'].unique().tolist()
multi_select_models = MultiSelect(title="select model(s)::", value=["Apple iPhone 11"], options=optionsModels,
                                  height=200)
multi_select_models.on_change('value', multi_select_callback)

# Allow user to select multiple attributes to be compared
optionsAttributes = df.columns.tolist()
multi_select_attributes = MultiSelect(title="Select attributes:", value=["price"], options=optionsAttributes,
                                      height=200)
multi_select_attributes.on_change('value', multi_select_callback)

compareElements = column(row(multi_select_models, multi_select_attributes), barchart)
layout = row(multi_select_models, compareElements)

curdoc().add_root(layout)
