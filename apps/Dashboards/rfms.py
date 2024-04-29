import dash_bootstrap_components as dbc
from dash import dcc, html

def gaugeCard():
    card = dbc.Card([
                    dbc.CardBody([
                        html.Img(id='gauge-img', src="/assets/icons/rainfall_station.svg", alt="Rain Gauge", width='100%')
                                ]),
                    ], className='hims-row1 card')
    return card

def textCard(stationID):
    card = dbc.Card([
                dbc.Table([
                         html.Tr([
                             html.Td(['Station'], colSpan=2),
                             html.Td([stationID], id='stationID')
                                ]),
                         html.Tr([
                             html.Td(['Rainfall'], rowSpan=4),
                             html.Td(['Current']),
                             html.Td(["N/A"], id='rf-current')
                                ]),
                         html.Tr([
                             html.Td(['Cumulative(from June 1)']),
                             html.Td(["N/A"], id='rf-cumulative')
                                ]),
                         html.Tr([
                             html.Td(['Cumulative over the Summer']),
                             html.Td(["N/A"], id='rf-cumulative-summer')
                                ]),
                         html.Tr([
                             html.Td(['Maximum in a day']),
                             html.Td(["N/A"], id='rf-max')
                                ])
                            ], className='dashboard-table')
                        ], className='hims-row1 card')
    return card

def plotCard(plot_id):
    card = dbc.Card(
                    html.Div([
                        dcc.Graph(id=plot_id),
                            ], id='hims-plot-div'),
                        className='hims-row2 card')
    return card

def generate_dashboard_rfms(stationID):

    dashboard = html.Div([
                        dbc.Row([
                            dbc.Col(gaugeCard(), width='3'),
                            dbc.Col(textCard(stationID), width=True)
                                ], className='hims-row'),
                        dbc.Row([
                            dbc.Col([plotCard('rfms-plot-single')]),
                            dbc.Col([plotCard('rfms-plot-cumulative')])
                                ], className='hims-row')
                        ])
    return dashboard

