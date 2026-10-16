from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

features = ["HomeForm", "AwayForm"]

train = matches[matches["Season"] <= "2425"]
test  = matches[matches["Season"] == "2526"]

model = LogisticRegression()
model.fit(train[features], train["FTR"])

predictions = model.predict(test[features])
print("Train:", len(train), "Test:", len(test))
print("Accuracy:", accuracy_score(test["FTR"], predictions))

pd.Series(predictions).value_counts()
