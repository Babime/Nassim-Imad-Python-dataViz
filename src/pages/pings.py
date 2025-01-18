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
    [Input("stored-pseudo", "data"), Input("matchs-data-store", "data"), Input("puuid-store", "data")],
    prevent_initial_call=False
)
def update_graph(stored_pseudo, matchs_store, puuid_store):
    if not stored_pseudo:
        return html.Div("Aucun pseudo stocké. Merci d'entrer un pseudo.")

    pings = {"True": {"allInPings": 0, "assistMePings": 0, "enemyMissingPings": 0, "enemyVisionPings": 0,
                  "holdPings": 0, "getBackPings": 0, "needVisionPings": 0, "onMyWayPings": 0,
                  "pushPings": 0, "visionClearedPings": 0},
             "False": {"allInPings": 0, "assistMePings": 0, "enemyMissingPings": 0, "enemyVisionPings": 0,
                       "holdPings": 0, "getBackPings": 0, "needVisionPings": 0, "onMyWayPings": 0,
                       "pushPings": 0, "visionClearedPings": 0}}

    from src.utils.pyltover.match import MatchData
    matchs = [MatchData(None, data) for data in matchs_store]

    ping_types = list(pings["True"].keys())
    win_games_per_ping = {ping_type: 0 for ping_type in ping_types}
    loss_games_per_ping = {ping_type: 0 for ping_type in ping_types}

    for match in matchs:
        for p in match.info.participants:
            if puuid_store != p.puuid:
                continue
            for ping_type in ping_types:
                if getattr(p, ping_type, 0) > 0:
                    if p.win:
                        win_games_per_ping[ping_type] += 1
                    else:
                        loss_games_per_ping[ping_type] += 1
                pings[str(p.win)][ping_type] += getattr(p, ping_type, 0)

    ping_win_probabilities = {
        ping_type: win_games_per_ping[ping_type] / (win_games_per_ping[ping_type] + loss_games_per_ping[ping_type])
        if (win_games_per_ping[ping_type] + loss_games_per_ping[ping_type]) > 0 else 0
        for ping_type in ping_types
    }
    
    total_games = len(matchs)
    total_wins = sum(1 for match in matchs if any(p.win for p in match.info.participants if p.puuid == puuid_store))
    baseline_winrate = total_wins / total_games if total_games > 0 else 0

    ping_impact = {
        ping_type: (ping_win_probabilities[ping_type] - baseline_winrate)
        for ping_type in ping_types
    }

    ping_impact_ratio = {
        ping_type: (ping_win_probabilities[ping_type] / baseline_winrate)
        if baseline_winrate > 0 else float('inf')
        for ping_type in ping_types
    }

    filtered_data = {
        "Ping Type": [],
        "Win Probability": [],
        "Impact (Difference)": [],
        "Impact (Ratio)": [],
    }

    for ping_type in ping_types:
        if (win_games_per_ping[ping_type] > 0 or loss_games_per_ping[ping_type] > 0) and ping_impact[ping_type] != -0.55:
            filtered_data["Ping Type"].append(ping_type)
            filtered_data["Win Probability"].append(ping_win_probabilities[ping_type])
            filtered_data["Impact (Difference)"].append(ping_impact[ping_type])
            filtered_data["Impact (Ratio)"].append(ping_impact_ratio[ping_type])

    df = pd.DataFrame(filtered_data)

    bar_colors = ["green" if val > 0 else "red" for val in df["Impact (Difference)"]]

    fig = bar(
        df,
        x="Ping Type",
        y="Impact (Difference)", 
        title="Adjusted Impact of Ping Usage on Win Probability",
        labels={"Ping Type": "Ping Type", "Impact (Difference)": "Adjusted Impact (vs Baseline)"},
        text_auto=True,
    )
    fig.update_traces(marker_color=bar_colors, textposition='outside')
    fig.update_layout(
        yaxis_title="Adjusted Impact (Difference)",
        xaxis_title="Ping Type",
        showlegend=False,
        xaxis={"automargin": True, "tickangle": -45},
        yaxis={"automargin": True, "range": [min(df["Impact (Difference)"]) - 0.1, max(df["Impact (Difference)"]) + 0.1]}
    )

    return GraphContainer(title="Impact of Ping Usage on Win Probability", figure=fig)
