import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Rain Watch", href="/apps/rfms"),
                dbc.DropdownMenuItem("Flood Watch", href="/apps/gwms"),
                dbc.DropdownMenuItem("Tidal Watch", href="/apps/tdms"),
                dbc.DropdownMenuItem("Heat Watch", href="/apps/hims"),
                dbc.DropdownMenuItem("Hazard Watch", href="/apps/hzms"),
            ],
            nav=True,
            in_navbar=True,
            label="Portals",
        ),
    ],
    brand="Climate Watch",
    brand_href="/home",
    color="#4D4478",
    dark=True,
)