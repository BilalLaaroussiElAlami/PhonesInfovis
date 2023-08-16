from bokeh.plotting import figure, show, curdoc
from bokeh.models import ColumnDataSource, Button, TextInput
from bokeh.layouts import column, row
from copy import deepcopy

# Initial data
players = ["Player A", "Player B", "Player C", "Player D"]
goals = [25, 18, 30, 15]

source = ColumnDataSource(data=dict(players=players, goals=goals))

# Text input and button for adding a player
new_player_input = TextInput(title="New Player Name")
add_button = Button(label="Add Player")

# Create the figure function
def create_figure():
    p = figure(x_range=players, height=350, title="Soccer Players and Goals")
    p.vbar(x='players', top='goals', width=0.5, source=source, line_color="white")
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Number of Goals"
    return p

# Define a callback function for the button
def add_player():
    new_player_name = new_player_input.value
    if new_player_name:
        players.append(new_player_name)
        goals.append(10)  # Initialize with 0 goals
        source.data = dict(players=players, goals=goals)
        new_p = create_figure()  # Create new barchart
        layout.children[0].children[0] = new_p  # Replace old chart with the new one

add_button.on_click(add_player)

# Create the initial figure
p = create_figure()

# Create nested layout
button_row = row(new_player_input, add_button)
layout = column(p, button_row)

layout = column(column(p, new_player_input), add_button)

curdoc().add_root(layout)

# To run the script, execute: bokeh serve --show script_name.py
