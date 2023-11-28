# from sklearn.calibration import CalibratedClassifierCV
from flask import Flask, request, jsonify
import pandas as pd
import pickle

# Create the Flask app
app = Flask(__name__)

# Loading the calibrated model
print("Loading model...")
model = pickle.load(open("../models/calibrated_model.pkl", "rb"))
print("Model loaded.")


@app.route("/authentication", methods=["GET"])
def authentication():
    """Endpoint for authentication.

    Returns:
        JSON: The authentication result.
    """
    global model
    test_data = pd.Series(request.get_json()).to_frame().T
    return jsonify({"output": model.predict_proba(test_data)[:, 1][0]}), 200


if __name__ == "__main__":
    # running the flask app
    app.run(debug=False, use_reloader=False)
