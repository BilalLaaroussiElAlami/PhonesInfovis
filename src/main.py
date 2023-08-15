from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

from compare import multi_select_models, multi_select_attributes, barchart
from explore import x_axis_choose, y_axis_choose, Figure2D

exploreElements = column(column(x_axis_choose, y_axis_choose), Figure2D)
compareElements = column(row(multi_select_models, multi_select_attributes), barchart)
layout = row(exploreElements, compareElements)


def updateBarChart(newBarchart):
    return
    #compareElements = column(row(multi_select_models, multi_select_attributes), newBarchart)
    #layout.children = row(exploreElements, compareElements)
    #curdoc().add_root(layout)


curdoc().add_root(layout)



updatedinitalData = {'models': ["x", "y", "z"],
              'values': [24, 25, 26]
            }
updatasource = ColumnDataSource(data=updatedinitalData)

updatedbarchart = figure(x_range= ["x","y","z"],  height=350, title="comparing $attribute",
                  toolbar_location=None, tools="")

updatedbarchart.vbar(x='models', top= 'values', source = updatasource ,width=0.4)
updatedbarchart.xgrid.grid_line_color = None
barchart.y_range.start = 0
#layout.children[0]  = updatedbarchart