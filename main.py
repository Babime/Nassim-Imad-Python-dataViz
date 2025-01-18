from dash import Dash, html, dcc, callback, page_container
from src.components import Header, Footer, InputPseudo, Navbar
from dash.dependencies import Input, Output, State

app = Dash(__name__, suppress_callback_exceptions=True, use_pages=True, pages_folder="./src/pages")

app.layout = html.Div(
    children=[
        dcc.Location(id="url"),
        dcc.Store(id="stored-pseudo", storage_type="local"),
        dcc.Store(id='puuid-store', storage_type="local"),
        dcc.Store(id='matchs-data-store', storage_type="memory"),
        dcc.Store(id='matchs-timeline-store', storage_type="memory"),
        Header(),
        InputPseudo(app),
        html.Div(id="navbar"),
        page_container,
        Footer(),
    ],
    id="main-container",
)

@callback(
    Output("navbar", "children"),
    [Input("stored-pseudo", "data"), Input("url", "pathname")],
)
def update_navbar(pseudo, current_page):
    return Navbar(current_page=current_page, pseudo=pseudo)

if __name__ == "__main__":
    app.run_server(debug=True)