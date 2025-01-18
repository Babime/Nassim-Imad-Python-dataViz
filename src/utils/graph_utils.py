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
        plot_bgcolor="rgba(0, 128, 255, 0.2)",
        paper_bgcolor="rgba(0, 128, 255, 0.1)",
        font=dict(
            family="Poppins, sans-serif",
            size=16,
            color="#ffffff",
        ),
        title=dict(
            font=dict(size=22, color="#0080ff"),
            x=0.5,
            y=0.95,
            xanchor="center",
            yanchor="top",
        ),
        xaxis=dict(
            gridcolor="rgba(255, 255, 255, 0.2)",
            zerolinecolor="rgba(255, 255, 255, 0.3)",
            color="#ffffff",
            title=dict(
                font=dict(size=14, color="#0080ff")
            )
        ),
        yaxis=dict(
            gridcolor="rgba(255, 255, 255, 0.2)",
            zerolinecolor="rgba(255, 255, 255, 0.3)",
            color="#ffffff",
            title=dict(
                font=dict(size=14, color="#0080ff")
            )
        ),
        legend=dict(
            bgcolor="rgba(0, 128, 255, 0.1)", 
            bordercolor="#0080ff",
            borderwidth=1,
            font=dict(color="#ffffff"),
        ),
        margin=dict(l=50, r=50, t=50, b=50),
    )
    return fig
