import geojson
from dash_extensions.javascript import Namespace, arrow_function
import dash_leaflet as dl
# Load river basins geojson to memory



def generate_map():
    def geojson_loader(filename):
        url = str('assets/shapefiles') + '/' + filename
        with open(url) as f:
            geoRsrc = geojson.load(f)
        return geoRsrc

    groundWater_rsrc = geojson_loader('GroundWater_Stations.geojson')
    regulator_rsrc = geojson_loader('Regulator_Stations.geojson')
    riverBasin_rsrc = geojson_loader('River_Basins.geojson')


    layer_main = dl.TileLayer()

    Filter_GWMS = Namespace("Filters", "customFilter_GWMS")
    CMSpace_GWMS = Namespace("Markers", "customMarker_GWMS")

    #main map with properties such as geolocation and additional geojson layers
    map_main = dl.Map(id='map-gwms', center=[10, 76], zoom=9, children=[layer_main,
                    dl.LocateControl(id='geolocator', options={'locateOptions': {'enableHighAccuracy': True},
                                                               'position': 'topright'}),

                    dl.ScaleControl(position='bottomright'),
                    dl.LayersControl(position='topright'),

                    dl.GeoJSON(data=riverBasin_rsrc, id="river-basins-gwms", format='geojson', children=None,options=dict(color='#2C7C74'), zoomToBoundsOnClick=True,
                               hoverStyle=arrow_function(dict(weight=5, color='#666', dashArray=''))),
                    dl.GeoJSON(data=groundWater_rsrc, id="stations-gwms", cluster=False, children=None,
                               options=dict(
                                   pointToLayer=CMSpace_GWMS("pointToLayer"),
                                   filter=Filter_GWMS("stationFilter")),
                               hideout=None),
                    dl.GeoJSON(data=regulator_rsrc, id="regulator-gwms", cluster=False, children=None,
                               options=dict(
                                   pointToLayer=CMSpace_GWMS("pointToLayer"),
                                   filter=Filter_GWMS("stationFilter")),
                               hideout=None)
                                                                        ],
                      zoomControl=True)
    return map_main