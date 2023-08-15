from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
from random import randint

# Create initial data
data = {'categories': ['A', 'B', 'C', 'D', 'E'],
        'values': [randint(1, 10) for _ in range(5)]}

# Create a ColumnDataSource
source = ColumnDataSource(data=data)

# Create a figure
p = figure(x_range=data['categories'], height=350, title="Updatable Bar Chart")
bars = p.vbar(x='categories', top='values', source=source, width=0.5)

# Update function to change the data
def update():
    new_data = {'categories': data['categories'] + ['F'],
                'values': [randint(1, 10) for _ in range(5)]}
    source.data = new_data

# Add a button to update the chart
from bokeh.models import Button
button = Button(label="Update Data", button_type="success")
button.on_click(update)

# Add a button to add a new bar
add_button = Button(label="Add Bar 'F'", button_type="primary")
add_button.on_click(update)


# Add the plot and button to the layout
layout = column(p, button, add_button)

# Add the layout to the current document
curdoc().add_root(layout)
