import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import dash_leaflet as dl

def gaugeCard():
    card = dbc.Card([
                    dbc.CardBody([
                        html.Img(id='gauge-img', src="/assets/icons/river_basin.svg", alt="River Basin", width='100%')
                                ]),
                    ], className='hims-row1 card')
    return card

def textCard():
    card = dbc.Card([
                dbc.Table([
                         html.Tr([
                             html.Td(['River Basin'], colSpan=2),
                             html.Td(['N/A'], id='stationID')
                                ]),
                         html.Tr([
                             html.Td(['Status'], colSpan=2),
                             html.Td(['A moderate amount of caution may be taken while going outdoors. Situation is mostly bearable.'])
                                ])
                            ], className='dashboard-table')
                        ], className='hims-row1 card')
    return card

def mapCard():
    card = dbc.Card(
                    html.Div([
                        dl.Map(id='gwms-map')
                            ], id='hims-plot-div'),
                        className='hims-row2 card')
    return card

def plotCard():
    card = dbc.Card(
                    html.Div([
                        dcc.Graph(id='hims-plot')
                            ], id='hims-plot-div'),
                        className='hims-row2 card')
    return card

def generate_dashboard_gwms():

    dashboard = html.Div([
                        dbc.Row([
                            dbc.Col(gaugeCard(), width='3'),
                            dbc.Col(textCard(), width=True)
                                ], className='hims-row'),
                        dbc.Row([
                            dbc.Col([mapCard()])
                                ], className='hims-row'),
                        dbc.Row([
                            dbc.Col([plotCard()])
                                ], className='hims-row')
                        ])
    return dashboard

