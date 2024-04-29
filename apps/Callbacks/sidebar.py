from dash.dependencies import Input, Output, State
from apps.Callbacks.callbacks_manager import CallbackManager

callback_sidebar = CallbackManager()

# **********************************************************************************************************************
# Callbacks for Sidebar
# **********************************************************************************************************************
from apps.Sidebar.home import home_sidebar
from apps.Sidebar.rfms import rfms_sidebar
from apps.Sidebar.gwms import gwms_sidebar
from apps.Sidebar.tdms import tdms_sidebar
from apps.Elements.colors import legendColors_rf, legendColors_gw



@callback_sidebar.callback([Output('sidebar-content', 'children'), Output('sub-heading', 'children')],
                           [Input('url', 'pathname')])
def generate_sidebar(pathname):
    if pathname == '/apps/gwms':
        return gwms_sidebar(legendColors_gw), 'FloodWatch'
    elif pathname == '/apps/rfms':
        return rfms_sidebar(legendColors_rf), 'RainWatch'
    elif pathname == '/apps/tdms':
        return tdms_sidebar(legendColors_rf), 'TidalWatch'
    elif pathname == '/':
        return home_sidebar(), 'Climatewatch'
    else:
        None, None