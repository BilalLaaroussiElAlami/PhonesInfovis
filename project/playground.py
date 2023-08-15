import pandas as pd
import plotly.express as px

# Create a DataFrame with multiple sets of data
data = {
    'Difficulty': [4, 3, 5, 2, 4],
    'Execution': [3, 4, 3, 0, 4],
    'Landing': [2, 3, 4, 3, 5],
    'Style': [5, 2, 2, 4, 3],
    'Creativity': [3, 4, 3, 5, 2]
}

df = pd.DataFrame(data)
df['theta'] = ['Difficulty', 'Execution', 'Landing', 'Style', 'Creativity']

# Create a radar chart with multiple lines
fig = px.line_polar(df, r='Difficulty', theta='theta', line_close=True, title='Radar Chart')

# Add traces and customize colors and dashes
traces = [
    px.line_polar(df, r=attr, theta='theta', line_close=True).data[0]
    for attr in ['Execution']
]

# Customize line colors and dashes for each trace
for i, trace in enumerate(traces):
    trace.line.color = px.colors.qualitative.Set1[i]  # Set a color from the Set1 palette
    trace.line.dash = 'solid'  # Change line dash style if needed

fig.add_traces(traces)
fig.show()
