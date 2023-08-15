from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

initalData = {'models': ["a", "b", "c"],
              'values': [1, 2, 3]
              }
source = ColumnDataSource(data=initalData)


barchart = figure(x_range= ["a","b","c"],  height=350, title="comparing $attribute",
                  toolbar_location=None, tools="")

barchart.vbar(x='models', top= 'values', source = source ,width=0.4)
barchart.xgrid.grid_line_color = None
barchart.y_range.start = 0



layout = column(barchart)
show(layout)


updatedinitalData = {'models': ["x", "y", "z"],
              'values': [24, 25, 26]
              }
updatasource = ColumnDataSource(data=updatedinitalData)

updatedbarchart = figure(x_range= ["x","y","z"],  height=350, title="comparing $attribute",
                  toolbar_location=None, tools="")

updatedbarchart.vbar(x='models', top= 'values', source = updatasource ,width=0.4)
updatedbarchart.xgrid.grid_line_color = None
barchart.y_range.start = 0
layout.children[0] = updatedbarchart
show(layout)
