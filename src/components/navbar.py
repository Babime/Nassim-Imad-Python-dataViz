from dash import html, dcc, callback
import dash

def Navbar(current_page="", pseudo=""):

    is_disabled = pseudo is None or pseudo.strip() == ""

    return html.Div(
        children=[
            dcc.Link(
                "Accueil",
                href="/",
                className="navbar-link active" if current_page == "/" else "navbar-link",
            ),
            dcc.Link(
                "À propos",
                href="/about",
                className="navbar-link active" if current_page == "/about" else "navbar-link",
            ),
            dcc.Link(
                "Simple Page",
                href="/simple_page",
                className="navbar-link disabled" if is_disabled else "navbar-link active" if current_page == "/simple_page" else "navbar-link",
            ),
            dcc.Link(
                "Page Complexe",
                href="/more-complex-page",
                className="navbar-link disabled" if is_disabled else "navbar-link active" if current_page == "/more-complex-page" else "navbar-link",
            ),
            dcc.Link(
                "Tests Visuels",
                href="/test-visual",
                className="navbar-link disabled" if is_disabled else "navbar-link active" if current_page == "/test-visual" else "navbar-link",
            ),
        ],
        className="navbar"
    )
