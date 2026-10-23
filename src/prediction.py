import json
from pathlib import Path

import joblib
import pandas as pd

MODELS = Path(__file__).resolve().parent.parent / "models"
RESULTS = ["H", "D", "A"]

def load_artifacts(folder=MODELS):
    """Load what train.py saved: the model and each team's current Elo (blueprint §8)."""
    model = joblib.load(folder / "model.joblib")
    state = pd.read_csv(folder / "team_state.csv")
    features = json.loads((folder / "features.json").read_text())
    if features != ["EloDiff"]:
        raise ValueError(f"predict() only builds EloDiff, but the model wants {features}")
    return model, dict(zip(state["Team"], state["Elo"]))

def predict(model, ratings, home, away):
    """H/D/A probabilities for one fixture. Takes the data's team names, e.g. "Man City"."""
    row = pd.DataFrame({"EloDiff": [ratings[home] - ratings[away]]})
    by_result = dict(zip(model.classes_, model.predict_proba(row)[0]))
    return {result: float(by_result[result]) for result in RESULTS}
