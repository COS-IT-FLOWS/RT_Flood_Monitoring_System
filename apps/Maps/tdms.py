import geojson
import dash_leaflet as dl
from dash_extensions.javascript import Namespace
# Load river basins geojson to memory



def generate_map():
    def geojson_loader(filename):
        url = str('assets/shapefiles') + '/' + filename
        with open(url) as f:
            geojson_resource = geojson.load(f)
        return geojson_resource

    tidalStations = geojson_loader('TDMS_Stations.geojson')

    layer_main = dl.TileLayer()

    CM_Space, Filter = Namespace("Markers", "customMarker_TDMS"), Namespace("Filters", "customFilter_TDMS")

    #main map with properties such as geolocation and additional geojson layers
    map_main = dl.Map(id='map-tdms', center=[10.1973, 76.216], zoom=6, children=[layer_main,
                    dl.LocateControl(id='geolocator', options={'locateOptions': {'enableHighAccuracy': True},
                                                               'position': 'topright'}),

                    dl.ScaleControl(position='bottomright'),
                    dl.LayersControl(position='topright'),

                    dl.GeoJSON(data=tidalStations, id="stations-tdms", children=None,
                               options=dict(
                                            pointToLayer=CM_Space("pointToLayer"),
                                             filter=Filter("stationFilter")),
                                             cluster=False, hideout=None),
                                                 ],
                      zoomControl=True)
    return map_main