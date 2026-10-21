
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def train_and_evaluate(
    matches,
    features=None,
    train_season="2425",
    test_season="2526",
):
    if features is None:
        features = ["HomeForm", "AwayForm"]

    train = matches[
        matches["Season"] <= train_season
    ].copy()

    test = matches[
        matches["Season"] == test_season
    ].copy()

    model = LogisticRegression()
    model.fit(train[features], train["FTR"])

    predictions = model.predict(test[features])

    accuracy = accuracy_score(
        test["FTR"], predictions
    )

    print("Train:", len(train), "Test:", len(test))
    print("Accuracy:", accuracy)

    prediction_counts = pd.Series(
        predictions
    ).value_counts()

    return model, test, predictions, accuracy, prediction_counts
