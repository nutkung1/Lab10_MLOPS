from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model_house.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return "Housing Price Prediction Model is Running"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Get the input features from the request
    input_features = np.array(data["features"]).reshape(1, -1)

    # Make a prediction using the model
    prediction = model.predict(input_features)[0]

    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
