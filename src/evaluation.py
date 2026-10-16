from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

features = ["HomeForm", "AwayForm"]

#split data by season
train = matches[matches["Season"] <= "2425"].copy
test  = matches[matches["Season"] == "2526"].copy

# sjekke om tomme dataset

if train.empty
    raise ValueError("Training data is empty")

if test.empty
    raise ValueError("Test data is empty")

# Treningsmodell
model = LogisticRegression()
model.fit(train[features], train["FTR"])

# Predict test resultat
predictions = model.predict(test[features])

# Evaluering
print("Train:", len(train), "Test:", len(test))
print("Accuracy:", accuracy_score(test["FTR"], predictions))

pd.Series(predictions).value_counts()


test["FTR"].value_counts(normalize=True)