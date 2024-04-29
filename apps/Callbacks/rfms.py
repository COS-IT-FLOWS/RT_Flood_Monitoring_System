from dash.dependencies import Input, Output, State
from dash_extensions.enrich import Trigger
from datetime import date, datetime
from dash import html
import dash_leaflet as dl
import pandas as pd
import math
from apps.Elements.colors import  legendColors_rf
from apps.Lib.db_connector import DB_Connector
from apps.Callbacks.callbacks_manager import CallbackManager
import confuse

callback_rfms = CallbackManager()



source = confuse.YamlSource('config.yaml')
config = confuse.RootView([source])
dbAuth = config['database'].get()
dataDF = DB_Connector().get_data('rainfall_data', 'TimeStamp')
# **********************************************************************************************************************
# Callbacks for RFMS
# **********************************************************************************************************************

# Load stations within feature boundary(identified by property 'Id' of feature)
@callback_rfms.callback(
    Output('stations-rfms', 'hideout'),
    [Trigger('data-source-rfms', 'value'), Trigger('date-picker-rfms', 'date')],
    [State('data-source-rfms', 'value'),  State('date-picker-rfms', 'date')],
prevent_initial_call=True)
def display_stations_rfms(data_source, dateVal):
    dateVal = date.fromisoformat(dateVal)
    dateStr = dateVal.strftime('%Y-%m-%d')
    dateDF = dataDF.loc[dateStr].to_dict()
    out = dict(dt_source=data_source, date_data=dateDF, legend_colors=legendColors_rf)
    return out

# Display tooltips for river basin
@callback_rfms.callback(
    Output('river-basins-rfms', 'children'),
    [Input('river-basins-rfms', 'hover_feature')],
prevent_initial_call=True)
def display_tooltip_rfms(feature):
    if feature is not None:
        properties = feature['properties']
        if properties['Name_river'] is not None:
            name = properties['Name_river']
        elif properties['name_est'] is not None:
            name = properties['name_est']
        elif properties['Type'] is not None:
            name = properties['Type']
        else:
            name = 'null'
        return dl.Tooltip([name])
    return None

# Display tooltips for stations
@callback_rfms.callback(
    Output('stations-rfms', 'children'),
    [Input('stations-rfms', 'hover_feature')],
    [State('date-picker-rfms', 'date')],
prevent_initial_call=True)
def display_tooltip_station_rfms(feature, dateVal):
    if feature is not None:
        stationID = feature['properties']['Station_ID']
        dateVal = date.fromisoformat(dateVal)
        dateStr = dateVal.strftime('%Y-%m-%d')
        rainfall = dataDF.loc[dateStr, stationID]
        print(stationID, rainfall)
        if math.isnan(rainfall):
            rainfall = 'N/A'
        else:
            rainfall = str(rainfall) + ' mm'
        if 'IMD' in stationID:
            name = stationID.replace('IMDRF', 'OTHRF')
        elif 'RSVR' in stationID:
            name = stationID.replace('RSVR', 'OTHRS')
        elif 'CWCRF' in stationID:
            name = stationID.replace('CWCRF', 'OTHRV')
        else:
            name = stationID
        tooltip_data = html.Table([
                            html.Tr([
                                html.Th(['Station ID : '],className='tooltip-left'),
                                html.Th([name], className='tooltip-right')
                                ]),
                            html.Tr([
                                html.Th(['Rainfall : '], className='tooltip-left'),
                                html.Th([rainfall], className='tooltip-right')
                                ]),
                                ], id='tooltip-table')
        return dl.Tooltip([tooltip_data])


# # Display Data as of date
# @callback_rfms.callback(
#     Output('community-stations', 'options'),
#     [Input('date-dropdown', 'value')],
# prevent_initial_call=True)
# def display_data_of_date(date):
#     print(df.loc[date])