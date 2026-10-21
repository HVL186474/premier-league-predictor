
from sklearn.linear_model import LogisticRegression


def train_model(matches, features):
    train = matches[matches["Season"] <= "2425"]
    test = matches[matches["Season"] == "2526"]

    model = LogisticRegression()
    model.fit(train[features], train["FTR"])

    return model, train, test
