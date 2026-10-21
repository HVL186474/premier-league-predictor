import pandas as pd
import pytest 
  
from src.split import FINAL_TRAIN_SEASONS, select_seasons, split_by_season
  

def make_season_matches():
      seasons = ["1617", "1718", "1819", "1920", "2021", "2122", "2223", "2324", "2425", "2526", "2627"]
      return pd.DataFrame({"Season": seasons, "FTR": ["H"] * len(seasons)})
     
     
def test_split_puts_each_season_in_the_right_set():
      train, validation, test = split_by_season(make_season_matches())
      assert set(train["Season"]) == {"1718", "1819", "1920", "2021", "2122", "2223", "2324"}
      assert set(validation["Season"]) == {"2425"}
      assert set(test["Season"]) == {"2526"}
     
     
def test_split_leaves_out_warm_up_and_current_season():
      train, validation, test = split_by_season(make_season_matches())
      used = set(train["Season"]) | set(validation["Season"]) | set(test["Season"])
      assert "1617" not in used
      assert "2627" not in used
def test_split_sets_do_not_overlap():
      train, validation, test = split_by_season(make_season_matches())
      assert not set(train.index) & set(validation.index)
      assert not set(train.index) & set(test.index)
      assert not set(validation.index) & set(test.index)
     
     
def test_final_training_seasons_end_with_the_test_season():
      final = select_seasons(make_season_matches(), FINAL_TRAIN_SEASONS)
      assert set(final["Season"]) == {"1718", "1819", "1920", "2021", "2122", "2223", "2324", "2425", "2526"}
     
     
def test_missing_season_raises():
      matches = make_season_matches()
      with pytest.raises(ValueError, match="2425"):
          split_by_season(matches[matches["Season"] != "2425"])
          
          
def test_split_returns_copies():
      matches = make_season_matches()
      train, _, _ = split_by_season(matches)
      train["FTR"] = "A"
      assert (matches["FTR"] == "H").all()