#reference: https://vecco-insight.gitbook.io/crash-visualization/plotly/6.3-statistical-charts/6.3.3-radar-chart


import plotly.express as px
import pandas as pd

#get the maximum values of each attribute of smartphones.csv associated with
def getMaxVals():
    df = pd.read_csv('smartphones.csv')
    #divide 'price' bu 100
    df['price'] = df['price']/100
    df = df.select_dtypes(include=['int64', 'float64', 'int32', 'float32', 'int', 'float', 'number'])
    maxVals = df.max()
    return maxVals

def create_radar_plot(valsA, nameA, valsB, nameB, labels):
    #normalize valsA and valsB
    valsA = [x/maxvals[labels[i]] for i,x in enumerate(valsA)]
    valsB = [x/maxvals[labels[i]] for i,x in enumerate(valsB)]

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



""""
#example usage of function radarplots
X =  create_radar_plot([100, 5.8, 4], "YUU", [300, 6.6, 3], "YUUKES", ['price', 'avg_rating', 'num_cores'])
X.show()
"""


