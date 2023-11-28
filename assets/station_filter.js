window.Filters = Object.assign({}, window.Filters, {
    customFilter_RFMS: {
        stationFilter: function(feature, context) {
//            let river_basin_id = context.props.hideout.id;
            let stationID = feature.properties.Station_ID;
            let data_source = context.props.hideout.dt_source;
            let station_type_out, data_source_out, river_basin_out;
            let data = context.props.hideout.date_data;
//            river_basin_out = river_basin_id == feature['properties']['Id'];

            if(data_source == 'CS')
                {
                    data_source_out = stationID.includes('CS');
                }
            else if(data_source == 'OTH')
                {
                    data_source_out = stationID.includes('IMD') || stationID.includes('CWC') || stationID.includes('RSVR');
                }
            else
                {
                    data_source_out = true;
                }

            return data_source_out;
        }
    },
    customFilter_GWMS: {
        stationFilter: function(feature, context) {
            let river_basin_out = context.props.hideout.Basin_ID == feature.properties.Basin_ID;
            let station_type = context.props.hideout.Station_Type;

            if(station_type == 'All')
                {
                    station_type_out = true;
                }
            else
                {
                    station_type_out = feature.properties.Station_ID.includes(station_type);
                }

            return river_basin_out && station_type_out;
        }
    },

    customFilter_TDMS: {
        stationFilter: function(feature, context) {
            let station_type = context.props.hideout.station_type;
            let stationID = feature.properties.Station_ID;

            if(['RFI', 'TFI'].indexOf(station_type) >= 0)
                {
                    station_type_out = stationID.includes('RSD');
                }
            else if(station_type == 'CTM')
                {
                    station_type_out = stationID.includes('TDS');
                }
            else if(station_type == 'TDG')
                {
                    station_type_out = stationID.includes('TDG');
                }
            else if(station_type == 'ATG')
                {
                    station_type_out = stationID.includes('ATG');
                }

            return station_type_out;
        }
    },

    customFilter_HIMS: {
        stationFilter: function(feature, context) {
            let stationID = feature.properties.station_id;
            if (stationID in context.props.hideout)
                {
                    return true
                }
            else
                {
                    return false
                }
        }
    },
});