from dash import html, dcc, callback, Output, Input, State
from src.components import GraphContainer
import dash
import plotly.graph_objects as go
import numpy as np

# enregistre la page dans dash avec un chemin basé sur le nom du fichier
dash.register_page(__name__, '/' + __name__.split('.')[-1])

# définit la mise en page de la page
layout = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Dropdown(
                    id="game-dropdown2",
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

# définit le callback pour mettre à jour les options du dropdown et le contenu du graphique
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
    # vérifie si les données de la timeline sont stockées
    if not stored_timeline_games:
        return [], html.Div("Aucun pseudo stocké. Merci d'entrer un pseudo.", style={"color": "white"})

    from src.utils.pyltover.match import MatchTimeline
    # crée des objets MatchTimeline à partir des données stockées
    matchs = [MatchTimeline(None, data) for data in stored_timeline_games]

    # crée les options du menu déroulant à partir des matchs stockés
    game_options = []
    for game in matchs:
        winning_team = ""
        for frames in game.info.frames:
            for event in frames.events:
                if event.type == "GAME_END":
                    winning_team = "Bleu" if event.raw_data["winningTeam"] == 100 else "Rouge"
        game_options.append({"label": f"Partie {game.metadata.matchId} - Win: {winning_team}", "value": game.metadata.matchId})

    # si aucune partie n'est sélectionnée, retourne les options et un message
    if not selected_game_id:
        return game_options, html.Div("Selectionnez une partie pour voir les données.", style={"color": "white"})

    # trouve les données de la partie sélectionnée
    selected_game_data = next(
        (game for game in matchs if game.metadata.matchId == selected_game_id), None
    )

    # si les données de la partie ne sont pas trouvées, retourne les options et un message
    if not selected_game_data:
        return game_options, html.Div("Partie introuvable.", style={"color": "white"})

    frames = selected_game_data.info.frames
    # trouve l'index du joueur dans les participants
    player_index = None
    for participant in selected_game_data.info.participants:
        if participant.puuid == puuid_store:
            player_index = participant.participantId

    time_steps = range(len(frames))
    # initialise un dictionnaire pour stocker l'or des participants
    participant_gold = {frame.participantId: [] for frame in frames[0].participantFrames}

    # remplit le dictionnaire avec les valeurs d'or pour chaque participant à chaque frame
    for frame in frames:
        for participant in frame.participantFrames:
            participant_gold[participant.participantId].append(participant.totalGold)

    fig = go.Figure()

    # ajoute une trace pour chaque participant au graphique
    for participant_id, gold_values in participant_gold.items():
        participant_name = "Vous" if participant_id == player_index else f"Joueur {participant_id}"
        fig.add_trace(go.Scatter(
            x=list(time_steps),
            y=gold_values,
            mode="lines",
            line=dict(width=2),
            name=participant_name
        ))

    # met à jour la mise en page du graphique
    fig.update_layout(
        title=f"Evolution des golds dans la partie {selected_game_id}",
        xaxis_title="Temps (minutes)",
        yaxis_title="Golds",
        template="plotly_white",
        height=500,
        width=700
    )

    # crée le contenu du graphique avec le conteneur de graphique personnalisé
    graph_content = GraphContainer(title="Evolution de la quantité de gold over time", figure=fig)

    return game_options, graph_content
