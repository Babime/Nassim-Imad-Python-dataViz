from dash import html

def Footer():
    return html.Div(
        children=[
            html.P("© 2023 League of Legends Dashboard | Tous droits réservés"),
        ],
        className="footer"
    )
