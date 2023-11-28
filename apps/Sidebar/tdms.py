from dash import dcc, html
from datetime import datetime, timedelta

# sidebar to web app
def tdms_sidebar(legendColors):
    endDate = datetime.today()
    startDate = endDate - timedelta(days=30)
    bar = html.Div(
        [
            html.H5(['Type of Station']),
            dcc.RadioItems(id='station-type-tdms',
                           options=[
                               {'label': 'Tidal Flood Inundation', 'value': 'TFI'},
                               {'label': 'River Flood Inundation', 'value': 'RFI'},
                               {'label': 'Coastal Tidal Monitoring', 'value': 'CTM'},
                               {'label': 'Autonomous Tidal Stations', 'value': 'ATG'}
                           ],
                           value='ATG',
                           labelStyle={'display': 'block'},
                           labelClassName='sidebar-labels'
                           ),
            html.Div(id='date-tdms-div', children=[
                html.H5(['Date']),
                dcc.DatePickerSingle(
                    id='date-picker-tdms',
                    min_date_allowed=startDate,
                    max_date_allowed=endDate,
                    display_format='DD-MM-YYYY',
                    date=endDate
                )
                    ]),
            html.H5(['Flood Levels']),
            html.Table(children=[
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['no_data']}, className='dot')]),
                    html.Th(['No Data'], className='legend')
                ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['lyt_rf']}, className='dot')]),
                    html.Th(['0 - 25 cm'], className='legend', id='legend_1')
                        ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['mod_rf']}, className='dot')]),
                    html.Th(['25 - 50 cm'], className='legend', id='legend_2')
                ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['hvy_rf']}, className='dot')]),
                    html.Th(['50 - 75 cm' ], className='legend', id='legend_3')
                ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['vhvy_rf']}, className='dot')]),
                    html.Th(['75 - 90 cm'], className='legend', id='legend_4')
                ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['xtr_rf']}, className='dot')]),
                    html.Th([' > 90 cm'], className='legend', id='legend_5')
                ])
            ]),
        ],
        id="sidebar-tdms"
    )
    return bar
