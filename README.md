# For Homework Exercise 1 - 4, you can see it in the pictures directory; for Exercise 5, you can see it in the housing_app directory.
# 🏠 Housing Price Predictor API

A simple Flask-based machine learning API predicts housing prices based on various features like area, number of bedrooms, bathrooms, and more. The model is trained using a dataset of housing properties and deployed via Docker.

---

## 🚀 Features

- Predict house price using regression
- Supports multiple input requests
- Input validation with helpful error messages
- Dockerized for easy deployment

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/housing-price-predictor.git
cd housing-price-predictor
```

### 2. Train the Model (if not already trained)
```bash
python train_model.py
```
This will generate a model.pkl file.

### 3. Run the Flask App
```bash
python house_app.py
```
Or run using Docker:

```bash
docker build -t housing-price-predictor .
docker run -p 9000:9000 housing-price-predictor
```

🧪 Sample API Request
Endpoint
bash
Copy
Edit
POST /predict
URL
bash
Copy
Edit
http://localhost:9000/predict
✅ Sample JSON Input
json
Copy
Edit
{
  "features": [
    [7420, 4, 2, 3, 1, 1, 0, 0, 1, 1, 3, 1, 0],
    [8960, 3, 3, 2, 0, 1, 1, 1, 0, 1, 2, 1, 2]
  ]
}
# ✅ Sample JSON Response
```json
{
  "predictions": [13300000.0, 12250000.0]
}
```
⚠️ Error Handling Example
Invalid Input (Wrong Number of Features)
```json
{
  "features": [[7420, 4]]
}
```
Response
```json
{
  "error": "Each input must contain exactly 13 numeric features."
}
```
# 📂 Dataset Columns Used
The model uses the following columns from Housing.csv:
price, area, bedrooms, bathrooms, stories,
mainroad, guestroom, basement, hotwaterheating,
airconditioning, parking, prefarea, furnishingstatus
🔄 Note: Categorical features are one-hot encoded before training.
