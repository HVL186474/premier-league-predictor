import pandas as pd
import pytest
from sklearn.dummy import DummyClassifier
  
from src.evaluation import score
  

def test_score_known_values(): 
    X = pd.DataFrame({"x": [0, 0, 0, 0]})
    y = pd.Series(["H", "H", "D", "A"])
    model = DummyClassifier(strategy="prior").fit(X, y)
 
    result = score(model, X, y)
 
    assert result["log_loss"] == pytest.approx(1.0397, abs=0.0001)
    assert result["accuracy"] == 0.5