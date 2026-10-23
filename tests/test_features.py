import pandas as pd
import pytest

from src.features import add_elo, add_form, expected_score, rating_change

def test_expected_score():
    assert expected_score(1000, 1000) == 0.5

def test_rating_change():
    assert rating_change(1000, 1000, 1, k = 20) == 10

def test_expected_score_known_value():
    assert expected_score(1700, 1400) == pytest.approx(0.849, abs=0.001)

def test_expected_scores_of_both_teams_sum_to_one():
    assert expected_score(1700, 1400) + expected_score(1400, 1700) == pytest.approx(1.0)

def test_rating_change_draw_known_value():
    assert rating_change(1700, 1650, 0.5, k = 20) == pytest.approx(-1.429, abs=0.001)

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

def make_elo_matches(second_season_away="E"):
      # Season 1: A, B, C, D play two rounds. Season 2: D is relegated and E is promoted
      return pd.DataFrame({
          "Season": ["1617"] * 4 + ["1718"] * 2,
          "Date": pd.to_datetime(["2020-01-01", "2020-01-01", "2020-01-02", "2020-01-02", "2021-01-01", "2021-01-01"]),
          "HomeTeam": ["A", "C", "A", "B", "A", "B"],
          "AwayTeam": ["B", "D", "C", "D", second_season_away, "C"],
          "FTR": ["H", "D", "A", "H", "D", "H"],
      })  


def test_elo_known_values():
      result = add_elo(make_elo_matches(), k = 20)
      # First match: both start at 1500. A wins, so A gains 20 * 0.5 = 10 and B loses 10
      assert result.loc[0, ["HomeElo", "AwayElo"]].tolist() == [1500, 1500]
      assert result.loc[2, ["HomeElo", "AwayElo"]].tolist() == [1510, 1500]
      assert result.loc[3, ["HomeElo", "AwayElo"]].tolist() == [1490, 1500]
      assert result.loc[2, "EloDiff"] == 10
 
     
def test_elo_ratings_sum_is_conserved():
      result = add_elo(make_elo_matches())
      # Round 2 (rows 2 and 3) has every team once, so its ratings must add up to 4 * 1500
      round_two = result.loc[[2, 3], ["HomeElo", "AwayElo"]].to_numpy().sum()
      assert round_two == pytest.approx(4 * 1500)

def test_promoted_team_starts_at_relegated_average():
      result = add_elo(make_elo_matches(), k = 20)
      # D is the only relegated team, so E starts at D's rating after D's last match (row 3)
      d_before = result.loc[3, "AwayElo"]
      b_before = result.loc[3, "HomeElo"]
      d_after = d_before - 20 * (1 - expected_score(b_before, d_before))
      assert result.loc[4, "AwayElo"] == pytest.approx(d_after)
      
      
def test_elo_season_without_promotion_carries_ratings_over():
      result = add_elo(make_elo_matches(second_season_away="D"), k = 20)
      # Same four teams in season 2, so D keeps its rating and nothing crashes
      d_before = result.loc[3, "AwayElo"]
      b_before = result.loc[3, "HomeElo"]
      d_after = d_before - 20 * (1 - expected_score(b_before, d_before))
      assert result.loc[4, "AwayElo"] == pytest.approx(d_after)
     
     
def test_elo_does_not_use_the_match_own_result():
      matches = make_elo_matches()
      changed = matches.copy()
      changed.loc[2, "FTR"] = "H"
     
      before = add_elo(matches)
      after = add_elo(changed)
     
      assert before.loc[:3, ["HomeElo", "AwayElo"]].equals(after.loc[:3, ["HomeElo", "AwayElo"]])
      assert before.loc[4, "HomeElo"] != after.loc[4, "HomeElo"]

def test_elo_uses_k():
      matches = make_elo_matches()
      assert add_elo(matches, k=40).loc[2, "HomeElo"] == 1520
     
      
def test_elo_rows_stay_matched_when_input_is_shuffled():
      matches = make_elo_matches()
      shuffled = matches.sample(frac=1, random_state=0)
     
      expected = add_elo(matches)
      result = add_elo(shuffled)
     
      assert result.index.tolist() == shuffled.index.tolist()
      assert result.loc[matches.index, "HomeElo"].equals(expected["HomeElo"])
     
     
def test_add_elo_does_not_change_the_input():
      matches = make_elo_matches()
      add_elo(matches)
      assert "HomeElo" not in matches.columns