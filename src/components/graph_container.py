from dash import html, dcc

from src.utils.graph_utils import apply_graph_style

def GraphContainer(title, figure):
    """
    crée un conteneur de graphique avec un titre et une figure stylisée

    Args:
        title (str): le titre du graphique
        figure (plotly.graph_objs._figure.Figure): la figure du graphique à afficher

    Returns:
        html.Div: un conteneur div contenant le titre et le graphique

    """ 
    figure = apply_graph_style(figure)# applique un style au graphique
    return html.Div(
        children=[
            html.H4(title, className="graph-title"),# ajoute un titre au graphique
            dcc.Graph(figure=figure),# affiche le graphique
        ],
        className="graph-container"# ajoute une classe css au conteneur
    )
