import pandas as pd


def preprocess_matches(matches):
    matches = matches.copy()

    # Convert dates to datetime
    matches["Date"] = pd.to_datetime(
        matches["Date"],
        dayfirst=True,
        format="mixed"
    )

    # Remove rows without a match result
    matches = matches.dropna(
        subset=["Date", "HomeTeam", "AwayTeam", "FTR"]
    )

    return matches
