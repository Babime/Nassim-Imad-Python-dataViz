from dash import html, dcc, callback, Output, Input, State
from src.components import GraphContainer
from plotly.express import bar
import pandas as pd
import dash

dash.register_page(__name__, '/' + __name__.split('.')[-1])

layout = html.Div(
    children=[
        html.Div(id="graph-container"),
    ],
    style={
        "padding": "20px",
        "backgroundColor": "#1f1e2e",
        "borderRadius": "10px",
    },
)

@callback(
    Output("graph-container", "children"),
    Input("stored-pseudo", "data"),  
    prevent_initial_call=False  
)
def update_graph(stored_pseudo):
    if not stored_pseudo:
        return html.Div("Aucun pseudo stocké. Merci d'entrer un pseudo.")

    from src.utils.pyltover_instance import pyl
    from src.utils.pyltover.enums import By

    tag = str(stored_pseudo).split('#')
    player = pyl.get_account(By.RIOT_ID, str(tag[0]), str(tag[1])).get_summoner()
    matchs = player.get_matchs()

    pings = {"True": {"allInPings": 0, "assistMePings": 0, "enemyMissingPings": 0, "enemyVisionPings": 0,
                  "holdPings": 0, "getBackPings": 0, "needVisionPings": 0, "onMyWayPings": 0,
                  "pushPings": 0, "visionClearedPings": 0},
         "False": {"allInPings": 0, "assistMePings": 0, "enemyMissingPings": 0, "enemyVisionPings": 0,
                   "holdPings": 0, "getBackPings": 0, "needVisionPings": 0, "onMyWayPings": 0,
                   "pushPings": 0, "visionClearedPings": 0}}

    for match in matchs.get_matchs_data():
        for p in match.info.participants:
            if player.puuid != p.puuid:
                continue
            for ping_type in pings["True"].keys():
                pings[str(p.win)][ping_type] += getattr(p, ping_type, 0)

    ping_types = list(pings["True"].keys())
    win_pings = [pings["True"][ping_type] for ping_type in ping_types]
    loss_pings = [pings["False"][ping_type] for ping_type in ping_types]
    total_pings = [win + loss for win, loss in zip(win_pings, loss_pings)]
    win_rate_contribution = [(win / total) * 100 if total > 0 else 0 for win, total in zip(win_pings, total_pings)]

    data = {
        "Ping Type": ping_types,
        "Win Pings": win_pings,
        "Loss Pings": loss_pings,
        "Total Pings": total_pings,
        "Win Rate Contribution (%)": win_rate_contribution,
    }
    df = pd.DataFrame(data)
    df = df[df["Win Pings"] > 0] 
    df = df[df["Loss Pings"] > 0] 

    fig = bar(
        df,
        x="Ping Type",
        y="Win Rate Contribution (%)",
        title="Win Rate Contribution by Ping Type",
        labels={"Ping Type": "Ping Type", "Win Rate Contribution (%)": "Win Rate Contribution (%)"},
        text_auto=True
    )
    fig.update_traces(marker_color='blue', textposition='outside')
    fig.update_layout(yaxis_title="Win Rate Contribution (%)", xaxis_title="Ping Type", showlegend=False)

    return GraphContainer(title="Win Rate Contribution by Ping Type", figure=fig)