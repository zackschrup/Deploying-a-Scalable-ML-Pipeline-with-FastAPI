import numpy as np

from ml.data import apply_label
from ml.model import train_model,compute_model_metrics
from sklearn.ensemble import RandomForestClassifier


# TODO: implement the first test. Change the function name and input as needed
def test_label_application():
    """
    Test to see if the binary predictions are converted to labels.
    """
    assert apply_label([1]) == ">50K"
    assert apply_label([0]) == "<=50K"
    


# TODO: implement the second test. Change the function name and input as needed
def test_train_model():
    """
    Test to check if train_model returns a RandomForestClassifier.
    """
    X_train = np.array([
        [1,2],
        [2,3],
        [3,4],
        [4,5]
    ])

    y_train = np.array([0,0,1,1])

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)

    


# TODO: implement the third test. Change the function name and input as needed
def test_model_metrics():
    """
    Test if metric calculations return expected values.
    """
    y_true = np.array([1, 1, 0, 0])
    y_pred = np.array([1, 1, 0, 0])

    precision, recall, fbeta = compute_model_metrics(
        y_true,
        y_pred
    )

    assert precision == 1.0
    assert recall == 1.0
    assert fbeta == 1.0

