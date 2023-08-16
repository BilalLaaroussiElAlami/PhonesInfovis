#reference: https://vecco-insight.gitbook.io/crash-visualization/plotly/6.3-statistical-charts/6.3.3-radar-chart

import pandas as pd

df = pd.DataFrame(dict(
    r=[4, 5, 2, 4, 3],
    theta=['Difficulty', 'Execution', 'Landing',
           'Style', 'Creativity']))

import plotly.express as px



fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself')
fig.show()