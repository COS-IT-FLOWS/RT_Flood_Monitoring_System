import yaml

from dash import dcc, html
# import dash_auth
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash_extensions.enrich import DashProxy, TriggerTransform, MultiplexerTransform

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

dashboards = config.get('dashboards')

for each in dashboards:
    print(each)
    from apps import each as each


# from apps import * 

# from apps.Callbacks.sidebar import callback_sidebar
# from apps.Callbacks.rfms import callback_rfms
# from apps.Callbacks.gwms import callback_gwms
# from apps.Callbacks.tdms import callback_tdms
# from apps.Elements import Home


# Keep this out of source code repository - save in a file or a database
# VALID_USERNAME_PASSWORD_PAIRS = {
#     'admin': 'passwd'
# }

app = DashProxy(__name__, transforms=[TriggerTransform(), MultiplexerTransform()], external_stylesheets=[dbc.themes.SUPERHERO])
# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
# )

app.title = 'ClimateWatch'
# For connecting to mod_wsgi apache web server [flask-like]
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return Home.layout
    elif pathname == '/apps/gwms':
        return gwms.layout
    elif pathname == '/apps/rfms':
        return rfms.layout
    elif pathname == '/apps/tdms':
        return tdms.layout
    else:
        return '404 Page Not Found'

callback_sidebar.attach_to_app(app)
callback_rfms.attach_to_app(app)
callback_gwms.attach_to_app(app)
callback_tdms.attach_to_app(app)

def main():
    app.run_server(debug=False, port='8050')

if __name__ == '__main__':
    main()
