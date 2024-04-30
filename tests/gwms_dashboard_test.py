import pytest
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from apps.Dashboards.gwms import generate_dashboard_gwms, gaugeCard, textCard, mapCard, plotCard

@pytest.fixture
def app():
    return Dash(__name__)

def test_generate_dashboard_gwms(app):
    dashboard = generate_dashboard_gwms()
    assert isinstance(dashboard, html.Div)
    assert len(dashboard.children) == 3

    row1 = dashboard.children[0]
    assert isinstance(row1, dbc.Row)
    assert len(row1.children) == 2
    assert isinstance(row1.children[0], dbc.Col)
    assert isinstance(row1.children[1], dbc.Col)

    row2 = dashboard.children[1]
    assert isinstance(row2, dbc.Row)
    assert len(row2.children) == 1
    assert isinstance(row2.children[0], dbc.Col)

    row3 = dashboard.children[2]
    assert isinstance(row3, dbc.Row)
    assert len(row3.children) == 1
    assert isinstance(row3.children[0], dbc.Col)

def test_gauge_card():
    gauge_card = gaugeCard()
    assert isinstance(gauge_card, dbc.Card)
    assert len(gauge_card.children) == 1
    assert isinstance(gauge_card.children[0], dbc.CardBody)
    assert len(gauge_card.children[0].children) == 1
    assert isinstance(gauge_card.children[0].children[0], html.Img)

def test_text_card():
    text_card = textCard()
    assert isinstance(text_card, dbc.Card)
    assert len(text_card.children) == 1
    assert isinstance(text_card.children[0], dbc.Table)
    assert len(text_card.children[0].children) == 2
    assert isinstance(text_card.children[0].children[0], html.Tr)
    assert isinstance(text_card.children[0].children[1], html.Tr)

def test_map_card():
    map_card = mapCard()
    assert isinstance(map_card, dbc.Card)
    assert len(map_card.children) == 1
    assert isinstance(map_card.children[0], html.Div)
    assert len(map_card.children[0].children) == 1
    assert isinstance(map_card.children[0].children[0], dl.Map)

def test_plot_card():
    plot_card = plotCard()
    assert isinstance(plot_card, dbc.Card)
    assert len(plot_card.children) == 1
    assert isinstance(plot_card.children[0], html.Div)
    assert len(plot_card.children[0].children) == 1
    assert isinstance(plot_card.children[0].children[0], dcc.Graph)