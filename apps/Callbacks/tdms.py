from dash.dependencies import Input, Output, State
from dash_extensions.enrich import Trigger
import pandas as pd
from datetime import date, datetime
from dash import html
from pathlib import Path
import plotly.express as px
import dash_leaflet as dl

from apps.Elements.colors import legendColors_rf

from apps.Callbacks.callbacks_manager import CallbackManager
callback_tdms = CallbackManager()


# **********************************************************************************************************************
# Callbacks for TDMS
# **********************************************************************************************************************

from apps.Dashboards.tdms import generate_dashboard_tdms

RSD_DF = pd.read_csv('Data/Tide/Tidal_RSD_Data.csv').set_index('Station_ID')
tidalData = RSD_DF['Tidal'].to_dict()
riverData = RSD_DF['2018'].to_dict()
for key in riverData:
    riverData[key] = riverData[key]*(100/300)
# Load stations within feature boundary(identified by property 'Id' of feature)
@callback_tdms.callback(
    [Output('stations-tdms', 'hideout'), Output('legend_1', 'children'), Output('legend_2', 'children'), Output('legend_3', 'children'), Output('legend_4', 'children'), Output('legend_5', 'children')],
    [Input('station-type-tdms', 'value')],
prevent_initial_call=True)
def display_stations_tdms(stationType):
    if stationType == 'TFI':
        data = tidalData
        legend  = ['0 - 25 cm', '25 - 50 cm', '50 - 75 cm', '75 - 90 cm', '> 90 cm']
    elif stationType == 'RFI':
        data = riverData
        legend  = ['0 - 75 cm', '75 - 150 cm', '150 - 225 cm', '225 - 270 cm', '> 270 cm']
    elif stationType == 'CTM':
        data = {}
        legend = ['0 - 75 cm', '75 - 150 cm', '150 - 225 cm', '225 - 270 cm', '> 270 cm']
    elif stationType == 'ATG':
        data = {}
        legend = ['0 - 75 cm', '75 - 150 cm', '150 - 225 cm', '225 - 270 cm', '> 270 cm']
    out = dict(station_type=stationType, data=data, legend_colors=legendColors_rf), legend[0], legend[1], legend[2], legend[3], legend[4]
    return out

# Display tooltips for stations
@callback_tdms.callback(
    Output('stations-tdms', 'children'),
    [Input('stations-tdms', 'hover_feature')],
prevent_initial_call=True)
def display_tooltip_station_tdms(feature):
    if feature is not None:
        stationID = feature['properties']['Station_ID']
        if 'RSD' in stationID:
            level2018 = RSD_DF.loc[stationID, '2018']
            levelTidal = RSD_DF.loc[stationID, 'Tidal']
            tooltip_data = html.Table([
                            html.Tr([
                                html.Th(['Station ID : '],className='tooltip-left'),
                                html.Th([stationID], className='tooltip-right')
                                ]),
                            html.Tr([
                                html.Th(['Highest Level during 2018 Floods : '], className='tooltip-left'),
                                html.Th([str(level2018 )+ ' cm'], className='tooltip-right')
                            ]),
                            html.Tr([
                                html.Th(['Highest Tidal Flood Level : '], className='tooltip-left'),
                                html.Th([str(levelTidal)+ ' cm'], className='tooltip-right')
                            ]),
                                ], id='tooltip-table')
            return dl.Tooltip([tooltip_data])
        elif 'TDS' in stationID:
            stationName = feature['properties']['Station_Name']
            tooltip_data = html.Table([
                html.Tr([
                    html.Th(['Station ID : '], className='tooltip-left'),
                    html.Th([stationID], className='tooltip-right')
                ]),
                html.Tr([
                    html.Th(['Station Name : '], className='tooltip-left'),
                    html.Th([stationName], className='tooltip-right')
                ]),
            ], id='tooltip-table')
        elif 'ATG' in stationID:
            stationName = feature['properties']['Station_Name']
            tooltip_data = html.Table([
                html.Tr([
                    html.Th(['Station ID : '], className='tooltip-left'),
                    html.Th([stationID], className='tooltip-right')
                ]),
                html.Tr([
                    html.Th(['Station Name : '], className='tooltip-left'),
                    html.Th([stationName], className='tooltip-right')
                ]),
            ], id='tooltip-table')
            return dl.Tooltip([tooltip_data])

@callback_tdms.callback(
    Output("date-tdms-div", "hidden"),
    [Input('station-type-tdms', 'value')],
prevent_initial_call=True)
def hide_date_div(stationType):
    if stationType != 'CTM':
        return True

tdmsPath = Path('Data/Tide/Station_ID')

# @callback_tdms.callback(
#     Output("plot-pane-tdms", "is_open"),
#     [Input('stations-tdms', 'click_feature')],
#     [State('station-type-tdms', 'value')],
# prevent_initial_call=True)
# def open_plot_pane(feature, stationType):
#     if stationType == 'CTM' and feature is not None:
#         return True

# @callback_tdms.callback(
#     Output("tdms-plot", "figure"),
#     [Trigger("plot-pane-tdms", "is_open"), Trigger('date-picker-tdms', 'date')],
#     [State("plot-pane-tdms", "is_open"), State('stations-tdms', 'click_feature'), State('date-picker-tdms', 'date')],
# prevent_initial_call=True)
# def display_plot_station_tdms(plotOpen, feature, dateStr):
#     if plotOpen:
#         dateStr = dateStr.split('T')[0]
#         stationID = feature['properties']['Station_ID']
#         stationName = feature['properties']['Station_Name']
#         df = pd.read_csv(tdmsPath/(stationID + '.csv'))
#         plotTitle = 'Station : ' + stationName + ' [' + stationID + ']  Date : ' + dateStr
#         try:
#             df = df[df['Current_Date'] == dateStr]
#             df = df[['DateTime', 'Data']]
#             df['DateTime'] = df['DateTime'].apply(lambda dateTime: datetime.strptime(dateTime, '%Y-%m-%d %H:%M:%S'))
#             plot = px.line(df, x='DateTime', y='Data',
#                            labels={
#                                'DateTime' : 'Date-Time [YYYY-MM-DD HH:MM:SS]',
#                                'Data' : 'Tidal Level [m above MSL]'
#                            })
#             plot.update_traces(line_color='rgba(132, 252, 41, 1)')
#         except:
#             plot = px.line()
#     else:
#         plot = px.line()
#         plotTitle = 'N/A'
#     plot.update_layout(
#         title=plotTitle,
#         plot_bgcolor='rgba(0, 0, 0, 0)',
#         paper_bgcolor='rgba(25, 45, 95, 0.92)',
#         font_family="monospace",
#         font_color="white",
#         title_font_family="monospace",
#         title_font_color="orange",
#     )
#     return plot

@callback_tdms.callback(
    [Output("collapsible", "is_open"), Output("dashboard", "children")],
    [Input('stations-tdms', 'click_feature')],
prevent_initial_call=True)
def open_dashboard(feature):
    if feature is not None:
        stationID = feature['properties']['Station_ID']
        return True, generate_dashboard_tdms(stationID)
    else:
        return False, None


# @callback_tdms.callback(
#     Output("plot-pane-tdms", "is_open"),
#     [Trigger("tdms-plot-close-button", "n_clicks")],
# prevent_initial_call=True)
# def close_plot_pane():
#     return False

@callback_tdms.callback(
    Output("collapsible", "is_open"),
    [Trigger("close-button", "n_clicks")],
prevent_initial_call=True)
def close_plot_pane():
    return False