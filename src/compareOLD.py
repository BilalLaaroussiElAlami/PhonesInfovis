# Allow user to select multiple models they wish to compare
import pandas as pd
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


source = ColumnDataSource(
    data=dict(models = selected_models,
            values = get_values_multiple_models_one_attribute(selected_models, selected_attribute)))

def create_barchart():
    barchart = figure(x_range=selected_models, height=350, title="comparing $attribute",
                      toolbar_location=None, tools="")
    barchart.vbar(x='models', top='values', source=source, width=0.4)
    barchart.xgrid.grid_line_color = None
    barchart.y_range.start = 0
    return barchart

barchart = create_barchart()

#will be called when selectinf models or attributes to see/compare
def multi_select_callback(attr, old, new):
    print("‼️  multi_select_callback")
    global selected_models
    selected_models = multi_select_models.value
    print("🙏",  selected_models, selected_models)
    newvalues = get_values_multiple_models_one_attribute(selected_models, selected_attribute)
    print("new values 🎉 : ", newvalues)
    source.data = dict(models = selected_models, values=newvalues)
    new_barchart = create_barchart()



optionsModels = df['model'].unique().tolist()
multi_select_models = MultiSelect(title="select model(s)::", value=["Apple iPhone 11"], options=optionsModels, height= 200)
multi_select_models.on_change('value', multi_select_callback)

# Allow user to select multiple attributes to be compared
optionsAttributes = df.columns.tolist()
multi_select_attributes = MultiSelect(title="Select attributes:", value=["price"], options=optionsAttributes, height= 200)
multi_select_attributes.on_change('value', multi_select_callback)


