import dash_bootstrap_components as dbc
from dash import html
from apps.Elements.Sidebar import sidebar



cardDeck = html.Div(
    [
        dbc.Card([
            dbc.CardImg(src="/assets/images/rain_1.jpg", top=True),
            dbc.CardHeader([
                html.H5("Rain Watch", className="card-title")
                            ]),
            dbc.CardBody([
                html.Blockquote(
                        "Rain Watch combines rainfall data from multiple sources, fills the gap in the existing system, invoking engagement through community sourced rainfall monitoring."
                        , className="card-text",
                    ),
                    dbc.Button(
                        "Launch", color="success", className="mt-auto", href='/apps/rfms'
                    ),
                ])
        ], className= 'home-card'),
        dbc.Card([
            dbc.CardImg(src="/assets/images/flood_1.jpg", top=True),
            dbc.CardHeader([
                html.H5("Flood Watch", className="card-title")
            ]),
            dbc.CardBody([
                html.Blockquote(
                    "Flood Watch combines river water levels, reservoir storage and spill and community sourced  groundwater monitoring systems.",
                    className="card-text",
                ),
                dbc.Button(
                    "Launch", color="success", className="mt-auto", href='/apps/gwms'
                ),
            ])
        ], className= 'home-card'),
        dbc.Card([
            dbc.CardImg(src="/assets/images/tide_1.jpg", top=True),
            dbc.CardHeader([
                html.H5("Tidal Watch", className="card-title")
            ]),
            dbc.CardBody([
                html.Blockquote(
                    "Tidal Watch leverages data from oceanographic and coastal spheres.",
                    className="card-text",
                ),
                dbc.Button(
                    "Launch", color="success", className="mt-auto", href='/apps/tdms', disabled=False
                ),
            ])
        ], className='home-card'),
    ], className='container')

layout = html.Div([
    html.H1(['RT-FMS'], id='main-title'),
    cardDeck
], id='container-home')