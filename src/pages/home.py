from dash import html
import dash

# enregistre la page avec dash et définit la route racine
dash.register_page(__name__, '/')

# définit la mise en page de la page d'accueil
layout = html.Div(
    children=[
        # titre principal de la page
        html.H1("Bienvenue sur le Dashboard League of Legends", className="h1"),
        # paragraphe descriptif
        html.P(
            "Explorez les statistiques et analyses des champions, objectifs, et performances.",
            style={"color": "#eaeaea", "textAlign": "center"},
        ),
    ],
    # style de la mise en page
    style={
        "padding": "20px",
        "margin-bottom": "20px",
        "backgroundColor": "#232323cc",
        "borderRadius": "10px",
    },
)
