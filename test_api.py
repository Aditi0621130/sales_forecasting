import requests

# Sample input
data = {
    "QUANTITYORDERED": 45,
    "PRICEEACH": 89.99,
    "MONTH": 12,
    "YEAR": 2004
}

# API call
response = requests.post("http://127.0.0.1:5000/predict", json=data)

# Print prediction
print("📈 Predicted Revenue:", response.json())