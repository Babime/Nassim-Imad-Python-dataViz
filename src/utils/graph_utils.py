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
