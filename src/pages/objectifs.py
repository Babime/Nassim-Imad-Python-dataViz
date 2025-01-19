from dash import html, callback, Output, Input
from src.components import GraphContainer
from plotly.express import bar
import pandas as pd
import dash

# enregistre la page dans dash
dash.register_page(__name__, '/' + __name__.split('.')[-1])

# définit la mise en page de la page
layout = html.Div(
    children=[
        html.Div(id="objectif-graph-container"),
    ],
    style={
        "padding": "20px",
        "backgroundColor": "#232323cc",
        "borderRadius": "10px",
    },
)

# définit le callback pour mettre à jour le graphique
@callback(
    Output("objectif-graph-container", "children"),
    [Input("stored-pseudo", "data"), Input("matchs-data-store", "data"), Input("puuid-store", "data")],
    prevent_initial_call=False
)
def update_graph(stored_pseudo, matchs_store, puuid_store):
    # vérifie si un pseudo est stocké
    if not stored_pseudo:
        return html.Div("Aucun pseudo stocké. Merci d'entrer un pseudo.", style={"color": "#eaeaea", "textAlign": "center"})

    try:
        from src.utils.pyltover.match import MatchData

        # crée une liste d'objets MatchData à partir des données de matchs
        matchs = [MatchData(None, data) for data in matchs_store]

        # initialise les statistiques des objectifs
        objectives_stats = {
            "riftHerald": {"wins": 0, "total": 0},
            "baron": {"wins": 0, "total": 0},
            "horde": {"wins": 0, "total": 0},
            "atakhan": {"wins": 0, "total": 0}
        }

        global_wins = 0

        # parcourt chaque match pour calculer les statistiques
        for match in matchs:
            for p in match.info.participants:
                if puuid_store != p.puuid:
                    continue

            for team in match.info.teams:
                if team.teamId != p.teamId:
                    continue
                if team.win:
                    global_wins += 1

                # met à jour les statistiques des objectifs
                for obj_str in objectives_stats.keys():
                    if getattr(team.objectives, obj_str).kills > 0:
                        objectives_stats[obj_str]["total"] += 1
                        if team.win:
                            objectives_stats[obj_str]["wins"] += 1

        win_with_objectives = {}

        # calcule le taux de victoire pour chaque objectif
        for objective, stats in objectives_stats.items():
            if stats["total"] > 0:
                winrate = (stats["wins"] / stats["total"]) * 100
                win_with_objectives[objective] = winrate

        # calcule le taux de victoire global
        global_winrate = global_wins / len(matchs) * 100
        objective_impact = {
            objective_type: (win_with_objectives[objective_type] - global_winrate)
            for objective_type in objectives_stats.keys()
        }

        # crée un dataframe avec les données calculées
        data = {
            "Objectif": [str(objective).capitalize() for objective in win_with_objectives.keys()],
            "Impact": [objective_impact[objective] for objective in win_with_objectives.keys()],
        }

        df = pd.DataFrame(data)

        # crée un graphique à barres avec plotly
        fig = bar(
            df,
            x="Objectif",
            y="Impact",
            title="Impact du Joueur par Objectif Pris par son Équipe",
            labels={"Objectif": "Type d'Objectif", "Impact": "Impact"},
            text_auto=True,
        )

        # met à jour la mise en page du graphique
        fig.update_layout(
            yaxis_title="Impact (Difference)",
            xaxis_title="Objecitf Type",
            showlegend=False,
            yaxis={"range": [df["Impact"].min() - 5, df["Impact"].max() + 5]}
        )

        # retourne le graphique dans un conteneur
        return GraphContainer(title="Impact par Objectif", figure=fig)

    except Exception as e:
        # retourne un message d'erreur en cas d'exception
        return html.Div(f"Erreur lors du traitement des données : {e}", style={"color": "red", "textAlign": "center"})
