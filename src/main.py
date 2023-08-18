from bokeh.io import curdoc
from bokeh.layouts import row, column

from compareByBrand import  getLayoutForCompareByBrand
from compare import compareViewModels, getLayoutForCompare
from explore import exploreViewModels
from updateView import getLayoutForUpdateView, ui_group_by_brand

layout = column(ui_group_by_brand,  row(exploreViewModels, compareViewModels))
getLayoutForUpdateView(layout)
getLayoutForCompare(layout)
getLayoutForCompareByBrand(layout)
curdoc().add_root(layout)