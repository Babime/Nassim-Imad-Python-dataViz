from dash import html, dcc, callback, Output, Input, State
from src.components import GraphContainer
import dash
import plotly.graph_objects as go
import numpy as np

dash.register_page(__name__, '/' + __name__.split('.')[-1])

layout = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Dropdown(
                    id="game-dropdown-damage",
                    placeholder="Choisir une partie...",
                    options=[],  
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
    matchs = [MatchData(None, data) for data in stored_data_games]

    game_options = [
        {"label": f"Partie {game.metadata.matchId}", "value": game.metadata.matchId}
        for game in matchs
    ]

    if not selected_game_id:
        return game_options, html.Div("Selectionnez une partie pour voir les données.", style={"color": "white"})

    selected_game_data = next(
        (game for game in matchs if game.metadata.matchId == selected_game_id), None
    )

    if not selected_game_data:
        return game_options, html.Div("Partie introuvable.", style={"color": "white"})

    participants = selected_game_data.info.participants
    player_index = [participant.participantId for participant in participants if participant.puuid == puuid_store][0]

    damage_data = {
        participant.participantId: {
            "total": participant.totalDamageDealtToChampions,
            "magic": participant.magicDamageDealtToChampions,
            "physical": participant.physicalDamageDealtToChampions,
        }
        for participant in participants
    }

    fig = go.Figure()

    for participant_id, damage in damage_data.items():
        participant_name = "Vous" if participant_id == player_index else f"Joueur {participant_id}"
        team_color = "blue" if participant_id <= 5 else "red"
        pastel_color = "lightblue" if team_color == "blue" else "lightcoral"
        dark_color = "darkblue" if team_color == "blue" else "darkred"

        fig.add_trace(go.Bar(
            x=[participant_name],
            y=[damage["magic"]],
            name=f"Magic Damage - {participant_name}",
            marker=dict(color=dark_color),
            showlegend=False
        ))
        fig.add_trace(go.Bar(
            x=[participant_name],
            y=[damage["physical"]],
            name=f"Physical Damage - {participant_name}",
            marker=dict(color=pastel_color),
            showlegend=False
        ))

    fig.update_layout(
        title=f"Damage Done in Game {selected_game_id}",
        xaxis_title="Participants",
        yaxis_title="Total Damage Done",
        template="plotly_white",
        height=500,
        width=700,
        barmode="stack"
    )

    graph_content = GraphContainer(title="Damage Done Per Participant", figure=fig)

    return game_options, graph_content
