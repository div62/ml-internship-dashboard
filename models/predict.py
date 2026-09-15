import pandas as pd


def make_prediction(model, features, target_names, feature_names):
    input_data = pd.DataFrame(
        [features],
        columns=feature_names
    )

    prediction = model.predict(input_data)[0]

    return target_names[prediction]