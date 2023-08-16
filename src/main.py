from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

from comapareNEW import multi_select_models, multi_select_attributes, barchart, getLayout
from explore import x_axis_choose, y_axis_choose, Figure2D, price_slider_filter, controlsExport


exploreElements = column(column(controlsExport) , Figure2D)
compareElements = column(row(multi_select_models, multi_select_attributes), barchart)
layout = row(exploreElements, compareElements)
getLayout(layout)

curdoc().add_root(layout)


