# Importing library's
from bokeh.plotting import figure, show, output_notebook
import pandas as pd

# Create Students,Subjects list and Colours.
Students = ['Ankur', 'Yash', 'Aditya', 'Harshit']
Subjects = ['Operating System', 'Data Structure',\
			'Java Programming']
cols = ['#00ff00', '#009900', '#00cc99']
# Initialize data to lists.
data = {'Students': Students,
		'Operating System': [17, 20, 19, 18],
		'Data Structure': [19, 18, 20, 17],
		'Java Programming': [20, 19, 20, 18]
		}
# Creates DataFrame.
df = pd.DataFrame(data)
df.head()

# plot data in Stack manner of bar type
fig = figure(x_range=df.Students,
			height=500,
			title="Marks counts of \
			every students according to subjects")
fig.vbar_stack(Subjects,
			x='Students',
			source=df,
			color=cols,
			width=0.5)
# Display Stack Graph
show(fig)
