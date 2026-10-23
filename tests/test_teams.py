from pathlib import Path

from src.prediction import load_artifacts
from src.teams import data_name, teams

def test_every_app_team_has_a_rating():
    _, ratings = load_artifacts()
    assert set(data_name.values()) == set(ratings)

def test_logos_exist():
    for _, logo, _, _ in teams:
        assert logo is None or Path(logo).exists()