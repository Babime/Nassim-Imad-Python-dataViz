from dash import html
from src.components import GraphContainer
from plotly.express import scatter
from src.utils import scatter_plot, apply_graph_style
import pandas as pd

data = {
    "Minute": [10, 20, 30, 40],
    "Gold Différence": [500, -200, 300, -100],
    "Victoire": ["Oui", "Non", "Oui", "Non"],
}
df = pd.DataFrame(data)

fig = scatter_plot(df, x="Minute", y="Gold Différence", color="Victoire", title="Impact de la Différence de Gold")
fig = apply_graph_style(fig)

layout = html.Div(
    children=[
        GraphContainer(title="Impact de la Différence de Gold", figure=fig),
    ],
    style={
        "padding": "20px",
        "backgroundColor": "#1f1e2e",
        "borderRadius": "10px",
        "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.7)",
    },
)
