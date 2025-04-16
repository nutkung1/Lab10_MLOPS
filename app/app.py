from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return "ML Model is Running"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Check if 'features' key exists in the request
    if "features" not in data:
        return jsonify({"error": "'features' key is required in the request"}), 400

    # Get the list of features
    input_features_list = data["features"]

    # Validate that each input is a list of 4 floats
    for idx, feature_set in enumerate(input_features_list):
        if len(feature_set) != 4:
            return (
                jsonify(
                    {"error": f"Input {idx + 1} does not contain exactly 4 values."}
                ),
                400,
            )
        if not all(isinstance(val, (float, int)) for val in feature_set):
            return (
                jsonify({"error": f"Input {idx + 1} contains non-numeric values."}),
                400,
            )

    # Convert the list of inputs into a numpy array
    input_features = np.array(input_features_list)

    # Get predictions for all input sets
    predictions = model.predict(input_features)

    # Get confidence scores for all input sets
    confidence_scores = np.max(model.predict_proba(input_features), axis=1)

    # Return predictions and confidence as a JSON response
    return jsonify(
        {"predictions": predictions.tolist(), "confidence": confidence_scores.tolist()}
    )


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
