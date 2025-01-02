from dash import html, dcc
from dash.dependencies import Input, Output
from src.pages import home, about, simple_page, test_visual, more_complex_page
from src.components.navbar import Navbar

def register_callbacks(app):
    @app.callback(
        [Output("page-content", "children"), Output("navbar", "children")],
        [Input("url", "pathname")]
    )
    def render_page_content(pathname):
        if pathname == "/":
            return home, Navbar(current_page="/")
        elif pathname == "/about":
            return about, Navbar(current_page="/about")
        elif pathname == "/simple-page":
            return simple_page, Navbar(current_page="/simple-page")
        elif pathname == "/more-complex-page":
            return more_complex_page, Navbar(current_page="/more-complex-page")
        elif pathname == "/test-visual":
            return test_visual, Navbar(current_page="/test-visual")
        else:
            return html.Div("404: Page non trouvée.", style={"textAlign": "center", "color": "red"}), Navbar(current_page="")

def create_router(app):
    return html.Div(
        children=[
            dcc.Location(id="url"),
            html.Div(id="page-content"), 
        ]
    )
