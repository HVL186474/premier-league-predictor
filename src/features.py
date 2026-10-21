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

def add_elo(matches, k=ELO_K):
      """Add HomeElo, AwayElo and EloDiff: both teams' Elo ratings before the match."""
      ratings = {}
      previous_teams = None
      home_elo = {}
      away_elo = {}
      
      ordered = matches.sort_values("Date", kind="stable")
      
      for season in ordered["Season"].unique():
          season_matches = ordered[ordered["Season"] == season]
          teams = set(season_matches["HomeTeam"]) | set(season_matches["AwayTeam"])
          
          if previous_teams is None:
              for team in teams:
                  ratings[team] = ELO_START
          else:   
              relegated = previous_teams - teams
              promoted = teams - previous_teams
              if promoted:
                  start = sum(ratings[team] for team in relegated) / len(relegated)
                  for team in promoted:
                      ratings[team] = start

          for idx, row in season_matches.iterrows():
                home = row["HomeTeam"]
                away = row["AwayTeam"]
                h = ratings[home]
                a = ratings[away]

                home_elo[idx] = h
                away_elo[idx] = a
            
                result = {"H": 1, "D": 0.5, "A": 0}[row["FTR"]]
                change = rating_change(h, a, result, k)
                ratings[home] = h + change
                ratings[away] = a - change
    
          previous_teams = teams

      result = matches.copy()
      result["HomeElo"] = pd.Series(home_elo)
      result["AwayElo"] = pd.Series(away_elo)
      result["EloDiff"] = result["HomeElo"] - result["AwayElo"]
      return result