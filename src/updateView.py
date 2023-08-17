from bokeh.models import RadioGroup

from compare import compareViewModels
from compareByBrand import compareViewBrand
from explore import exploreViewModels
from exploreByBrand import exploreViewBrand

group_by_brand = RadioGroup(labels=["Yes", "No"], active=0)

def updateView():
    print("🤔  group_by_brand", group_by_brand.active)
    if(group_by_brand.active == 0):
        layout.children[1].children[0] = exploreViewModels
        layout.children[1].children[1] = compareViewModels
    else:
        layout.children[1].children[0] = exploreViewBrand
        layout.children[1].children[1] = compareViewBrand


layout = None
def getLayoutForUpdateView(llayout):
    global layout
    layout = llayout

group_by_brand.on_change('active', lambda attr, old, new: updateView())