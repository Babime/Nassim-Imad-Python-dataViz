from dash import html
import dash

dash.register_page(__name__, '/' + __name__.split('.')[-1])

layout = html.Div(
    children=[
        html.H1("À propos de ce tableau de bord", className="h1"),
        html.P(
            "Ce tableau de bord explore les performances des joueurs de League of Legends "
            "et offre des analyses détaillées pour améliorer les stratégies.",
            style={"color": "#eaeaea", "textAlign": "center"},
        ),
        html.P(
            "Technologies utilisées : Python, Dash, Plotly, et Pandas.",
            style={"color": "#eaeaea", "textAlign": "center"},
        ),
    ],
    style={
        "padding": "20px",
        "margin-bottom": "20px",
        "backgroundColor": "#232323cc",
        "borderRadius": "10px",
    },
)
