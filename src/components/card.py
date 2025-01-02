from dash import html

def create_card(title, content):
    return html.Div(
        children=[
            html.H4(title, className="card-title"),
            html.P(content, className="card-content"),
        ],
        className="card"
    )
