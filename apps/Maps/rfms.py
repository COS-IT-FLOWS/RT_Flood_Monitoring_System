import geojson
from dash_extensions.javascript import Namespace, arrow_function
import dash_leaflet as dl
# Load river basins geojson to memory



def generate_map():
    def geojson_loader(filename):
        url = str('assets/shapefiles') + '/' + filename
        with open(url) as f:
            geojson_resource = geojson.load(f)
        return geojson_resource

    commStations_rsrc = geojson_loader('Rainfall_Stations.geojson')
    riverBasin_rsrc = geojson_loader('River_Basins.geojson')

    # station_filter = assign("function(feature, context){return context.props.hideout.Id == feature.properties.Id;}")

    layer_main = dl.TileLayer()

    CM_Space_Rainfall, Filter_Rainfall = Namespace("Markers", "customMarker_Rainfall"), Namespace("Filters", "customFilter_RFMS")

    #main map with properties such as geolocation and additional geojson layers
    map_main = dl.Map(id='map-rfms', center=[10, 76], zoom=9, children=[layer_main,
                    dl.LocateControl(id='geolocator', options={'locateOptions': {'enableHighAccuracy': True},
                                                               'position': 'topright'}),

                    dl.ScaleControl(position='bottomright'),
                    dl.LayersControl(position='topright'),

                    dl.GeoJSON(data=riverBasin_rsrc, id="river-basins-rfms", format='geojson', children=None,options=dict(color='#2C7C74'), zoomToBoundsOnClick=True,
                               hoverStyle=arrow_function(dict(weight=5, color='#666', dashArray=''))),
                    dl.GeoJSON(data=commStations_rsrc, id="stations-rfms", children=None,
                               options=dict(
                                   pointToLayer = CM_Space_Rainfall("pointToLayer"),
                                            filter=Filter_Rainfall("stationFilter")),
                               cluster=False, hideout=None)
                                                                    ],
                      zoomControl=True)
    return map_main