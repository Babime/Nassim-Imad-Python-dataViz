from dash import html, dcc

def Navbar(current_page):
    return html.Div(
        children=[
            dcc.Link("Accueil", href="/", className="navbar-link active" if current_page == "/" else "navbar-link"),
            dcc.Link("À propos", href="/about", className="navbar-link active" if current_page == "/about" else "navbar-link"),
            dcc.Link("Simple Page", href="/simple-page", className="navbar-link active" if current_page == "/simple-page" else "navbar-link"),
            dcc.Link("Page Complexe", href="/more-complex-page", className="navbar-link active" if current_page == "/more-complex-page" else "navbar-link"),
            dcc.Link("Tests Visuels", href="/test-visual", className="navbar-link active" if current_page == "/test-visual" else "navbar-link"),
        ],
        className="navbar"
    )
