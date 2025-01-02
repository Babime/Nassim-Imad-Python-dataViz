from dash import html, dcc

from src.utils.graph_utils import apply_graph_style

def GraphContainer(title, figure):
    figure = apply_graph_style(figure)
    return html.Div(
        children=[
            html.H4(title, className="graph-title"),
            dcc.Graph(figure=figure),
        ],
        className="graph-container"
    )
