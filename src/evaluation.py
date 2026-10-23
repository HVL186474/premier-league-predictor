import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    log_loss,
)

def score(model, X, y):
      """Score a fitted model on X, y. Every model in the project is compared with this."""
      probabilities = model.predict_proba(X)
      predicted = model.classes_[probabilities.argmax(axis=1)]
      return {
          "log_loss": log_loss(y, probabilities, labels=model.classes_),
          "accuracy": accuracy_score(y, predicted),
      }

def evaluate_model(y_true, predictions):
    accuracy = accuracy_score(y_true, predictions)

    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification report:")
    print(classification_report(y_true, predictions))

    print("\nConfusion matrix:")
    print(confusion_matrix(
        y_true,
        predictions,
        labels=["H", "D", "A"],
    ))

    print("\nPredicted result distribution:")
    print(
        pd.Series(predictions)
        .value_counts(normalize=True)
        .reindex(["H", "D", "A"], fill_value=0)
    )

    return {
        "accuracy": accuracy,
        "classification_report": classification_report(
            y_true, predictions, output_dict=True
        ),
        "confusion_matrix": confusion_matrix(
            y_true, predictions, labels=["H", "D", "A"]
        ),
    }
