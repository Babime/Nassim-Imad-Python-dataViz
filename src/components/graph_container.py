from dash import html, dcc

def GraphContainer(title, figure):
    return html.Div(
        children=[
            html.H4(title, className="graph-title"),
            dcc.Graph(figure=figure),
        ],
        className="graph-container"
    )
