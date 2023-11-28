import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import confuse
from apps.Lib.db_connector import DB_Connector
import plotly.express as px

def gaugeCard():
    card = dbc.Card([
                    dbc.CardBody([
                        html.Img(id='gauge-img', src="/assets/icons/tidal_station.svg", alt="Tidal Station", width='100%')
                                ]),
                    ], className='row1 card')
    return card

def textCard(stationID):
    card = dbc.Card([
                dbc.Table([
                         html.Tr([
                             html.Td(['Station'], colSpan=2),
                             html.Td([stationID], id='stationID')
                                ]),
                         html.Tr([
                             html.Td(['Tidal Level'], rowSpan=5),
                             html.Td(['Highest']),
                             html.Td(["N/A"], id='td-max')
                                ]),
                         html.Tr([
                             html.Td(['Lowest']),
                             html.Td(["N/A"], id='td-min')
                                ]),
                         html.Tr([
                             html.Td(['Current']),
                             html.Td(["N/A"], id='td-current')
                                ]),
                         html.Tr([
                             html.Td(["Today's Highest"]),
                             html.Td(["N/A"], id='td-max-today')
                                 ]),
                         html.Tr([
                             html.Td(["Today's Lowest"]),
                             html.Td(["N/A"], id='td-min-today')
                                ])
                            ], className='dashboard-table')
                        ], className='row1 card')
    return card

def generate_plot(ds):
    fig = px.scatter(ds, x=ds.index, y=ds.name,
                     labels={
                        "timestamp_station": "Time",
                        "depth": "Depth(cm)",
                        "temperature_ambient": "Temperature(deg.C)",
                        "temperature_water": "Temperature(deg.C)",
                        "ph" : "pH",
                        "humidity": "Humidity(%)"
                     },
                     title=ds.name.upper())

    fig.update_layout(showlegend=False,
                      title_x=0.5,
                      paper_bgcolor='rgba(0, 0, 0, 0)',
                      plot_bgcolor='#ffffff',
                      yaxis_gridcolor='grey',
                      xaxis_gridcolor='grey'
                      )
    return fig

def plotCard(ds, plot_id):
    card = dbc.Card(
                    html.Div([
                        dcc.Graph(figure=generate_plot(ds.tail(200)),
                        config = {
                                     'displayModeBar': False
                                 }
                        , id=plot_id)
                            ], id='plot-div'),
                        className='row2 dash-card')
    return card

source = confuse.YamlSource('config.yaml')
config = confuse.RootView([source])
dbAuth = config['database'].get()



def generate_dashboard_tdms(stationID):
    df = DB_Connector().get_data('station', 'timestamp_station')
    df.drop('timestamp_broker', axis=1, inplace=True)

    if 'ATG' in stationID:
        dashboard = html.Div([
                                dbc.Row([
                                    dbc.Col([plotCard(df['depth'], 'depth')]),
                                ]),
                                dbc.Row([
                                        dbc.Col([plotCard(df['temperature_ambient'], 'temperature_ambient')]),
                                        dbc.Col([plotCard(df['temperature_water'], 'temperature_water')])
                                ]),
                                dbc.Row([
                                        dbc.Col([plotCard(df['humidity'], 'humidity')]),
                                        dbc.Col([plotCard(df['ph'], 'ph')])
                                ])
                            ])
    else:
        dashboard = html.Div([
                            dbc.Row([
                                dbc.Col(gaugeCard(), width='3'),
                                dbc.Col(textCard(stationID), width=True)
                                    ], className='row'),
                            dbc.Row([
                                dbc.Col([plotCard('current-plot')])
                                    ], className='row'),
                            dbc.Row([
                                dbc.Col([plotCard('long-term-plot')])
                            ], className='row')
                            ])
    return dashboard

