from dash import dcc, html
import pandas as pd
from datetime import datetime, timedelta

dataDF = pd.read_csv('Data/Rainfall.csv').set_index('TimeStamp')
endDate = dataDF.index.values[-1]

# sidebar to web app
def rfms_sidebar(legendColors, endDate=endDate):

    endDate = datetime.strptime(endDate, '%Y-%m-%d').date()
    startDate = endDate - timedelta(days=30)
    bar = html.Div(
        [
            html.H5(['Data Source']),
            dcc.RadioItems(id='data-source-rfms',
                           options=[
                               {'label': 'Others', 'value': 'OTH'},
                               {'label': 'Community', 'value': 'CS'},
                               {'label': 'All', 'value': 'All'}
                           ],
                           value='All',
                           labelStyle={'display': 'block'},
                           labelClassName='sidebar-labels'
                           ),
            html.H5(['Date']),
            dcc.DatePickerSingle(
                id='date-picker-rfms',
                min_date_allowed=startDate,
                max_date_allowed=endDate,
                display_format='DD-MM-YYYY',
                date=endDate
            ),
            html.H5(['Rainfall Status Legend [ in mm ]']),
            html.Table(children=[
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['no_data']}, className='dot')]),
                    html.Th(['No Data'], className='legend')
                ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['no_rf']}, className='dot')]),
                    html.Th(['No Rainfall [ ~0 ]'], className='legend')
                        ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['lyt_rf']}, className='dot')]),
                    html.Th(['Light Rainfall [ 0-15.5 ]'], className='legend')
                ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['mod_rf']}, className='dot')]),
                    html.Th(['Moderate Rainfall [ 15.5-64.5 ]'], className='legend')
                ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['hvy_rf']}, className='dot')]),
                    html.Th(['Heavy Rainfall [ 64.5-115.5 ]' ], className='legend')
                ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['vhvy_rf']}, className='dot')]),
                    html.Th(['Very Heavy Rainfall [ 115.5-204.5]'], className='legend')
                ]),
                html.Tr([
                    html.Th([html.Span(style={'background-color': legendColors['xtr_rf']}, className='dot')]),
                    html.Th(['Extreme Rainfall [ >204.5 ]'], className='legend')
                ])
            ])
        ],
        id="sidebar-rfms"
    )
    return bar
