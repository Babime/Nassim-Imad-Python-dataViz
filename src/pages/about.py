from dash import html

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
        "backgroundColor": "#1f1e2e",
        "borderRadius": "10px",
        "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.7)",
    },
)
