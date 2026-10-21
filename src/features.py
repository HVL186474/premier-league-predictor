
import pandas as pd


def add_form_features(matches, window=5):
    matches = matches.copy()

    matches["Date"] = pd.to_datetime(
        matches["Date"],
        dayfirst=True,
        format="mixed",
    )

    home = pd.DataFrame({
        "Date": matches["Date"],
        "Team": matches["HomeTeam"],
        "Home": True,
        "Points": matches["FTR"].map({
            "H": 3, "D": 1, "A": 0
        }),
    })

    away = pd.DataFrame({
        "Date": matches["Date"],
        "Team": matches["AwayTeam"],
        "Home": False,
        "Points": matches["FTR"].map({
            "H": 0, "D": 1, "A": 3
        }),
    })

    team_matches = pd.concat([home, away])
    team_matches = team_matches.sort_values("Date")

    team_matches["Form"] = (
        team_matches.groupby("Team")["Points"]
        .transform(
            lambda s: s.shift(1)
            .rolling(window, min_periods=1)
            .mean()
        )
    )

    matches["HomeForm"] = (
        team_matches[team_matches["Home"]]["Form"]
    )
    matches["AwayForm"] = (
        team_matches[~team_matches["Home"]]["Form"]
    )

    return matches
