from sklearn.datasets import load_iris
import pandas as pd


def load_iris_data():
    iris = load_iris()

    df = pd.DataFrame(
        iris.data,
        columns=iris.feature_names
    )

    df["target"] = iris.target
    df["target_name"] = df["target"].map(
        dict(enumerate(iris.target_names))
    )

    return df