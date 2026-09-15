import joblib
from pathlib import Path


def load_model():
    model_path = Path("models") / "iris_model.pkl"

    model = joblib.load(model_path)

    return model