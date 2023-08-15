from bokeh.io import curdoc
from bokeh.layouts import row, column

from compare import multi_select_models, multi_select_attributes
from explore import x_axis_choose, y_axis_choose, Figure2D

layout =  row(column(column(x_axis_choose, y_axis_choose), Figure2D), multi_select_models, multi_select_attributes)
curdoc().add_root(layout)