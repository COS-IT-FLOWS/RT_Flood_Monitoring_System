from dash import dcc, html
from datetime import datetime

# sidebar to web app
def gwms_sidebar(legendColors):

    endDate = datetime(2023, 11, 27)

    bar = html.Div(
        [
            html.H5(['Last Updated on:'], className='content-header'),
            dcc.DatePickerSingle(
                id='date-picker-gwms',
                min_date_allowed=endDate,
                max_date_allowed=endDate,
                display_format='DD-MM-YYYY',
                date=endDate
            ),
            html.H5(['Storage [%]'], className='content-header'),
            html.Table(children=[
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['no_data']}, className='dot')]),
                    html.Th(['No Data'], className='legend')
                ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['val0_25']}, className='dot')]),
                    html.Th(['0% - 25%'], className='legend')
                ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['val25_50']}, className='dot')]),
                    html.Th(['25% - 50%'], className='legend')
                ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['val50_75']}, className='dot')]),
                    html.Th(['50% - 75%'], className='legend')
                ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['val75_90']}, className='dot')]),
                    html.Th(['75% - 90%'], className='legend')
                ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['val90_100']}, className='dot')]),
                    html.Th(['90% - 100%'], className='legend')
                ]),
            ]),
            html.H5(['Station Type'], className='content-header'),
            dcc.RadioItems(id='station-type-gwms',
                           options=[
                               {'label': 'River Stations', 'value': 'CWCRV'},
                               {'label': 'Reservoir Stations', 'value': 'RSVR'},
                               {'label': 'Ground Water Stations', 'value': 'CSGW'},
                               {'label': 'All Stations', 'value': 'All'}
                           ],
                           value='All',
                           labelStyle={'display': 'block'},
                           labelClassName='sidebar-labels'
                           ),
        ],
        id="sidebar-gwms"
    )
    return bar
