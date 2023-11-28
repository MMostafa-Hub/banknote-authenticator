from autosklearn.classification import AutoSklearnClassifier
from flask import Flask, request, jsonify
from load_model import load_model
import pandas as pd

# Create the Flask app
app = Flask(__name__)

# The AutoSklearnClassifier model
model = None


@app.route("/authentication", methods=["GET"])
def authentication():
    """Endpoint for authentication.

    Returns:
        JSON: The authentication result.
    """
    global model
    test_data = pd.Series(request.get_json())
    return jsonify({"output": model.predict_proba(test_data)[1]}), 200


if __name__ == "__main__":
    # loading the ml model for inference
    model = load_model()

    # running the flask app
    app.run(debug=True, port=8400)
