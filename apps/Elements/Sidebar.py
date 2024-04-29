import dash_bootstrap_components as dbc
from dash import html
# sidebar to web app
def sidebar():
    bar = html.Div(
        [
            html.Header(id='sidebar-header', children=[
                                    html.A([
                                        html.H2(id='heading', children=['CLIMATEWATCH'])
                                        ]),
                                    html.Div(id='sub-heading-div', children=[
                                        html.H4(id='sub-heading', children=None),
                                        dbc.DropdownMenu(
                                            id='main-menu',
                                            label = None,
                                            direction='down',
                                            # bs_size="md",
                                            right=True,
                                            color='#4646462E',
                                            children=[
                                                dbc.DropdownMenuItem("RainWatch", href='/apps/rfms', className='main-menu-items'),
                                                dbc.DropdownMenuItem("FloodWatch", href='/apps/gwms', className='main-menu-items'),
                                                dbc.DropdownMenuItem("TidalWatch", href='/apps/tdms', className='main-menu-items'),
                                                dbc.DropdownMenuItem("HeatWatch", href='/apps/hims', className='main-menu-items'),
                                                dbc.DropdownMenuItem("HazardWatch", href='/apps/hzms', className='main-menu-items'),
                                            ])
                                    ])
            ]),
            html.Div(id='sidebar-content', children=None),
            html.Footer(id='sidebar-footer', children=[
            html.A(id='logo-link', href='https://www.equinoct.com',
                       children=[html.Img(id='logo-img', src='/assets/logo/Equinoct_Logo.png')])
                ])
        ],
        id="sidebar"
    )
    return bar

