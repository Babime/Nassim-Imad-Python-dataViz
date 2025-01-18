from dash import html, dcc, callback, Output, Input
from src.components import GraphContainer
from plotly.express import bar
import pandas as pd
import dash

# Enregistrement de la page avec un chemin spécifique
dash.register_page(__name__, '/' + __name__.split('.')[-1])

# Layout de la page
layout = html.Div(
    children=[
        html.Div(id="objectif-graph-container"),
    ],
    style={
        "padding": "20px",
        "backgroundColor": "#1f1e2e",
        "borderRadius": "10px",
    },
)

@callback(
    Output("objectif-graph-container", "children"),
    Input("stored-pseudo", "data"),
    prevent_initial_call=False
)
def update_graph(stored_pseudo):
    if not stored_pseudo:
        return html.Div("Aucun pseudo stocké. Merci d'entrer un pseudo.", style={"color": "#eaeaea", "textAlign": "center"})


    from src.utils.pyltover_instance import pyl
    from src.utils.pyltover.enums import By

    tag = str(stored_pseudo).split('#')
    player = pyl.get_account(By.RIOT_ID, str(tag[0]), str(tag[1])).get_summoner()
    matchs = player.get_matchs()

    objectives_stats = {
                    "Herald": {"win": 0, "lose": 0},
                    "Dragon": {"win": 0, "lose": 0},
                    "Baron": {"win": 0, "lose": 0},
                    "Horde": {"win": 0, "lose": 0}
                }

    for match in matchs.get_matchs_data():
        match.info.teams[0]

    for match in matchs.get_matchs_data():
        for team in match.info.teams:
            win_status = "win" if team.win else "lose"
            print(team.objectives.baron.kills)
            if team.objectives.get("riftHerald", {}).get("kills", 0) > 0:
                objectives_stats["Herald"][win_status] += team.objectives["riftHerald"]["kills"]

            if team.objectives.get("dragon", {}).get("kills", 0) > 0:
                objectives_stats["Dragon"][win_status] += team.objectives["dragon"]["kills"]

            if team.objectives.get("baron", {}).get("kills", 0) > 0:
                objectives_stats["Baron"][win_status] += team.objectives["baron"]["kills"]

            if team.objectives.get("horde", {}).get("kills", 0) > 0:
                objectives_stats["Horde"][win_status] += team.objectives["horde"]["kills"]

    data = {
        "Objectif": [],
        "Avec Objectif": [],
        "Sans Objectif": [],
    }

    total_matches = len(matchs.get_matchs_data())

    for objective, stats in objectives_stats.items():
        total_with = stats["win"] + stats["lose"]
        total_without = total_matches - total_with

        winrate_with = (stats["win"] / total_with) * 100 if total_with > 0 else 0
        winrate_without = ((total_matches - stats["lose"]) / total_without) * 100 if total_without > 0 else 0

        data["Objectif"].append(objective)
        data["Avec Objectif"].append(winrate_with)
        data["Sans Objectif"].append(winrate_without)

    df = pd.DataFrame(data)

    fig = bar(
        df,
        x="Objectif",
        y=["Avec Objectif", "Sans Objectif"],
        title="Impact des Objectifs sur le Winrate",
        labels={"value": "Winrate (%)", "variable": "Statut"},
        barmode="group",
        text_auto=True,
    )

    return GraphContainer(title="Impact des Objectifs sur le Winrate", figure=fig)
