from dash import html

def Footer():
    return html.Div(
        children=[
            html.P("© 2025 League of Legends Dashboard | Tous droits réservés"),
        ],
        className="footer"
    )
