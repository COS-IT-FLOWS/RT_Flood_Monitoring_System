import pytest
from dash import Dash, html
from apps.Elements.Sidebar import sidebar
from apps.Maps.gwms import generate_map

def test_layout():
    app = Dash(__name__)
    app.layout = html.Div([
        sidebar(),
        generate_map()
    ])

    assert str(app.layout) == '<div id="main-container">\n<div id="sidebar">\n<div class="sidebar-content">\n<div class="sidebar-header">\n<h3>GWMS Dashboard</h3>\n</div>\n<div class="sidebar-body">\n<div class="sidebar-item">\n<h5>River Basin Selection</h5>\n<div class="sidebar-input">\n<select id="river-basin-select" multiple>\n<option value="basin1">Basin 1</option>\n<option value="basin2">Basin 2</option>\n<option value="basin3">Basin 3</option>\n</select>\n</div>\n</div>\n<div class="sidebar-item">\n<h5>Time Range</h5>\n<div class="sidebar-input">\n<input type="date" id="start-date" />\n<input type="date" id="end-date" />\n</div>\n</div>\n<div class="sidebar-item">\n<h5>Variable Selection</h5>\n<div class="sidebar-input">\n<select id="variable-select" multiple>\n<option value="var1">Variable 1</option>\n<option value="var2">Variable 2</option>\n<option value="var3">Variable 3</option>\n</select>\n</div>\n</div>\n</div>\n</div>\n</div>\n<div id="map-pane">\n<div id="map"></div>\n</div>\n</div>\n</div>'