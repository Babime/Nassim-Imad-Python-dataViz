from dash import Dash, html
from src.pages.router import create_router, register_callbacks
from src.components import Header, Footer

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    children=[
        Header(),
        html.Div(id="navbar"),
        create_router(app),
        Footer(),
    ],
    id="main-container",
)

register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)