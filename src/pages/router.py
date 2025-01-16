from dash import html, dcc
from dash.dependencies import Input, Output, State
from src.pages import home, about, simple_page, test_visual, more_complex_page
from src.components.navbar import Navbar

def register_callbacks(app):
    @app.callback(
        Output("page-content", "children"),
        Input("url", "pathname"),
        [State("stored-pseudo", "data")],
    )
    def render_page_content(pathname, pseudo):
        if pseudo is None or pseudo.strip() == "":
            if pathname == "/":
                return home
            if pathname == "/about":
                return about

        match pathname:
            case "/":
                return home
            case "/about":
                return about
            case "/simple-page":
                return simple_page
            case "/more-complex-page":
                return more_complex_page
            case "/test-visual":
                return test_visual
            case _:
                return html.Div("404: Page non trouvée.", style={"textAlign": "center", "color": "red"})


    @app.callback(
        Output("navbar", "children"),
        [Input("stored-pseudo", "data"), Input("url", "pathname")],
    )
    def update_navbar(pseudo, current_page):
        return Navbar(current_page=current_page, pseudo=pseudo)


def create_router(app):
    return html.Div(
        children=[
            dcc.Location(id="url"),
            html.Div(id="page-content"), 
        ]
    )
