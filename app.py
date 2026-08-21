
from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os


# ============================================================
# CREATE FLASK APPLICATION
# ============================================================

app = Flask(__name__)


# ============================================================
# MODEL PATH
# ============================================================

MODEL_PATH = os.environ.get(
    "MODEL_PATH",
    "ExtraaLearn_Best_Lead_Conversion_Model.pkl"
)


# ============================================================
# LOAD MACHINE LEARNING MODEL
# ============================================================

try:

    model = joblib.load(MODEL_PATH)

    print("=" * 60)
    print("MODEL LOADED SUCCESSFULLY")
    print("=" * 60)

    print("Model path:", MODEL_PATH)

except Exception as e:

    print("=" * 60)
    print("ERROR LOADING MODEL")
    print("=" * 60)

    print("Error:", str(e))

    model = None


# ============================================================
# HOME ENDPOINT
# ============================================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({

        "application":
            "ExtraaLearn Lead Conversion Prediction API",

        "status":
            "running",

        "description":
            "Machine Learning API for predicting "
            "lead conversion",

        "endpoints": {

            "home":
                "GET /",

            "health":
                "GET /health",

            "prediction":
                "POST /predict"

        }

    })


# ============================================================
# HEALTH CHECK ENDPOINT
# ============================================================

@app.route("/health", methods=["GET"])
def health():

    if model is not None:

        return jsonify({

            "status":
                "healthy",

            "model_loaded":
                True

        }), 200

    else:

        return jsonify({

            "status":
                "unhealthy",

            "model_loaded":
                False

        }), 500


# ============================================================
# PREDICTION ENDPOINT
# ============================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ----------------------------------------------------
        # Check model
        # ----------------------------------------------------

        if model is None:

            return jsonify({

                "error":
                    "Machine learning model "
                    "is not loaded."

            }), 500


        # ----------------------------------------------------
        # Get JSON request
        # ----------------------------------------------------

        data = request.get_json(
            silent=True
        )


        if data is None:

            return jsonify({

                "error":
                    "Request body must contain "
                    "valid JSON."

            }), 400


        # ----------------------------------------------------
        # Convert JSON into DataFrame
        # ----------------------------------------------------

        input_data = pd.DataFrame(
            [data]
        )


        # ----------------------------------------------------
        # Make prediction
        # ----------------------------------------------------

        prediction = model.predict(
            input_data
        )[0]


        # ----------------------------------------------------
        # Calculate conversion probability
        # ----------------------------------------------------

        probability = None


        if hasattr(
            model,
            "predict_proba"
        ):

            probabilities = model.predict_proba(
                input_data
            )

            probability = float(
                probabilities[0][1]
            )


        # ----------------------------------------------------
        # Business-friendly prediction
        # ----------------------------------------------------

        if int(prediction) == 1:

            status = "Converted"

        else:

            status = "Not Converted"


        # ----------------------------------------------------
        # Prepare response
        # ----------------------------------------------------

        response = {

            "prediction":
                int(prediction),

            "status":
                status

        }


        if probability is not None:

            response[
                "conversion_probability"
            ] = round(
                probability,
                4
            )


        return jsonify(
            response
        ), 200


    except Exception as e:

        return jsonify({

            "error":
                str(e)

        }), 400


# ============================================================
# 404 ERROR HANDLER
# ============================================================

@app.errorhandler(404)
def page_not_found(error):

    return jsonify({

        "error":
            "Endpoint not found."

    }), 404


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            10000
        )
    )

    app.run(

        host="0.0.0.0",

        port=port,

        debug=False

    )
