import pytest

from src.prediction import load_artifacts, predict
  

@pytest.fixture(scope="module")
def artifacts():
    return load_artifacts()
      
     
def test_every_current_team_has_a_rating(artifacts):
    _, ratings = artifacts
    assert len(ratings) == 20
     
 
def test_probabilities_sum_to_one(artifacts):
    model, ratings = artifacts
    result = predict(model, ratings, "Arsenal", "Chelsea")
    assert list(result) == ["H", "D", "A"]
    assert sum(result.values()) == pytest.approx(1)


def test_stronger_team_is_favourite(artifacts):
    model, ratings = artifacts
    result = predict(model, ratings, "Man City", "Coventry")
    assert result["H"] > result["A"]


def test_home_advantage(artifacts):
    model, ratings = artifacts
    at_home = predict(model, ratings, "Arsenal", "Chelsea")["H"]
    away = predict(model, ratings, "Chelsea", "Arsenal")["A"]
    assert at_home > away