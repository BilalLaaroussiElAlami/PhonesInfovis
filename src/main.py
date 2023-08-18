from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, HTMLTemplateFormatter
from bokeh.plotting import figure
from bokeh.themes import Theme

from compareByBrand import multi_select_models, multi_select_attributes, barchart, getLayoutForCompareByBrand
from exploreByBrand import x_axis_choose, y_axis_choose, Figure2D, price_slider_filter, controlsExport, brand_select
from compare import compareViewModels, getLayoutForCompare
from explore import exploreViewModels
from updateView import group_by_brand, getLayoutForUpdateView, ui_group_by_brand

"""
exploreElements = column(column(controlsExport), Figure2D, width = 1200)
compareElements = column(row(multi_select_models, multi_select_attributes), barchart)
layout = row(exploreElements, compareElements)
getLayout(layout)
"""


layout = column(ui_group_by_brand,  row(exploreViewModels, compareViewModels))
getLayoutForUpdateView(layout)
getLayoutForCompare(layout)
getLayoutForCompareByBrand(layout)


# Add the layout to the document
curdoc().add_root(layout)