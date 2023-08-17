from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, Div
import pandas as pd

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

# List of models and attributes
models = ["Apple iPhone 11", "Apple iPhone 14", "Google Pixel 2 XL", "Samsung Galaxy S23 Plus"]
attributes = ["price", "battery_capacity", "screen_size"]

# Create the HTML representation
div = create_data_table(models, attributes)


show(div)
