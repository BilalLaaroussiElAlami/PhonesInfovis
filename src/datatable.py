from bokeh.io import show, output_file
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, DataTable, TableColumn
import pandas as pd
from bokeh.plotting import figure

df = pd.read_csv('smartphones.csv')

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, DataTable, TableColumn
import pandas as pd

def create_data_table(models, attributes):
    filtered_data = df[df['model'].isin(models)]
    source = ColumnDataSource(filtered_data)
    column_width = 100
    columns = [TableColumn(field='Model', title='Model', width=column_width)] + \
              [TableColumn(field=attribute, title=attribute, width=column_width) for attribute in attributes]
    data_table = DataTable(source=source, columns=columns, height_policy="fit")
    return data_table

# List of models and attributes
models = ["Model1", "Model3"]  # Example models
attributes = ["Attribute1", "Attribute2", "Attribute3"]

# Create the DataTable
data_table = create_data_table(models, attributes)
# Create the DataTable
data_table = create_data_table(['Apple iPhone 11', 'Apple iPhone 14', 'Google Pixel 2 XL', 'Samsung Galaxy S23 Plus'], ['price', 'num_cores','processor_speed','battery_capacity'])
data_table2 = create_data_table(['Apple iPhone 11'], ['price'])
show(data_table)

