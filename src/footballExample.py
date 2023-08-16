from bokeh.io import show
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Button, TextInput
from bokeh.layouts import column

# Initial data
players = ["Player A", "Player B", "Player C", "Player D"]
goals = [25, 18, 30, 15]

source = ColumnDataSource(data=dict(players=players, goals=goals))

# Create the figure
p = figure(x_range=players, height=350, title="Soccer Players and Goals")
bars = p.vbar(x='players', top='goals', width=0.5, source=source, line_color="white")

# Text input and button for adding a player
new_player_input = TextInput(title="New Player Name")
add_button = Button(label="Add Player")

# Define a callback function for the button
def add_player():
    new_player_name = new_player_input.value
    if new_player_name:
        print(" 🔔added new player: ", new_player_name)
        players.append(new_player_name)
        print(players)
        goals.append(10)  # Initialize with 10 goals
        source.data = dict(players=players, goals=goals)
        print(" 🔔 source.data: ", source.data)
        p.x_range.factors = players  # Update x-axis range
        bars.data_source.data['x'] = players  # Update x-axis range
        bars.data_source.data['top'] = goals  # Update bar heights
        show(p)


add_button.on_click(add_player)

# Customize the plot
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.yaxis.axis_label = "Number of Goals"

# Add the plot, input, and button to the current document
layout = column(p, new_player_input, add_button)
curdoc().add_root(layout)
