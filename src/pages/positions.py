from dash import html, dcc, callback, Output, Input, State
from src.components import GraphContainer
import dash
import plotly.graph_objects as go
import numpy as np
from PIL import Image
import base64

dash.register_page(__name__, '/' + __name__.split('.')[-1])

layout = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Dropdown(
                    id="game-dropdown",
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
            children=[
                dcc.Slider(
                    id="time-slider",
                    min=0,
                    max=1,
                    step=1,
                    value=0,
                    marks={},
                    tooltip={"placement": "bottom", "always_visible": True},
                ),
            ],
            style={
                "padding": "0 20px",
            },
        ),
        html.Div(
            id="position-graph-container",
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
        Output("game-dropdown", "options"),
        Output("time-slider", "max"),
        Output("time-slider", "marks"),
        Output("position-graph-container", "children"),
    ],
    [
        Input("game-dropdown", "value"),
        Input("time-slider", "value"), 
        Input("stored-pseudo", "data"),
    ],
    [
        State("matchs-timeline-store", "data"),
        State("puuid-store", "data"),
    ],
    prevent_initial_call=False,
)
def update_dropdown_slider_and_graph(selected_game_id, slider_value, _pseudo, stored_timeline_games, puuid_store):
    if not stored_timeline_games:
        return [], 1, {}, html.Div("Aucun pseudo stocké. Merci d'entrer un pseudo.", style={"color": "white"})

    from src.utils.pyltover.match import MatchTimeline
    matchs = [MatchTimeline(None, data) for data in stored_timeline_games]

    game_options = [
        {"label": f"Partie {game.metadata.matchId}", "value": game.metadata.matchId}
        for game in matchs
    ]

    if not selected_game_id:
        return game_options, 1, {}, html.Div("Selectionnez une partie pour voir les données.", style={"color": "white"})

    selected_game_data = next(
        (game for game in matchs if game.metadata.matchId == selected_game_id), None
    )

    if not selected_game_data:
        return game_options, 1, {}, html.Div("Partie introuvable.", style={"color": "white"})

    max_time = len(selected_game_data.info.frames) - 1
    marks = {i: str(i) for i in range(max_time + 1)}

    player_index = [participant.participantId for participant in selected_game_data.info.participants if participant.puuid == puuid_store][0]

    if slider_value is None or slider_value > max_time:
        slider_value = 0

    frames_data = selected_game_data.info.frames[slider_value].participantFrames

    x_positions = []
    y_positions = []
    colors = []
    for frame in frames_data:
        x_positions.append(frame.position.x)
        y_positions.append(frame.position.y)
        if frame.participantId == player_index:
            if player_index <=5:
                colors.append("#80ccff")
            else:
                colors.append("#ff8080")
        elif 0 <= frame.participantId <= 5:
            colors.append("blue") 
        else:
            colors.append("red") 

    image_path = "assets/Summoner's_Rift_Minimap2.png"
    img = Image.open(image_path)
    img_width, img_height = img.size
    x_min, y_min = -120, -120
    x_max, y_max = 14870, 14980

    def scale_coordinates(x, y, img_width, img_height):
        scaled_x = (x - x_min) / (x_max - x_min) * img_width
        scaled_y = (y - y_min) / (y_max - y_min) * img_height
        return scaled_x, scaled_y

    scaled_x_positions = []
    scaled_y_positions = []
    for x, y in zip(x_positions, y_positions):
        scaled_x, scaled_y = scale_coordinates(x, y, img_width, img_height)
        scaled_x_positions.append(scaled_x)
        scaled_y_positions.append(scaled_y)

    with open(image_path, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode("utf-8")
    encoded_image = f"data:image/png;base64,{encoded_image}"

    fig = go.Figure()
    fig.add_layout_image(
        dict(
            source=encoded_image,
            xref="x",
            yref="y",
            x=0,
            y=img_height,
            sizex=img_width,
            sizey=img_height,
            xanchor="left",
            yanchor="top",
            layer="below"
        )
    )

    fig.add_trace(go.Scatter(
        x=scaled_x_positions,
        y=scaled_y_positions,
        mode="markers",
        marker=dict(size=8, color=colors),
    ))

    fig.update_layout(
        xaxis=dict(range=[0, img_width], showgrid=False, zeroline=False),
        yaxis=dict(range=[0, img_height], showgrid=False, zeroline=False, scaleanchor="x"),
        height=500,
        width=500,
        template="plotly_white"
    )

    graph_content = GraphContainer(title=f"Positions at {slider_value} min", figure=fig)

    return game_options, max_time, marks, graph_content
