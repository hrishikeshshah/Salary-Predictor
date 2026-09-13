import os
import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the trained salary prediction model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "reg_model.pkl")

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict/", methods=["POST"])
def predict():
    try:
        years = float(request.form["experience"])

        if years < 0:
            return render_template(
                "index.html",
                prediction_text="Please enter a valid number of years."
            )

        features = np.array([[years]])
        prediction = model.predict(features)
        output = round(float(prediction[0]), 2)

        return render_template(
            "index.html",
            prediction_text=f"Predicted salary is ${output:,.2f}",
            experience=years
        )

    except (ValueError, TypeError, KeyError):
        return render_template(
            "index.html",
            prediction_text="Please enter a valid number."
        )


if __name__ == "__main__":
    # Render provides the PORT environment variable.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
