import pandas as pd
import pytest

from src.features import add_form, expected_score, rating_change

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

def make_matches():
      return pd.DataFrame({
          "Season": ["1617"] * 4,
          "Date": pd.to_datetime(["2020-01-01", "2020-01-02", "2020-01-03", "2020-01-04"]),
          "HomeTeam": ["A", "B", "C", "A"],
          "AwayTeam": ["B", "C", "A", "B"],
          "FTR": ["H", "D", "A", "D"],
      })  
     
 
def test_form_known_values():
      result = add_form(make_matches())
      assert list(result["HomeForm"]) == pytest.approx([0.79, 0.0, 1.0, 3.0])
      assert list(result["AwayForm"]) == pytest.approx([0.79, 0.79, 3.0, 0.5])
     
     
def test_form_does_not_use_the_match_own_result():
      matches = make_matches()
      changed = matches.copy()
      changed.loc[2, "FTR"] = "H"
     
      before = add_form(matches)
      after = add_form(changed)
     
      assert before.loc[:2, ["HomeForm", "AwayForm"]].equals(after.loc[:2, ["HomeForm", "AwayForm"]])
      assert before.loc[3, "HomeForm"] != after.loc[3, "HomeForm"]
     
     
def test_form_window_limits_how_many_matches_count():
      result = add_form(make_matches(), window=1)
      assert result.loc[3, "HomeForm"] == 3.0
      assert result.loc[3, "AwayForm"] == 1.0

def test_add_form_does_not_change_the_input():
      matches = make_matches()
      add_form(matches)
      assert "HomeForm" not in matches.columns