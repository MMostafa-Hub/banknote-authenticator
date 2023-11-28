from autosklearn.classification import AutoSklearnClassifier
import pickle


def load_model() -> AutoSklearnClassifier:
    """Load the model object from disk."""
    with open("../models/calibrated_model.pkl", "rb") as f:
        model = pickle.load(f)

    return model
