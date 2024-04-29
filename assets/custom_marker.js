window.Markers = Object.assign({}, window.Markers, {
    customMarker_Rainfall: {
        pointToLayer: function(feature, latlng, context) {

            let iconUrl, id, color;
            let stationID = feature['properties']['Station_ID'];
            if (stationID.includes('IMD'))
                {
                iconUrl = '/assets/icons/rainfall_station.png';
                stn_id = 'IMDRF';
                }
            else if (stationID.includes('CSRF'))
                {
                iconUrl = '/assets/icons/comm_rainfall_station.png';
                stn_id = 'CSRF';
                }
            else if (stationID.includes('CWCRF'))
                {
                iconUrl = '/assets/icons/rainfall_station.png';
                stn_id = 'CWCRF';
                }
            else if (stationID.includes('RSVR'))
                {
                iconUrl = '/assets/icons/rainfall_station.png';
                stn_id = 'RSVR';
                };




            let data = context.props.hideout.date_data;
            let legendColors = context.props.hideout.legend_colors;
            value = data[stationID];

            if (value == 0) {
                color = legendColors['no_rf'];
            } else if (value > 0 && value <= 15.5) {
                color = legendColors['lyt_rf'];
            } else if (value > 15.5 && value <= 64.5) {
                color = legendColors['mod_rf'];
            } else if (value > 64.5 && value <= 115.5) {
                color = legendColors['hvy_rf'];
            } else if (value > 115.5 && value <= 204.5) {
                color = legendColors['vhvy_rf'];
            } else if (value > 204.5) {
                color = legendColors['xtr_rf'];
            } else {
                color = legendColors['no_data'];
            };


            const iconSettings = {
		        mapIconUrl: '<svg version="1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 149 178">'
		                  + '<path fill="{mapIconColor}" stroke="#FFF" '
		                  + 'stroke-width="6" stroke-miterlimit="10" '
		                  + 'd="M126 23l-6-6A69 69 0 0 0 74 1a69 69 0 0 0-51 22A70 70 0 0 0 1 74c0 21 7 38 '
		                  + '22 52l43 47c6 6 11 6 16 0l48-51c12-13 18-29 18-48 0-20-8-37-22-51z"/>'
//		                  + '<circle fill="{mapIconColorInnerCircle}" cx="74" cy="75" r="61"/>'
		                  + '<defs><pattern id="{stationMarkerId}" height="100%" width="100%" viewBox="0 0 100 100">'
                          + '<image width="100" height="100" xlink:href="{stationIconUrl}"/>'
		                  + '</pattern></defs>'
		                  + '<circle fill="{mapIconColorInnerCircle}" cx="74" cy="75" r="57"/>'
		                  + '<circle fill="url(#{stationMarkerId})" cx="74" cy="75" r="50"/>'
		                  + '</svg>',
		        mapIconColor: color,
		        mapIconColorInnerCircle: '#ffffff',
		        stationIconUrl: iconUrl,
		        stationMarkerId: stn_id
	        };

            // icon normal state
            const divIcon = L.divIcon({
              className: "leaflet-data-marker",
              html: L.Util.template(iconSettings.mapIconUrl, iconSettings), //.replace('#','%23'),
              iconAnchor  : [12, 32],
              iconSize    : [45, 50],
              popupAnchor : [0, -28]
            });

            outIcon = new L.Marker(latlng, {icon: divIcon});
            return outIcon;
        }
    },

    customMarker_GWMS: {
        pointToLayer: function(feature, latlng, context) {
            let iconUrl, stnID;
            let stationID = feature['properties']['Station_ID'];
            let sizeIcon = [49.5, 55];

            if (stationID.includes('CWCRV'))
                {
                    iconUrl = '/assets/icons/river_station.png';
                    stnID = 'CWCRV';
                }
            else if (stationID.includes('RSVR'))
                {
                    iconUrl = '/assets/icons/reservoir_station.png';
                    stnID = 'RSVR';
                }
            else if (stationID.includes('CSGW'))
                {
                    iconUrl = '/assets/icons/well_station.png';
                    stnID = 'CSGW';
                }
            else if (stationID.includes('RGLTR'))
                {
                    iconUrl = '/assets/icons/regulator_station.png';
                    stnID = 'RGLTR';
                    sizeIcon = [36, 40];
                };

            let data = context.props.hideout.Station_Storage;
            let legendColors = context.props.hideout.legend_colors;
            let value = data[stationID];
            let color = legendColors['no_data'];



            if (value >= 0 && value <= 25) {
                color = legendColors['val0_25'];
            } else if (value > 25 && value <= 50) {
                color = legendColors['val25_50'];
            } else if (value > 50 && value <= 75) {
                color = legendColors['val50_75'];
            } else if (value > 75 && value <= 90) {
                color = legendColors['val75_90'];
            } else if (value > 90) {
                color = legendColors['val90_100'];
            };

            var iconSettings = {
		        mapIconUrl: '<svg version="1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 149 178">'
		                  + '<path fill="{mapIconColor}" stroke="#FFF" '
		                  + 'stroke-width="6" stroke-miterlimit="10" '
		                  + 'd="M126 23l-6-6A69 69 0 0 0 74 1a69 69 0 0 0-51 22A70 70 0 0 0 1 74c0 21 7 38 '
		                  + '22 52l43 47c6 6 11 6 16 0l48-51c12-13 18-29 18-48 0-20-8-37-22-51z"/>'
//		                  + '<circle fill="{mapIconColorInnerCircle}" cx="74" cy="75" r="61"/>'
		                  + '<defs><pattern id="{stationMarkerId}" height="100%" width="100%" viewBox="0 0 100 100">'
                          + '<image width="100" height="100" xlink:href="{stationIconUrl}"/>'
		                  + '</pattern></defs>'
		                  + '<circle fill="{mapIconColorInnerCircle}" cx="74" cy="75" r="57"/>'
		                  + '<circle fill="url(#{stationMarkerId})" cx="74" cy="75" r="50"/>'
		                  + '</svg>',
		        mapIconColor: color,
		        mapIconColorInnerCircle: '#ffffff',
		        stationIconUrl: iconUrl,
		        stationMarkerId: stnID
	        };

            // icon normal state
            const divIcon = L.divIcon({
              className: "leaflet-data-marker",
              html: L.Util.template(iconSettings.mapIconUrl, iconSettings), //.replace('#','%23'),
              iconAnchor  : [12, 32],
              iconSize    : sizeIcon,
              popupAnchor : [0, -28]
            });

            outIcon = new L.Marker(latlng, {icon: divIcon});
            return outIcon;
        }
    },

    customMarker_TDMS: {
        pointToLayer: function(feature, latlng, context) {
            let color;
            let iconUrl, stnID;
            let stationID = feature['properties']['Station_ID'];
            let sizeIcon = [49.5, 55];

            if (stationID.includes('RSD'))
                {
                    iconUrl = '/assets/icons/tidal_station.png';
                    stnID = 'RSD';
                }
            else if (stationID.includes('TDS'))
                {
                    iconUrl = '/assets/icons/tidal_station.png';
                    stnID = 'TDS';
                }
            else if (stationID.includes('ATG'))
                {
                    iconUrl = '/assets/icons/auto_tidal_gauge.png';
                    stnID = 'ATG';
                    sizeIcon = [65, 70];
                }

            let data = context.props.hideout.data;
            let legendColors = context.props.hideout.legend_colors;
            value = data[stationID];
            if (value == 0) {
                color = legendColors['no_data'];
            } else if (value > 0 && value <= 25) {
                color = legendColors['lyt_rf'];
            } else if (value > 25 && value <= 50) {
                color = legendColors['mod_rf'];
            } else if (value > 50 && value <= 75) {
                color = legendColors['hvy_rf'];
            } else if (value > 75 && value <= 90) {
                color = legendColors['vhvy_rf'];
            } else if (value > 90) {
                color = legendColors['xtr_rf'];
            } else {
                color = legendColors['no_data'];
            };

            const iconSettings = {
		        mapIconUrl: '<svg version="1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 149 178">'
		                  + '<path fill="{mapIconColor}" stroke="#FFF" '
		                  + 'stroke-width="6" stroke-miterlimit="10" '
		                  + 'd="M126 23l-6-6A69 69 0 0 0 74 1a69 69 0 0 0-51 22A70 70 0 0 0 1 74c0 21 7 38 '
		                  + '22 52l43 47c6 6 11 6 16 0l48-51c12-13 18-29 18-48 0-20-8-37-22-51z"/>'
//		                  + '<circle fill="{mapIconColorInnerCircle}" cx="74" cy="75" r="61"/>'
		                  + '<defs><pattern id="{stationMarkerId}" height="100%" width="100%" viewBox="0 0 100 100">'
                          + '<image width="100" height="100" xlink:href="{stationIconUrl}"/>'
		                  + '</pattern></defs>'
		                  + '<circle fill="{mapIconColorInnerCircle}" cx="74" cy="75" r="57"/>'
		                  + '<circle fill="url(#{stationMarkerId})" cx="74" cy="75" r="50"/>'
		                  + '</svg>',
		        mapIconColor: color,
		        mapIconColorInnerCircle: '#ffffff',
		        stationIconUrl: iconUrl,
		        stationMarkerId: stnID
	        };

            // icon normal state
            const divIcon = L.divIcon({
              className: "leaflet-data-marker",
              html: L.Util.template(iconSettings.mapIconUrl, iconSettings), //.replace('#','%23'),
              iconAnchor  : [12, 32],
              iconSize    : sizeIcon,
              popupAnchor : [0, -28]
            });

            outIcon = new L.Marker(latlng, {icon: divIcon});
            return outIcon;
        }
    },

    customMarker_HIMS: {
        pointToLayer: function(feature, latlng, context) {
            let stn_id='HIS';
            let iconUrl = '/assets/icons/heat_station.png';
            let stationID = feature['properties']['station_id'];
            let colors = context.props.hideout;
            color = colors[stationID];
            console.log(colors);

            const iconSettings = {
		        mapIconUrl: '<svg version="1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 149 178">'
		                  + '<path fill="{mapIconColor}" stroke="#FFF" '
		                  + 'stroke-width="6" stroke-miterlimit="10" '
		                  + 'd="M126 23l-6-6A69 69 0 0 0 74 1a69 69 0 0 0-51 22A70 70 0 0 0 1 74c0 21 7 38 '
		                  + '22 52l43 47c6 6 11 6 16 0l48-51c12-13 18-29 18-48 0-20-8-37-22-51z"/>'
//		                  + '<circle fill="{mapIconColorInnerCircle}" cx="74" cy="75" r="61"/>'
		                  + '<defs><pattern id="{stationMarkerId}" height="100%" width="100%" viewBox="0 0 100 100">'
                          + '<image width="100" height="100" xlink:href="{stationIconUrl}"/>'
		                  + '</pattern></defs>'
		                  + '<circle fill="{mapIconColorInnerCircle}" cx="74" cy="75" r="57"/>'
		                  + '<circle fill="url(#{stationMarkerId})" cx="74" cy="75" r="50"/>'
		                  + '</svg>',
		        mapIconColor: color,
		        mapIconColorInnerCircle: '#ffffff',
		        stationIconUrl: iconUrl,
		        stationMarkerId: stn_id
	        };

            // icon normal state
            const divIcon = L.divIcon({
              className: "leaflet-data-marker",
              html: L.Util.template(iconSettings.mapIconUrl, iconSettings), //.replace('#','%23'),
              iconAnchor  : [12, 32],
              iconSize    : [45, 50],
              popupAnchor : [0, -28]
            });

            outIcon = new L.Marker(latlng, {icon: divIcon});
            return outIcon;
        }
    },
});