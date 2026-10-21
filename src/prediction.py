
def predict_matches(model, test, features):
    predictions = model.predict(test[features])
    return predictions
