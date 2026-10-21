import numpy as np
import pandas as pd
import pytest
 
from src.compare_models import bookmaker_probabilities, class_frequency_probabilities, results_row
     
 
def test_bookmaker_probabilities_sum_to_one():
      odds = pd.DataFrame({"B365A": [4.0, 2.5], "B365D": [3.5, 3.2], "B365H": [1.9, 2.8]})
      probabilities = bookmaker_probabilities(odds)
      assert probabilities.sum(axis=1) == pytest.approx([1.0, 1.0])
      assert probabilities[0].argmax() == 2
     
 
def test_class_frequency_probabilities_match_training_results():
      train = pd.DataFrame({"FTR": ["H", "H", "D", "A"]})
      probabilities = class_frequency_probabilities(train, n_matches=3)
      assert probabilities.shape == (3, 3)
      assert probabilities[0] == pytest.approx([0.25, 0.25, 0.5])
      

def test_results_row_known_values():
      probabilities = np.array([[0.2, 0.2, 0.6], [0.5, 0.3, 0.2]])
      row = results_row("Test", pd.Series(["H", "D"]), probabilities)
      assert row["Log loss"] == pytest.approx((-np.log(0.6) - np.log(0.3)) / 2)
      assert row["Accuracy"] == 0.5 
      assert row["Draws predicted"] == 0.0