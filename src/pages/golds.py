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
                    id="game-dropdown2",
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
            id="gold-graph-container",
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
        Output("game-dropdown2", "options"),
        Output("gold-graph-container", "children"),
    ],
    [
        Input("game-dropdown2", "value"),
        Input("stored-pseudo", "data"),
    ],
    [
        State("matchs-timeline-store", "data"),
        State("puuid-store", "data"),
    ],
    prevent_initial_call=False,
)
def update_gold_graph(selected_game_id, _pseudo, stored_timeline_games, puuid_store):
    if not stored_timeline_games:
        return [], html.Div("Aucun pseudo stocké. Merci d'entrer un pseudo.", style={"color": "white"})

    from src.utils.pyltover.match import MatchTimeline
    matchs = [MatchTimeline(None, data) for data in stored_timeline_games]

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

    frames = selected_game_data.info.frames
    player_index = [participant.participantId for participant in selected_game_data.info.participants if participant.puuid == puuid_store][0]

    time_steps = range(len(frames))
    participant_gold = {frame.participantId: [] for frame in frames[0].participantFrames}

    for frame in frames:
        for participant in frame.participantFrames:
            participant_gold[participant.participantId].append(participant.totalGold)

    fig = go.Figure()

    for participant_id, gold_values in participant_gold.items():
        participant_name = "Vous" if participant_id == player_index else f"Joueur {participant_id}"
        fig.add_trace(go.Scatter(
            x=list(time_steps),
            y=gold_values,
            mode="lines",
            line=dict(width=2),
            name=participant_name
        ))

    # Update layout
    fig.update_layout(
        title=f"Gold Evolution in Game {selected_game_id}",
        xaxis_title="Time (minutes)",
        yaxis_title="Gold Amount",
        template="plotly_white",
        height=500,
        width=700
    )

    graph_content = GraphContainer(title="Gold Evolution Over Time", figure=fig)

    return game_options, graph_content
