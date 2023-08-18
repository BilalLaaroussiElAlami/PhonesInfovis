#reference: https://vecco-insight.gitbook.io/crash-visualization/plotly/6.3-statistical-charts/6.3.3-radar-chart

import plotly.express as px
import pandas as pd



def radarplots(valsA,nameA,valsB,nameB, labels):
    df1 = pd.DataFrame(dict(
        r=valsA,
        theta=labels))
    df2 = pd.DataFrame(dict(
        r=valsB,
        theta=labels))

    fig = px.line_polar(df1, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself', name=nameA)

    fig.add_trace(
        px.line_polar(df2, r='r', theta='theta', line_close=True)
        .update_traces(fill='toself', name=nameB)
        .data[0]
    )
    return fig


#example usage of function radarplots
X =  radarplots([0.2, 0.8, 0.4, 0.3, 1], "YUU", [0.5, 0.6, 0.9, 0.7, 0.5], "YUUKES", ['Difficulty', 'Execution', 'Landing','Style', 'Creativity'])
X.show()
"""
# Create multiple dataframes with different data
df1 = pd.DataFrame(dict(
    r=[0.2, 0.8, 0.4, 0.3, 1],
    theta=['Difficulty', 'Execution', 'Landing',
           'Style', 'Creativity']))

df2 = pd.DataFrame(dict(
    r=[0.5, 0.6, 0.9, 0.7, 0.5],
    theta=['Difficulty', 'Execution', 'Landing',
           'Style', 'Creativity']))

# Create a figure and add multiple polar line traces
fig = px.line_polar(df1, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself', name='Dataset 1')

fig.add_trace(
    px.line_polar(df2, r='r', theta='theta', line_close=True)
    .update_traces(fill='toself', name='Dataset 2')
    .data[0]
)

# You can add more traces similarly for more datasets

fig.show()
"""