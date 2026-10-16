import pandas as pd

FORM_WINDOW = 5
MISSING_FORM = 0.79

ELO_K = 20
ELO_START = 1500

# Definerer ELO hjelpere: 

# Forventet score for hjemmelaget gitt deres rating og bortelagets rating
def expected_score(home_rating, away_rating):
    return 1 / (1 + 10 ** ((away_rating - home_rating) / 400))

# Endrer rating basert på resultatet av kampen og forventet score
def rating_change(home_rating, away_rating, result, k=ELO_K):
    return k * (result - expected_score(home_rating, away_rating))

def add_form(matches, window=FORM_WINDOW):
    home = pd.DataFrame({
      "Date": matches["Date"],
      "Team": matches["HomeTeam"],
      "Home": True,
      "Points": matches["FTR"].map({"H": 3, "D": 1, "A": 0}),
  })  

    away = pd.DataFrame({
        "Date": matches["Date"],
        "Team": matches["AwayTeam"],
        "Home": False,
        "Points": matches["FTR"].map({"H": 0, "D": 1, "A": 3}),
    })  

    team_matches = pd.concat([home, away]).sort_values("Date", kind="stable")

    team_matches["Form"] = (
        team_matches.groupby("Team")["Points"]
        .transform(lambda s: s.shift(1).rolling(window, min_periods=1).mean())
    )

    matches = matches.copy()
    matches["HomeForm"] = team_matches.loc[team_matches["Home"], "Form"].fillna(MISSING_FORM)
    matches["AwayForm"] = team_matches.loc[~team_matches["Home"], "Form"].fillna(MISSING_FORM)

    return matches

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

def add_elo(matches, k=ELO_K):
    """Add HomeElo, AwayElo and EloDiff: both teams' Elo ratings before the match."""
    rating = {}
    previous_teams = None
    home_elo = {}
    away_elo = {}

    matches = matches.sort_values("Date")

    home_elo = []
    away_elo = []
    ratings = {}
    previous_teams = None

    for season in matches["Season"].unique():
        season_matches = matches[matches["Season"] == season]
        teams = set(season_matches["HomeTeam"]) | set(season_matches["AwayTeam"])

        if previous_teams is None:
            for team in teams:
                ratings[team] = 1500
        else:
            relegated = previous_teams - teams
            promoted = teams - previous_teams
            start = sum(ratings[t] for t in relegated) / len(relegated)
            print(season, "relegated:", sorted(relegated), "promoted:", sorted(promoted), "start:", start)            
            for team in promoted:
                ratings[team] = start

        for _, row in season_matches.iterrows():
            home = row["HomeTeam"]
            away = row["AwayTeam"]
            h = ratings[home]
            a = ratings[away]
            
            home_elo.append(h)   
            away_elo.append(a)

            result = {"H": 1, "D": 0.5, "A": 0}[row["FTR"]]
            change = rating_change(h, a, result)
            ratings[home] = h + change
            ratings[away] = a - change

        previous_teams = teams
    
    matches["HomeElo"] = home_elo    
    matches["AwayElo"] = away_elo
    matches["EloDiff"] = matches["HomeElo"] - matches["AwayElo"]