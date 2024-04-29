from dash import html, dcc
import dash_bootstrap_components as dbc
from apps.Elements.Sidebar import sidebar
from apps.Maps.gwms import generate_map
# Import modules to generate plots


# Load river basins geojson to memory

map_main = generate_map()

body = html.Div(id='main-container', children=[
                                            dbc.Collapse(id='collapsible', is_open=False,
                                            children=[
                                                html.Div(id='dashboard'),
                                                dbc.Button(id='close-button', children=[html.Img(src='/assets/icons/Close_Button.png', width='27px', height='27px')]),
                                                    ]),
                                        html.Div(id='map-pane', children=[map_main]),
                                        sidebar()
                                                ])


layout = html.Div([
    dcc.Store(id='river-basin-selection-gwms'),
    body
])

