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
                "Objectifs",
                href="/objectifs",
                className="navbar-link disabled" if is_disabled else "navbar-link active" if current_page == "/objectifs" else "navbar-link",
            ),
            dcc.Link(
                "Pings",
                href="/pings",
                className="navbar-link disabled" if is_disabled else "navbar-link active" if current_page == "/pings" else "navbar-link",
            ),
            dcc.Link(
                "Positions",
                href="/positions",
                className="navbar-link disabled" if is_disabled else "navbar-link active" if current_page == "/positions" else "navbar-link",
            ),
            dcc.Link(
                "Golds",
                href="/golds",
                className="navbar-link disabled" if is_disabled else "navbar-link active" if current_page == "/golds" else "navbar-link",
            ),
            dcc.Link(
                "Damage",
                href="/damage",
                className="navbar-link disabled" if is_disabled else "navbar-link active" if current_page == "/damage" else "navbar-link",
            )
        ],
        className="navbar"
    )
