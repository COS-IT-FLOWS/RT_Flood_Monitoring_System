import pytest
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from apps.Dashboards.rfms import generate_dashboard_rfms

def test_generate_dashboard_rfms():
    # Create a test Dash app
    app = Dash(__name__)

    # Call the generate_dashboard_rfms function
    dashboard = generate_dashboard_rfms("Test Station ID")

    # Assert that the dashboard is a Dash component
    assert isinstance(dashboard, html.Div)

    # Assert that the dashboard has the correct structure
    assert len(dashboard.children) == 2
    assert isinstance(dashboard.children[0], dbc.Row)
    assert isinstance(dashboard.children[1], dbc.Row)

    # # Assert that the first row has the correct structure
    row1 = dashboard.children[0]
    assert len(row1.children) == 2
    assert isinstance(row1.children[0], dbc.Col)
    assert isinstance(row1.children[1], dbc.Col)

    # Assert that the first column has the correct structure
    col1 = row1.children[0]
    assert isinstance(col1.children, dbc.Card)
    assert isinstance(col1.children.children[0], dbc.CardBody)
    # assert isinstance(col1.children.children.children[0], html.Img)

    # Assert that the second column has the correct structure
    col2 = row1.children[1]
    assert isinstance(col2.children, dbc.Card)
    assert isinstance(col2.children.children[0], dbc.Table)

    # Assert that the second row has the correct structure
    row2 = dashboard.children[1]
    assert len(row2.children) == 2
    assert isinstance(row2.children[0], dbc.Col)
    assert isinstance(row2.children[1], dbc.Col)

    # Assert that the first column of the second row has the correct structure
    col3 = row2.children[0]
    assert isinstance(col3.children[0], dbc.Card)
    assert isinstance(col3.children[0].children, html.Div)
    # assert isinstance(col3.children[0].children.children, dcc.Graph)

    # Assert that the second column of the second row has the correct structure
    col4 = row2.children[1]
    assert isinstance(col4.children[0], dbc.Card)
    assert isinstance(col4.children[0].children, html.Div)
    # assert isinstance(col4.children.children.children, dcc.Graph)

    # Clean up
    # app.server.ki()