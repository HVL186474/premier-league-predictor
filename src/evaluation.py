 import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)


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
