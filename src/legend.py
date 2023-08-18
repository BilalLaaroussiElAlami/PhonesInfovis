from bokeh.plotting import show, figure
from bokeh.models import Div

# HTML code for the circle and text
html_code = """
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  .legend {
    font-family: Arial, sans-serif;
    font-size: 12px;
  }
  .legend-item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  .circle {
    border-radius: 45%;
  }
  .square {
    border-radius: 5px;
  }
  .color-box {
    width: 20px;
    height: 20px;
    margin-right: 5px;
  }
</style>
</head>
<body>
  <div class="legend">
    <div class="legend-item">
      <div class="color-box circle" style = "background-color: gray;"  ></div>
      <span>smartphone</span>
    </div>
    <div class="legend-item">
      <div class="color-box" style = "background-color: gray;" ></div>
      <span>excellent</span>
    </div>
    <div class="legend-item">
      <div class="color-box circle" style="background-color: orange"></div>
      <span>Apple</span>
    </div>
    <div class="legend-item">
      <div class="color-box circle" style="background-color: cyan"></div>
      <span>Samsung</span>
    </div>
    <div class="legend-item">
      <div class="color-box circle" style="background-color: green"></div>
      <span>Huawei</span>
    </div>
    <div class="legend-item">
        <div class="color-box circle" style="background-color: purple"></div>
        <span>Oppo</span>
    </div>
    <div class="legend-item">
        <div class="color-box circle" style="background-color: red"></div>
        <span>vivo</span>
    </div>
    <div class="legend-item">
        <div class="color-box circle" style="background-color: gray"></div>
        <span>other</span>
    </div>
</body>
</html>
"""

# Add a Div widget with the HTML code
legendDiv = Div(text=html_code)


