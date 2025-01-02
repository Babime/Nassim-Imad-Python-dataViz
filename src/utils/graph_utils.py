import plotly.express as px
import plotly.graph_objects as go

def scatter_plot(data, x, y, color=None, size=None, title=None, **kwargs):
    """
    Crée un scatter plot générique.

    Params:
        - data: pd.DataFrame : Données source
        - x: str : Colonne pour l'axe X
        - y: str : Colonne pour l'axe Y
        - color: str : Colonne pour colorer les points
        - size: str : Colonne pour ajuster la taille des points
        - title: str : Titre du graphique
        - kwargs : Autres paramètres Plotly Express

    Returns:
        - fig : Figure Plotly
    """
    fig = px.scatter(data, x=x, y=y, color=color, size=size, title=title, **kwargs)
    return fig


def bar_chart(data, x, y, color=None, barmode="group", title=None, **kwargs):
    """
    Crée un bar chart générique.

    Params:
        - data: pd.DataFrame : Données source
        - x: str : Colonne pour l'axe X
        - y: str : Colonne pour l'axe Y
        - color: str : Colonne pour colorer les barres
        - barmode: str : Mode des barres ('group', 'stack', etc.)
        - title: str : Titre du graphique
        - kwargs : Autres paramètres Plotly Express

    Returns:
        - fig : Figure Plotly
    """
    fig = px.bar(data, x=x, y=y, color=color, barmode=barmode, title=title, **kwargs)
    return fig


def line_chart(data, x, y, color=None, title=None, **kwargs):
    """
    Crée un line chart générique.

    Params:
        - data: pd.DataFrame : Données source
        - x: str : Colonne pour l'axe X
        - y: str : Colonne pour l'axe Y
        - color: str : Colonne pour colorer les lignes
        - title: str : Titre du graphique
        - kwargs : Autres paramètres Plotly Express

    Returns:
        - fig : Figure Plotly
    """
    fig = px.line(data, x=x, y=y, color=color, title=title, **kwargs)
    return fig


def heatmap(data, x, y, z, colorscale="Viridis", title=None, **kwargs):
    """
    Crée un heatmap générique.

    Params:
        - data: pd.DataFrame : Données source
        - x: str : Colonne pour l'axe X
        - y: str : Colonne pour l'axe Y
        - z: str : Colonne pour les valeurs de la couleur
        - colorscale: str : Échelle de couleurs
        - title: str : Titre du graphique
        - kwargs : Autres paramètres Plotly Express

    Returns:
        - fig : Figure Plotly
    """
    fig = px.density_heatmap(data, x=x, y=y, z=z, color_continuous_scale=colorscale, title=title, **kwargs)
    return fig


def apply_graph_style(fig):
    """
    Applique un style personnalisé à un graphique Plotly.

    Args:
        fig (go.Figure): Le graphique Plotly à styliser.

    Returns:
        go.Figure: Le graphique avec le style appliqué.
    """
    fig.update_layout(
        plot_bgcolor="#1e1e30",
        paper_bgcolor="#0d0d0d",
        font=dict(
            family="Cinzel, serif",
            size=14,
            color="#eaeaea",
        ),
        title=dict(
            font=dict(size=20, color="#c9b037"),
            x=0.5,
        ),
        xaxis=dict(
            gridcolor="#333333",
            color="#eaeaea",
        ),
        yaxis=dict(
            gridcolor="#333333",
            color="#eaeaea",
        ),
        legend=dict(
            bgcolor="#1e1e30", 
            bordercolor="#c9b037",
            borderwidth=1,
            font=dict(color="#eaeaea"),
        ),
    )
    return fig