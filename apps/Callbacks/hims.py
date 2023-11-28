from dash.dependencies import Input, Output, State
from dash_extensions.enrich import Trigger
import pandas as pd
from datetime import date, datetime
from dash import html
import plotly.express as px
from matplotlib import cm
import dash_leaflet as dl
import confuse
from math import sqrt
from apps.Callbacks.callbacks_manager import CallbackManager

from apps.Lib.db_connector import DB_Connector

callback_hims = CallbackManager()

source = confuse.YamlSource('config.yaml')
config = confuse.RootView([source])
dbAuth = config['Database'].get()
HI_DF = DB_Connector().get_data('imd_awstation_data', 'time')
HI_DF = HI_DF[HI_DF.index == HI_DF.index[-1]]
HI_DF = HI_DF[['station_id', 'temperature', 'relative_humidity']]
HI_DF.set_index('station_id', inplace=True)


def degC_degF_converter(degC_temp):
    degF_temp = (degC_temp * 1.8) + 32
    return degF_temp

def degF_degC_converter(degF_temp):
    degC_temp = (degF_temp - 32) / 1.8
    return degC_temp
# Rothfusz - NOAA HI Formula

def noaa_hi_complex(ta_f, rh):
    complexHI = -42.379 + 2.04901523 * ta_f + 10.14333127 * rh - 0.22475541 * ta_f * rh - 0.00683783 * (
                ta_f ** 2) - 0.05481717 * (rh ** 2) + 0.00122874 * (ta_f ** 2) * rh + 0.00085282 * ta_f * (
                            rh ** 2) - 0.00000199 * ((ta_f * rh) ** 2)

    if rh < 13 and 80 < ta_f < 112:
        adjustment = ((13 - rh) / 4) * sqrt((17 - abs(ta_f - 95.)) / 17)
        complexHI = complexHI - adjustment
        return complexHI

    if rh > 85 and 80 < ta_f < 87:
        adjustment = ((rh - 85) / 10) * ((87 - ta_f) / 5)
        complexHI = complexHI + adjustment
        return complexHI

    return complexHI

def noaa_hi(ta, rh):
    # Convert Temperature from deg Celsius to Fahrenheit
    ta_f = degC_degF_converter(ta)

    simpleHI = 0.5 * (ta_f + 61.0 + ((ta_f - 68.0) * 1.2) + (rh * 0.094))

    avg_hi_ta = (simpleHI + ta_f) / 2

    if avg_hi_ta < 80:

        outputHI = simpleHI

    else:

        outputHI = noaa_hi_complex(ta_f, rh)

    outputHI = degF_degC_converter(outputHI)
    return outputHI
# **********************************************************************************************************************
# Callbacks for HIMS
# **********************************************************************************************************************

from apps.Dashboards.hims import generate_dashboard_hims

# HI_DF = pd.read_csv('Data/Heat_Index/Summary.csv', index_col='Station_ID')
cmap = cm.get_cmap("YlOrRd")
HI_DF['Heat_Index'] = HI_DF.apply(lambda x: noaa_hi(x['temperature'], x['relative_humidity']), axis=1)
HI_DF['HI_to1'] = HI_DF['Heat_Index']/HI_DF['Heat_Index'].max()
HI_DF['colors'] = HI_DF['HI_to1'].apply(lambda x: cmap(x))
HI_DF['colors'] = HI_DF['colors'].apply(lambda x: 'rgba(' + str(x[0]*255) + ', ' + str(x[1]*255) + ', ' + str(x[2]*255) + ', ' + str(x[3]) + ')')
hiColors = HI_DF['colors'].to_dict()

@callback_hims.callback(
    [Output('stations-hims', 'hideout')],
    [Trigger('station-type-hims', 'value')],
prevent_initial_call=True)
def display_stations_hims():
    return hiColors

# Display tooltips for stations
@callback_hims.callback(
    Output('stations-hims', 'children'),
    [Input('stations-hims', 'hover_feature')],
prevent_initial_call=True)
def display_tooltip_station_hims(feature):
    if feature is not None:
        stationID = feature['properties']['station_id']
        heatIndex = round(HI_DF.loc[stationID, 'Heat_Index'], 2)
        if pd.isna(heatIndex):
            heatIndex = 'N/A'
        tooltip_data = html.Table([
                        html.Tr([
                            html.Th(['Station ID : '],className='tooltip-left'),
                            html.Th([stationID], className='tooltip-right')
                            ]),
                        html.Tr([
                            html.Th(['Heat Index:'], className='tooltip-left'),
                            html.Th([heatIndex], className='tooltip-right')
                        ])
                            ], id='tooltip-table')
        return dl.Tooltip([tooltip_data])

# @callback_hims.callback(
#     [Output("collapsible", "is_open"), Output("dashboard", "children")],
#     [Input('stations-hims', 'click_feature')],
# prevent_initial_call=True)
# def open_plot_pane(feature):
#     if feature is not None:
#         stationID = feature['properties']['station_id']
#         return True, generate_dashboard_hims(stationID)
#     else:
#         return False, None
#
# @callback_hims.callback(
#     [Output("hims-plot", "figure"), Output('hi-current', 'children')],
#     [Input('stations-hims', 'click_feature')],
# prevent_initial_call=True)
# def display_graph(feature):
#     if feature is not None:
#         stationID = feature['properties']['station_id']
#         fileName = stationID + '.csv'
#         df = pd.read_csv('Data/Heat_Index/Dynamic' + '/' + fileName, index_col='DateTime')
#         fig = px.line(df, x=df.index, y=['Heat_Index', 'Temperature(degC)'])
#         fig.update_layout({
#                             'plot_bgcolor': 'lightblue',
#                             'paper_bgcolor': 'lightblue'
#                           })
#         fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='black')
#         fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='black')
#
#         hi_current = df[df['Heat_Index'].notna()].tail(1)['Heat_Index']
#         hi_text = str(round(hi_current.values[0], 2)) + ' last updated at ' + str(datetime.strptime(hi_current.index.values[0], '%Y-%m-%d %H:%M:%S').ctime())
#
#         return fig, hi_text
#
# @callback_hims.callback(
#     Output("collapsible", "is_open"),
#     [Trigger("close-button", "n_clicks")],
# prevent_initial_call=True)
# def close_plot_pane():
#     return False
