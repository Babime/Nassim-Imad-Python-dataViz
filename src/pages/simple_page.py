from dash import html
from src.components import GraphContainer
from plotly.express import bar
from src.utils import bar_chart
import pandas as pd

data = {
    "Champion": ["Ahri", "Lux", "Yasuo"],
    "Winrate": [52, 48, 50],
}
df = pd.DataFrame(data)

fig = bar_chart(df, x="Champion", y="Winrate")

layout = html.Div(
    children=[
        GraphContainer(title="Winrate des Champions", figure=fig),
    ],
    style={
        "padding": "20px",
        "backgroundColor": "#1f1e2e",
        "borderRadius": "10px",
        "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.7)",
    },
)
