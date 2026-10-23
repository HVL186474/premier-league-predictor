import json
from pathlib import Path

import joblib
import pandas as pd

from src.compare_models import logistic_regression
from src.data_loader import load_matches    
from src.features import add_elo, add_form, current_elo
from src.preprocessing import preprocess_matches
from src.split import FINAL_TRAIN_SEASONS, select_seasons

FEATURES = ["EloDiff"]
CURRENT_SEASON = "2627"
MODELS = Path("models")

def train_final_model(matches):
      """Fit the chosen model (decision D5) on every completed season."""
      train = select_seasons(matches, FINAL_TRAIN_SEASONS)
      return logistic_regression().fit(train[FEATURES], train["FTR"])
     
      
def team_state(matches):
    """Current Elo for each team in the current season, using the data's team names (D7)."""
    ratings = current_elo(matches)
    current = select_seasons(matches, [CURRENT_SEASON])
    teams = sorted(set(current["HomeTeam"]) | set(current["AwayTeam"]))
    return pd.DataFrame({"Team": teams, "Elo": [ratings[team] for team in teams]})
      
      
def save(model, state):
    MODELS.mkdir(exist_ok=True)
    joblib.dump(model, MODELS / "model.joblib")
    state.to_csv(MODELS / "team_state.csv", index=False)
    (MODELS / "features.json").write_text(json.dumps(FEATURES))
      
     
if __name__ == "__main__":
    matches = add_elo(add_form(preprocess_matches(load_matches())))
    model = train_final_model(matches)
    state = team_state(matches)
    save(model, state)
    print(state.sort_values("Elo", ascending=False).to_string(index=False))