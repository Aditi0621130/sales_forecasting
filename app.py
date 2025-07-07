from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load("data/sales_data.pkl")

@app.route("/")
def index():
    return "✅ Sales Prediction Model API is running!"

# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Get values from request JSON
        qty = data['QUANTITYORDERED']
        price = data['PRICEEACH']
        month = data['MONTH']
        year = data['YEAR']

        # Format into numpy array
        input_data = np.array([[qty, price, month, year]])

        # Make prediction
        prediction = model.predict(input_data)

        return jsonify({
            "Predicted Revenue": round(float(prediction[0]), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the app
if __name__ == "__main__":
    app.run(debug=True)