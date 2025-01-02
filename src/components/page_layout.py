from dash import html
from .header import Header
from .footer import Footer
from .navbar import Navbar

def PageLayout(content):
    return html.Div(
        children=[
            Header(),
            Navbar(),
            html.Div(content, id="page-content"),
            Footer(),
        ],
        id="main-container"
    )
