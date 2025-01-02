from dash import html

def Header(title="League of Legends Dashboard"):
    return html.Div(
        children=[
            html.H1(title, style={"marginBottom": "5px"}),
        ],
        className="header"
    )
