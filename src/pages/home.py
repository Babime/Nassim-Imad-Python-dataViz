from dash import html
import dash

dash.register_page(__name__, '/')

layout = html.Div(
    children=[
        html.H1("Bienvenue sur le Dashboard League of Legends", className="h1"),
        html.P(
            "Explorez les statistiques et analyses des champions, objectifs, et performances.",
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
