from backend.data_loader import load_iris_data
from preprocessing.preprocess import split_data
from models.model import train_model
from models.save_model import save_model


df = load_iris_data()

X_train, X_test, y_train, y_test = split_data(df)

model = train_model(X_train, y_train)

model_path = save_model(model)

print("Model trained successfully!")
print("Model saved at:", model_path)
