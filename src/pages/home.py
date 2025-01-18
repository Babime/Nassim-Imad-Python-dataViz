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
        "backgroundColor": "#1f1e2e",
        "borderRadius": "10px",
        "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.7)",
    },
)
