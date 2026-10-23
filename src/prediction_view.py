import streamlit as st

from src.prediction import load_artifacts, predict
from src.teams import data_name


@st.cache_resource
def get_model():
    return load_artifacts()


def show_prediction(home_team, away_team):
    """Show H/D/A probabilities. Takes the app's team names, e.g. "Manchester City"."""
    model, ratings = get_model()
    result = predict(model, ratings, data_name[home_team], data_name[away_team])

    home_col, draw_col, away_col = st.columns(3)
    home_col.metric(f"{home_team} win", f"{result['H']:.0%}")
    draw_col.metric("Draw", f"{result['D']:.0%}")
    away_col.metric(f"{away_team} win", f"{result['A']:.0%}")

    st.caption(
        "Based on each team's current Elo rating. "
        "A draw is almost never the single most likely result, "
        "even though about a quarter of matches end level."
    )