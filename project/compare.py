# Allow user to select multiple models they wish to compare
from bokeh.models import MultiSelect

from project.main import df

optionsModels = df['model'].unique().tolist()
multi_select_models = MultiSelect(title="select model(s)::", value=["Option 1"], options=optionsModels, height= 200)

def multi_select_callback(attr, old, new):
    selected_models = multi_select_models.value
    selected_attributes = multi_select_attributes.value
    print("Selected models:", selected_models)
    print("Selected attributes:", selected_attributes)

multi_select_models.on_change('value', multi_select_callback)

# Allow user to select multiple attributes to be compared
optionsAttributes = df.columns.tolist()
multi_select_attributes = MultiSelect(title="Select attributes:", value=["Option 1"], options=optionsAttributes, height= 200)
multi_select_attributes.on_change('value', multi_select_callback)
multi_select_attributes.on_change('value', multi_select_callback)