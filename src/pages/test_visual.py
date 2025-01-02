from dash import html
from src.components import GraphContainer
from src.utils.graph_utils import scatter_plot, bar_chart, line_chart, heatmap, apply_graph_style
import pandas as pd

data = {
    "minute": [1, 2, 3, 4, 5],
    "item_vendu": [0, 0, 1, 1, 1],
    "situation": ["early", "early", "mid", "mid", "late"],
    "objectif": ["herald", "dragon", "baron", "grubs", "dragon"],
    "winrate": [0.6, 0.7, 0.8, 0.5, 0.7],
    "type": ["XP", "Gold", "XP", "Gold", "XP"],
    "value": [100, 200, 150, 250, 180],
}

df = pd.DataFrame(data)

scatter = scatter_plot(df, x="minute", y="item_vendu", color="situation", title="Items Starters")
scatter = apply_graph_style(scatter)
bar_chart_obj = bar_chart(df, x="objectif", y="winrate", title="Objectifs et Winrate")
bar_chart_obj = apply_graph_style(bar_chart_obj)

layout = html.Div(
    children=[
        GraphContainer(title="Scatter Plot (Items)", figure=scatter),
        GraphContainer(title="Bar Chart (Objectifs)", figure=bar_chart_obj),
    ],
    style={
        "padding": "20px",
        "backgroundColor": "#1f1e2e",
        "borderRadius": "10px",
        "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.7)",
    },
)
