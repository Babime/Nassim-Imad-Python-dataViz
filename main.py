from dash import Dash, html, dcc
from src.pages.router import create_router, register_callbacks
from src.components import Header, Footer, InputPseudo
from src.utils.pyltover import Pyltover
from src.utils.pyltover.enums import By, Region, Loading

pyl = Pyltover(api_key='RGAPI-1bd654a2-dffb-4216-b237-f9b8dc6ebe00', region=Region.EUW1, loading_style=Loading.EAGER)

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    children=[
        dcc.Store(id="stored-pseudo", storage_type="local"),
        Header(),
        InputPseudo(app),
        html.Div(id="navbar"),
        create_router(app),
        Footer(),
    ],
    id="main-container",
)

register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)