from dash.dependencies import Input, Output, State
from dash_extensions.enrich import Trigger
import pandas as pd
from datetime import date, datetime
from dash import html
import dash_leaflet as dl
#Import modules to send data to JS Script
import json

from apps.Elements.colors import legendColors_gw

from apps.Callbacks.callbacks_manager import CallbackManager
callback_gwms = CallbackManager()
# **********************************************************************************************************************
# Callbacks for GWMS
# **********************************************************************************************************************
riverStatic_df = pd.read_csv('Data/River/Static.csv')
riverStatic_df = riverStatic_df[riverStatic_df['Station_ID'].notna()]
riverStatic_df.set_index('Station_ID', inplace=True)
riverDynamic_df = pd.read_csv('Data/River/Dynamic.csv')
riverDynamic_df.set_index('Station_ID', inplace=True)

rsvrStatic_df = pd.read_csv('Data/Reservoir/Static.csv')
rsvrStatic_df = rsvrStatic_df[rsvrStatic_df['Station_ID'].notna()]
rsvrStatic_df.set_index('Station_ID', inplace=True)
rsvrDynamic_df = pd.read_csv('Data/Reservoir/Dynamic.csv')
rsvrDynamic_df.set_index('Station_ID', inplace=True)

gndWtrDynamic_df = pd.read_csv('Data/Ground_Water/Dynamic.csv')
gndWtrDynamic_df.set_index('TimeStamp', inplace=True)

storage_df = pd.read_csv('Data/GWMS_Dataset.csv')
storage_df.set_index('Station_ID', inplace=True)
storage_df = storage_df['Storage_Percent(%)'].to_dict()


# validStations = rsvrStatic_df.index.values.tolist() + riverStatic_df.index.values.tolist() + gndWtrDynamic_df.index.values.tolist()
# print(validStations)
# Load stations within feature boundary(identified by property 'Id' of feature)
@callback_gwms.callback(
    Output('stations-gwms', 'hideout'),
    [Input('river-basins-gwms', 'click_feature'), Trigger('station-type-gwms', 'value')],
    [State('station-type-gwms', 'value')],
prevent_initial_call=True)
def display_stations_gwms(feature, stationType):
    if feature is not None:
        id_value = feature['properties']['Id']
        out = {'Station_Storage' : storage_df,
               'Basin_ID' : str(id_value),
               'Station_Type' : stationType,
               'legend_colors' : legendColors_gw
               }
        print(out)
        out = json.loads(json.dumps(out))
        return out

@callback_gwms.callback(
    Output('regulator-gwms', 'hideout'),
    [Input('river-basins-gwms', 'click_feature'), Trigger('station-type-gwms', 'value')],
    [State('station-type-gwms', 'value')],
prevent_initial_call=True)
def display_stations_gwms(feature, stationType):
    if feature is not None:
        id_value = feature['properties']['Id']
        out = {'Station_Storage' : storage_df,
               'Basin_ID' : str(id_value),
               'Station_Type' : stationType,
               'legend_colors' : legendColors_gw
               }
        out = json.loads(json.dumps(out))
        return out

# Display tooltips for river basin
@callback_gwms.callback(
    Output('river-basins-gwms', 'children'),
    [Input('river-basins-gwms', 'hover_feature')],
prevent_initial_call=True)
def display_tooltip(feature):
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

