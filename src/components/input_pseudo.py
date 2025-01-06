from dash import html, dcc

def InputPseudo():
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
