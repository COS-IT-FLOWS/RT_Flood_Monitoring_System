import sys
from dash import dcc, html
import dash_bootstrap_components as dbc
from apps.Maps.tdms import generate_map
from apps.Elements.Sidebar import sidebar


map_main = generate_map()

body = html.Div(id='main-container', children=[

        dbc.Collapse(id='collapsible', is_open=False,
                     children=[
                         html.Div(id='dashboard-pane', children=[
                             dbc.Button(id='close-button', children=[
                                 html.Img(src='/assets/icons/Close_Button.png', width='27px', height='27px')],
                                        className='close-button'),
                             html.Div(id='dashboard')
                         ])
                     ]),
    html.Div(id='map-pane', children=[map_main]),
                                        sidebar()
                                                ])


layout = html.Div([
    dcc.Store(id='river-basin-selection'),
    body
])


