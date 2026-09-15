import joblib
from pathlib import Path


def save_model(model):
    model_path = Path("models") / "iris_model.pkl"

    joblib.dump(model, model_path)

    return model_path