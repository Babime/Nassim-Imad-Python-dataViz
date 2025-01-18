from dash import html, dcc
from dash.dependencies import Input, Output, State

def InputPseudo(app):
    @app.callback(
        [Output("stored-pseudo", "data"), Output("pseudo-feedback", "children"), Output("pseudo-input", "value")],
        [Input("submit-pseudo", "n_clicks")],
        [State("pseudo-input", "value")],
    )
    def update_pseudo(n_clicks, pseudo):
        if n_clicks and pseudo:  # Validate the pseudo using the library if possible
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
                    "padding": "12px 15px",
                    "width": "300px",
                    "border": "1px solid rgba(0, 128, 255, 0.5)",
                    "borderRadius": "10px",
                    "fontSize": "1em",
                    "color": "#ffffff",
                    "backgroundColor": "rgba(35, 35, 35, 0.85)",
                    "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.2)",
                    "transition": "box-shadow 0.3s ease-in-out, transform 0.2s ease-in-out",
                },
            ),
            html.Button(
                "Valider",
                id="submit-pseudo",
                style={
                    "marginLeft": "10px",
                    "padding": "10px 25px",
                    "backgroundColor": "rgba(0, 128, 255, 0.2)",
                    "color": "#ffffff",
                    "border": "1px solid rgba(0, 128, 255, 0.5)",
                    "borderRadius": "25px",
                    "fontSize": "1.2em",
                    "cursor": "pointer",
                    "transition": "background-color 0.3s ease-in-out, transform 0.2s ease-in-out",
                },
                n_clicks=0,
            ),
            html.Div(
                id="pseudo-feedback",
                style={
                    "marginTop": "10px",
                    "color": "#0080ff",
                    "fontSize": "1.2em",
                },
            ),
        ],
        style={"textAlign": "center", "marginBottom": "20px", "marginTop": "25px"},
    )