# Display tooltips for river stations
@callback_gwms.callback(
    Output('stations-gwms', 'children'),
    [Input('stations-gwms', 'click_feature')],
prevent_initial_call=True)
def display_tooltip_river(feature):
    if feature is not None:
        stationID = feature['properties']['Station_ID']
        stationName = feature['properties']['Station_Name']
        print(stationID, stationName)
        if stationID in riverDynamic_df.index.values:
            timeStamp = datetime.strptime(riverDynamic_df.loc[stationID, 'TimeStamp'], '%d-%m-%Y_%H')
            warningLevel = round(riverStatic_df.loc[stationID, 'Warning_Level(m)'], 2)
            currentLevel = round(riverDynamic_df.loc[stationID, 'Level(m)'], 2)
            tooltip_data = html.Table([
                        html.Tr([
                            html.Th(['Station : '], className='tooltip-left'),
                            html.Th([stationID], className='tooltip-right')
                        ]),
                        html.Tr([
                            html.Th(['Warning Level(m): '], className='tooltip-left'),
                            html.Th([warningLevel], className='tooltip-right')
                        ]),
                        html.Tr([
                            html.Th(['Current Level(m): '], className='tooltip-left'),
                            html.Th([currentLevel], className='tooltip-right')
                        ]),
                        html.Tr([
                            html.Th(['Timestamp: '], className='tooltip-left'),
                            html.Th([timeStamp], className='tooltip-right')
                        ]),
                    ], id='tooltip-table')
        elif stationID in rsvrDynamic_df.index.values:
            timeStamp = datetime.strptime(rsvrDynamic_df.loc[stationID, 'TimeStamp'], '%Y-%m-%d')
            currentStorage = rsvrDynamic_df.loc[stationID, 'Storage_Percent(%)']
            spill = rsvrDynamic_df.loc[stationID, 'Spill(m^3/s)']
            tooltip_data = html.Table([
                html.Tr([
                    html.Th(['Station : '], className='tooltip-left'),
                    html.Th([stationName], className='tooltip-right')
                ]),
                html.Tr([
                    html.Th(['Storage(%) : '], className='tooltip-left'),
                    html.Th([currentStorage], className='tooltip-right')
                ]),
                html.Tr([
                    html.Th(['Spill(m^3/s) : '], className='tooltip-left'),
                    html.Th([spill], className='tooltip-right')
                ]),
                html.Tr([
                    html.Th(['Timestamp: '], className='tooltip-left'),
                    html.Th([timeStamp], className='tooltip-right')
                ]),
            ], id='tooltip-table')
        elif stationID in gndWtrDynamic_df.columns.values:
            timeStr = gndWtrDynamic_df[stationID].index.values[-1]
            timeStamp = datetime.strptime(timeStr, '%Y-%m-%d')
            currentLevel = gndWtrDynamic_df.loc[timeStr, stationID]
            tooltip_data = html.Table([
                html.Tr([
                    html.Th(['Station : '], className='tooltip-left'),
                    html.Th([stationID], className='tooltip-right')
                ]),
                html.Tr([
                    html.Th(['Level(m) : '], className='tooltip-left'),
                    html.Th([currentLevel], className='tooltip-right')
                ]),
                html.Tr([
                    html.Td(['Timestamp : '], className='tooltip-left'),
                    html.Td([timeStamp], className='tooltip-right')
                ]),
            ], id='tooltip-table')
        else:
            tooltip_data = html.Table([
                        html.Tr([
                            html.Th(['Station ID : '], className='tooltip-left'),
                            html.Th([stationID], className='tooltip-right')
                        ]),
                        html.Tr([
                            html.Th(['Station : '], className='tooltip-left'),
                            html.Th([stationName], className='tooltip-right')
                        ]),
                        html.Tr([
                            html.Th(['No Data'], colSpan=2, className='tooltip-row')
                        ]),
                    ], id='tooltip-table')
        return dl.Popup([tooltip_data])

# Display tooltips for river stations
@callback_gwms.callback(
    Output('regulator-gwms', 'children'),
    [Input('regulator-gwms', 'click_feature')],
prevent_initial_call=True)
def display_tooltip_river(feature):
    if feature is not None:
        # stationID = feature['properties']['Station_ID']
        stationName = feature['properties']['Station_Name']
        tooltip_data = html.Table([
                    html.Tr([
                        html.Th(['Station: '], className='tooltip-left'),
                        html.Th([stationName], className='tooltip-right')
                    ]),
                    html.Tr([
                        html.Th(['No Data'], colSpan=2, className='tooltip-row')
                    ]),
                ], id='tooltip-table')
        return dl.Popup([tooltip_data])