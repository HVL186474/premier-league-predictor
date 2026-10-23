from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.calibration import calibration_curve

from src.compare_models import (
    CLASSES,
    bookmaker_probabilities,
    class_frequency_probabilities,
    logistic_regression,
    results_row,
)

from src.data_loader import load_matches
from src.features import add_elo, add_form
from src.preprocessing import preprocess_matches
from src.split import split_by_season

FEATURES = ["EloDiff"]
FIGURES = Path("figures")

def fit_on_known_seasons(matches):
      """Train on train + validation, the seasons played before the test season."""
      train, validation, test = split_by_season(matches)
      known = pd.concat([train, validation])
      model = logistic_regression().fit(known[FEATURES], known["FTR"])
      return model, known, test

def evaluate_on_test():
      """Run ONCE. Scores the chosen model and baselines on the 2025/26 test season."""
      matches = add_form(preprocess_matches(load_matches()))
      model, known, test = fit_on_known_seasons(add_elo(matches))
      baseline, _, baseline_test = fit_on_known_seasons(add_elo(matches, k=20))
     
      y = test["FTR"]
      probabilities = model.predict_proba(test[FEATURES])
      rows = [
          results_row("Class frequencies", y, class_frequency_probabilities(known, len(test))),
          results_row("LogReg: Elo only, K = 20", y, baseline.predict_proba(baseline_test[FEATURES])),
          results_row("LogReg: Elo only, K = 30 (chosen)", y, probabilities),
          results_row("Bet365 (benchmark)", y, bookmaker_probabilities(test)),
      ]   
      return pd.DataFrame(rows), y, probabilities

def save_figures(y, probabilities):
      FIGURES.mkdir(exist_ok=True)
     
      predicted = np.array(CLASSES)[probabilities.argmax(axis=1)]
      ConfusionMatrixDisplay.from_predictions(y, predicted, labels=["H", "D", "A"])
      plt.title("Chosen model, 2025/26 test season")
      plt.savefig(FIGURES / "confusion_matrix.png", dpi=150, bbox_inches="tight")
      plt.close()
      
      fig, ax = plt.subplots()
      for column, result in enumerate(CLASSES):
          observed, predicted_mean = calibration_curve(
              y == result, probabilities[:, column], n_bins=8, strategy="quantile"
          )   
          ax.plot(predicted_mean, observed, marker="o", label=result)
      ax.plot([0, 1], [0, 1], linestyle="--", color="grey", label="Perfect")
      ax.set_xlabel("Predicted probability")
      ax.set_ylabel("How often it happened")
      ax.set_title("Calibration, 2025/26 test season")
      ax.legend()
      fig.savefig(FIGURES / "calibration.png", dpi=150, bbox_inches="tight")
      plt.close(fig)

if __name__ == "__main__":
      table, y, probabilities = evaluate_on_test()
      print(table.to_string(index=False, float_format="%.4f"))
      save_figures(y, probabilities)
