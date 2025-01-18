from dash import html, callback, Output, Input
from src.components import GraphContainer
from plotly.express import bar
import pandas as pd
import dash

dash.register_page(__name__, '/' + __name__.split('.')[-1])

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
    [Input("stored-pseudo", "data"), Input("matchs-data-store", "data"), Input("puuid-store", "data")],
    prevent_initial_call=False
)
def update_graph(stored_pseudo, matchs_store, puuid_store):
    if not stored_pseudo:
        return html.Div("Aucun pseudo stocké. Merci d'entrer un pseudo.", style={"color": "#eaeaea", "textAlign": "center"})

    try:
        from src.utils.pyltover.match import MatchData

        matchs = [MatchData(None, data) for data in matchs_store]

        objectives_stats = {
            "riftHerald": {"wins": 0, "total": 0},
            "baron": {"wins": 0, "total": 0},
            "horde": {"wins": 0, "total": 0},
            "atakhan": {"wins": 0, "total": 0}
        }

        global_wins = 0

        for match in matchs:
            for p in match.info.participants:
                if puuid_store != p.puuid:
                    continue

            for team in match.info.teams:
                if team.teamId != p.teamId:
                    continue
                if team.win:
                    global_wins += 1

                for obj_str in objectives_stats.keys():
                    if getattr(team.objectives, obj_str).kills > 0:
                        objectives_stats[obj_str]["total"] += 1
                        if team.win:
                            objectives_stats[obj_str]["wins"] += 1

        win_with_objectives = {}

        for objective, stats in objectives_stats.items():
            if stats["total"] > 0:
                winrate = (stats["wins"] / stats["total"]) * 100
                win_with_objectives[objective] = winrate

        global_winrate = global_wins / len(matchs) * 100
        objective_impact = {
            objective_type: (win_with_objectives[objective_type] - global_winrate)
            for objective_type in objectives_stats.keys()
        }

        data = {
            "Objectif": [str(objective).capitalize() for objective in win_with_objectives.keys()],
            "Impact": [objective_impact[objective] for objective in win_with_objectives.keys()],
        }

        df = pd.DataFrame(data)

        fig = bar(
            df,
            x="Objectif",
            y="Impact",
            title="Impact du Joueur par Objectif Pris par son Équipe",
            labels={"Objectif": "Type d'Objectif", "Impact": "Impact"},
            text_auto=True,
        )

        fig.update_layout(
            yaxis_title="Impact (Difference)",
            xaxis_title="Objecitf Type",
            showlegend=False,
            yaxis={"range": [df["Impact"].min() - 5, df["Impact"].max() + 5]}
        )

        return GraphContainer(title="Impact par Objectif", figure=fig)

    except Exception as e:
        return html.Div(f"Erreur lors du traitement des données : {e}", style={"color": "red", "textAlign": "center"})
