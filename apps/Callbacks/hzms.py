from dash.dependencies import Input, Output, State
from dash_extensions.enrich import Trigger
import pandas as pd
from datetime import date, datetime
from dash import html
import plotly.express as px
from matplotlib import cm
import dash_leaflet as dl
import plotly.graph_objects as go
from dash import dcc
from apps.Maps.hzms import generate_map
from apps.Callbacks.callbacks_manager import CallbackManager

callback_hzms = CallbackManager()

# **********************************************************************************************************************
# Callbacks for HAZARD MS
# **********************************************************************************************************************



df = pd.read_csv('Data/Hazards/dataset.csv')
aqi_df = pd.read_csv('Data/Hazards/aqi_dataset.csv', index_col='Date')

map_main = generate_map()

# Display tooltips for stations
@callback_hzms.callback(
    [Output('hzms-graph', 'figure')],
    [Input('date-selector-hzms', 'value')],
prevent_initial_call=False)
def display_map_hzms(dateVal):
    if dateVal is not None:
        dateData = df[df['Date'] == dateVal]
        dateData_count = dateData.groupby(dateData.columns.tolist()).size().reset_index(drop=True)
        dateData = dateData.drop_duplicates().reset_index()
        dateData.loc[:, 'Count'] = dateData_count
        aqiData = aqi_df.loc[dateVal]
        aqiText = [f"AVG: <b>{aqiData['AVG_01']}</b><br>MAX: <b>{aqiData['MAX_01']}</b><br>MIN: <b>{aqiData['MIN_01']}</b>",
                   f"AVG: <b>{aqiData['AVG_02']}</b><br>MAX: <b>{aqiData['MAX_02']}</b><br>MIN: <b>{aqiData['MIN_02']}</b>"]
        figure=go.Figure(
            go.Scattermapbox(
                lat=dateData['latitude'],
                lon=dateData['longitude'],
                mode='markers',
                marker=dict(
                    size=dateData['Count']*15,
                    color=dateData['Color'],
                ),
                hoverlabel=dict(bgcolor='white',
                                font_size=16),
                opacity=0.8,
                text=dateData['Impact'],
                hovertext=dateData['Count'],
                hovertemplate="Impact Level : <b>%{text}</b>\
                <br>Number : <b>%{hovertext}</b><extra></extra>",
                # text = dateData['Alert_Level'],
                # values = dateData['Count']
            ),

            go.Layout(mapbox=dict(accesstoken='pk.eyJ1IjoiZGV2LWVxdWlub2N0IiwiYSI6ImNsZXdxZ2NmcDFjN2Y0NHMwbTQ4aXBvcTIifQ.mqUOGlCY3jHKLgJxfxV9lg',
                                  center=dict(lat=10.02, lon=76.31),
                                  zoom=11.1,
                                  ),
                      showlegend=False, width=1200, height=800
                      )
            )

        figure.add_trace(
            go.Scattermapbox(
                lat=[9.993325217084237],
                lon=[76.36340328685692],
                mode='markers',
                hoverlabel=dict(bgcolor='white',
                                font_size=16),
                text=['Brahmapuram Waste Management Facility'],
                hovertemplate='%{text}<extra></extra>',
                marker=dict(
                    size=25,
                    color='black',
                )
            )
        )
        figure.add_trace(
            go.Scattermapbox(
                lat=[9.97499779265068, 10.079712459157204],
                lon=[76.29467506759245, 76.30527693409658],
                mode='markers',
                hoverlabel=dict(bgcolor='white',
                                font_size=16),
                hovertext=['Vyttila', 'Eloor'],
                text= aqiText,
                marker=dict(
                    size=20,
                    color='blue',
                ),
                hovertemplate="%{hovertext} - PM2.5 Values<br>%{text}<extra></extra>"

            )
        )
        return figure

@callback_hzms.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@callback_hzms.callback(
    [Output("aqi-plot", "src"), Output("aqi-plot-pane", "is_open")],
    [Input("hzms-graph", "clickData"), ],
    [State("date-selector-hzms", "value")],
prevent_initial_call=True)
def display_aqi_plots(clickData, dateVal):
    if clickData['points'][0]['curveNumber'] == 2:
        pointIndex = clickData['points'][0]['pointIndex']
        fileLoc = f'/assets/images/aqi_station_imgs/{pointIndex}/{dateVal}.png'
        return fileLoc, True
    
@callback_hzms.callback(
    Output("aqi-plot-pane", "is_open"),
    [Trigger("close-button", "n_clicks")],
prevent_initial_call=True)
def close_plot_pane():
    return False