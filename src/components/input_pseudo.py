from dash import html, dcc
from dash.dependencies import Input, Output, State

def InputPseudo(app):
    @app.callback(
        [Output("stored-pseudo", "data"), Output("pseudo-feedback", "children"), Output("pseudo-input", "value")],
        [Input("submit-pseudo", "n_clicks")],
        [State("pseudo-input", "value")],
    )
    def update_pseudo(n_clicks, pseudo):
        if n_clicks and pseudo: #Rajouter les conditions pour le pseudo par la librairie si possible
            return pseudo, f"Pseudo enregistré : {pseudo}", ""
        elif n_clicks:
            return None, "Veuillez entrer un pseudo valide.", ""
        return None, "", ""
    
    return html.Div(
        children=[
            dcc.Input(
                id="pseudo-input",
                type="text",
                placeholder="Entrez votre pseudo...",
                style={
                    "margin": "10px 0",
                    "padding": "10px",
                    "width": "300px",
                    "border": "1px solid #c9b037",
                    "borderRadius": "5px",
                    "fontSize": "1em",
                    "color": "#1f1e2e",
                    "backgroundColor": "#eaeaea",
                },
            ),
            html.Button(
                "Valider",
                id="submit-pseudo",
                style={
                    "marginLeft": "10px",
                    "padding": "10px 20px",
                    "backgroundColor": "#c9b037",
                    "color": "#1f1e2e",
                    "border": "none",
                    "borderRadius": "5px",
                    "fontSize": "1em",
                    "cursor": "pointer",
                },
            ),
            html.Div(
                id="pseudo-feedback",
                style={"marginTop": "10px", "color": "#c9b037", "fontSize": "1.2em"},
            ),
        ],
        style={"textAlign": "center", "marginBottom": "20px", "marginTop": "25px"},
    )

    