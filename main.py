from backend.data_loader import load_iris_data
from models.predict import make_prediction
from models.load_model import load_model
from sklearn.datasets import load_iris

loaded_model = load_model()
print("Saved model loaded successfully!")

iris = load_iris()  

features = [5.1, 3.5, 1.4, 0.2]

prediction = make_prediction(
    loaded_model,
    features,
    iris.target_names,
    iris.feature_names
)

print("\nPrediction:", prediction)