from dash import html
from src.components import GraphContainer
from plotly.express import bar
from src.utils import bar_chart
import pandas as pd

import dash
dash.register_page(__name__, '/'+__name__.split('.')[-1])

from src.utils.pyltover_instance import pyl
from src.utils.pyltover.enums import By

temp = pyl.get_account(By.RIOT_ID, 'Babimee', 'EUW').get_summoner()

data = {
    "Champion": [temp.account_id, "Lux", "Yasuo"],
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
