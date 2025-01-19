from dash import html, dcc, callback, Output, Input, State
from src.components import GraphContainer
import dash
import plotly.graph_objects as go
import numpy as np

# enregistre la page dash avec un chemin basé sur le nom du fichier
dash.register_page(__name__, '/' + __name__.split('.')[-1])

# définit la mise en page de la page
layout = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Dropdown(
                    id="game-dropdown-damage",
                    placeholder="Choisir une partie...",
                    options=[],  # options du dropdown initialement vide
                    style={"color": "black", 
                           "width": "45%",
                            "margin": "0 auto",},
                ),
            ],
            style={
                "display": "flex",
                "justifyContent": "center",
                "marginBottom": "20px",
            },
        ),
        html.Div(
            id="damage-bar-chart-container",
            style={"display": "flex", "justifyContent": "center"},
        ),
    ],
    style={
        "padding": "20px",
        "backgroundColor": "#232323cc",
        "borderRadius": "10px",
    },
)

# définit le callback pour mettre à jour les options du dropdown et le graphique
@callback(
    [
        Output("game-dropdown-damage", "options"),
        Output("damage-bar-chart-container", "children"),
    ],
    [
        Input("game-dropdown-damage", "value"),
        Input("stored-pseudo", "data"),
    ],
    [
        State("matchs-data-store", "data"),
        State("puuid-store", "data"),
    ],
    prevent_initial_call=False,
)
def update_damage_bar_chart(selected_game_id, _pseudo, stored_data_games, puuid_store):
    if not stored_data_games:
        return [], html.Div("Aucun pseudo stocké. Merci d'entrer un pseudo.", style={"color": "white"})

    from src.utils.pyltover.match import MatchData
    matchs = [MatchData(None, data) for data in stored_data_games]  # crée des objets MatchData à partir des données stockées

    game_options = [
        {"label": f"Partie {game.metadata.matchId}", "value": game.metadata.matchId}
        for game in matchs
    ]  # crée une liste d'options pour le dropdown avec les identifiants des parties

    if not selected_game_id:
        return game_options, html.Div("Selectionnez une partie pour voir les données.", style={"color": "white"})
        # si aucune partie n'est sélectionnée, retourne les options du dropdown et un message

    selected_game_data = next(
        (game for game in matchs if game.metadata.matchId == selected_game_id), None
    )  # trouve les données de la partie sélectionnée

    if not selected_game_data:
        return game_options, html.Div("Partie introuvable.", style={"color": "white"})
        # si les données de la partie sélectionnée ne sont pas trouvées, retourne les options du dropdown et un message

    participants = selected_game_data.info.participants  # obtient les participants de la partie sélectionnée
    player_index = [participant.participantId for participant in participants if participant.puuid == puuid_store][0]
    # trouve l'index du joueur principal

    damage_data = {
        participant.participantId: {
            "total": participant.totalDamageDealtToChampions,
            "magic": participant.magicDamageDealtToChampions,
            "physical": participant.physicalDamageDealtToChampions,
        }
        for participant in participants
    }  # crée un dictionnaire avec les dégâts infligés par chaque participant

    fig = go.Figure()  # crée une nouvelle figure pour le graphique

    for participant_id, damage in damage_data.items():
        participant_name = "Vous" if participant_id == player_index else f"Joueur {participant_id}"
        # détermine le nom du participant
        team_color = "blue" if participant_id <= 5 else "red"
        pastel_color = "lightblue" if team_color == "blue" else "lightcoral"
        dark_color = "darkblue" if team_color == "blue" else "darkred"
        # détermine les couleurs de l'équipe

        fig.add_trace(go.Bar(
            x=[participant_name],
            y=[damage["magic"]],
            name=f"Magic Damage - {participant_name}",
            marker=dict(color=dark_color),
            showlegend=False
        ))  # ajoute une barre pour les dégâts magiques

        fig.add_trace(go.Bar(
            x=[participant_name],
            y=[damage["physical"]],
            name=f"Physical Damage - {participant_name}",
            marker=dict(color=pastel_color),
            showlegend=False
        ))  # ajoute une barre pour les dégâts physiques

    fig.update_layout(
        title=f"Dégâts effectués dans la partie {selected_game_id}",
        xaxis_title="Participants",
        yaxis_title="Total Damage",
        template="plotly_white",
        height=500,
        width=700,
        barmode="stack"
    )  # met à jour la mise en page du graphique

    graph_content = GraphContainer(title="Damage par Participant", figure=fig)
    # crée un conteneur de graphique avec le titre et la figure

    return game_options, graph_content  # retourne les options du dropdown et le contenu du graphique
