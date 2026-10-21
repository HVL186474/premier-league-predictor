import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, log_loss
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
 
from src.data_loader import load_matches
from src.features import add_elo, add_form
from src.preprocessing import preprocess_matches
from src.split import split_by_season

CLASSES = ["A", "D", "H"]
 
FEATURE_SETS = {
      "Elo only": ["EloDiff"],
      "Form only": ["HomeForm", "AwayForm"],
      "Elo + form": ["EloDiff", "HomeForm", "AwayForm"],
  }

def build_matches():
      return add_elo(add_form(preprocess_matches(load_matches())))


def logistic_regression():
      # Skalerer først, så Elo (~1500) og form (0-3) får like stor sjanse i modellen
      return make_pipeline(StandardScaler(), LogisticRegression())
 
 
def class_frequency_probabilities(train, n_matches):
      """Give every match the same probabilities: how often A, D and H happened in training."""
      frequencies = train["FTR"].value_counts(normalize=True).reindex(CLASSES)
      return np.tile(frequencies.to_numpy(), (n_matches, 1))
 
 
def bookmaker_probabilities(matches):
      """Bet365 odds turned into probabilities. Benchmark only, never a feature (decision D1)."""
      implied = 1 / matches[["B365A", "B365D", "B365H"]].to_numpy()
      return implied / implied.sum(axis=1, keepdims=True)
 
  
def results_row(name, y_true, probabilities):
      predicted = np.array(CLASSES)[probabilities.argmax(axis=1)]
      return {
          "Model": name,
          "Log loss": log_loss(y_true, probabilities, labels=CLASSES),
          "Accuracy": accuracy_score(y_true, predicted),
          "Draws predicted": (predicted == "D").mean(),
      }

def compare_on_validation(matches):
      """Score every model on the validation season. The test season is not touched."""
      train, validation, _ = split_by_season(matches)
      y = validation["FTR"]
     
      rows = [results_row("Class frequencies", y, class_frequency_probabilities(train, len(validation)))]
 
      for name, features in FEATURE_SETS.items():
          model = logistic_regression().fit(train[features], train["FTR"])
          assert list(model.classes_) == CLASSES
          rows.append(results_row(f"LogReg: {name}", y, model.predict_proba(validation[features])))
          
      rows.append(results_row("Bet365 (benchmark)", y, bookmaker_probabilities(validation)))
     
      return pd.DataFrame(rows).sort_values("Log loss", ignore_index=True)
     
if __name__ == "__main__":
      table = compare_on_validation(build_matches())
      print(table.to_string(index=False, float_format="%.4f"))