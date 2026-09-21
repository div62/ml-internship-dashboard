import joblib
from pathlib import Path


def load_model():
    model_path = Path("models") / "iris_model.pkl"

    if not model_path.exists():
        raise FileNotFoundError(
            "Trained model not found. Please run train.py first."
        )

    model = joblib.load(model_path)

    return model