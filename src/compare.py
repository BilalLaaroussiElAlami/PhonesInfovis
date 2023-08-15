# Allow user to select multiple models they wish to compare
import pandas as pd
from bokeh.models import MultiSelect, ColumnDataSource
from bokeh.plotting import figure



df = pd.read_csv('smartphones.csv')

initial_attribute = 'avg_rating',
initial_models = ['Apple iPhone 11', 'Google Pixel 2 XL']

def get_value_attribute(model, attribute):
    print("🤔  model: ", model, " attribute: ", attribute)
    return df.loc[df['model'] == model, attribute].values[0]
def get_values_multiple_models_one_attribute(models, attribute):
    return list(map(lambda model: get_value_attribute(model, attribute), models))
def get_values_attributes(model, attributes):
    return list(map(lambda attribute: get_value_attribute(model, attribute), attributes))

initalData = {'models': initial_models,
              'values': get_values_multiple_models_one_attribute(initial_models, initial_attribute)
              }
source = ColumnDataSource(data=initalData)


barchart = figure(x_range= initial_models , height=350, title="comparing $attribute",
                  toolbar_location=None, tools="")

barchart.vbar(x='models', top= 'values', source = source ,width=0.4)
barchart.xgrid.grid_line_color = None
barchart.y_range.start = 0



#will be called when selectinf models or attributes to see/compare
def multi_select_callback(attr, old, new):
    print("‼️  multi_select_callback")
    selected_models = multi_select_models.value
    selected_attributes = multi_select_attributes.value
    print("🙏",  selected_models, selected_attributes)
    newvalues = get_values_multiple_models_one_attribute(selected_models, selected_attributes[0])
    print("new values 🎉 : ", newvalues)
    source.data['models'] = selected_models
    source.data['values'] = newvalues


    """newbarchart = figure(x_range=initial_models, height=350, title="comparing $attribute",
                      toolbar_location=None, tools="")

    newbarchart.vbar(x= selected_models , top= newvalues, source=source, width=0.4)
    newbarchart.xgrid.grid_line_color = None
    newbarchart.y_range.start = 0
    updateBarChart(newbarchart)"""



optionsModels = df['model'].unique().tolist()
multi_select_models = MultiSelect(title="select model(s)::", value=["Apple iPhone 11"], options=optionsModels, height= 200)
multi_select_models.on_change('value', multi_select_callback)

# Allow user to select multiple attributes to be compared
optionsAttributes = df.columns.tolist()
multi_select_attributes = MultiSelect(title="Select attributes:", value=["price"], options=optionsAttributes, height= 200)
multi_select_attributes.on_change('value', multi_select_callback)


#from main import updateBarChart