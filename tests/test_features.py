import pytest
from src import features
from src.features import expected_score, rating_change

def test_expected_score():
    assert expected_score(1000, 1000) == 0.5

def test_rating_change():
    assert rating_change(1000, 1000, 1) == 10

def test_expected_score_known_value():
    assert expected_score(1700, 1400) == pytest.approx(0.849, abs=0.001)

def test_expected_scores_of_both_teams_sum_to_one():
    assert expected_score(1700, 1400) + expected_score(1400, 1700) == pytest.approx(1.0)

def test_rating_change_draw_known_value():
    assert rating_change(1700, 1650, 0.5) == pytest.approx(-1.429, abs=0.001)

def test_rating_change_scales_with_k():
    assert rating_change(1600, 1500, 1, k=40) == pytest.approx(2 * rating_change(1600, 1500, 1, k=20))

def test_win_raises_rating_and_loss_lowers_rating():
    assert rating_change(1500, 1500, 1) > 0
    assert rating_change(1500, 1500, 0) < 0